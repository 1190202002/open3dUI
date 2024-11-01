import open3d as o3d
import time
import copy
import laspy
import numpy as np
import pymeshlab
import convlas2mesh
import vtkmodules.all as vtk
from vtkmodules.util import vtkImageImportFromArray,vtkImageExportToArray
import matplotlib.pyplot as plt
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray,vtk_to_numpy
def preprocess_point_cloud(pcd, voxel_size, fpfh=False):
    pcd_down = pcd.voxel_down_sample(voxel_size)
    pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 1.4, max_nn=30))
    pcd.orient_normals_consistent_tangent_plane(100)
    if (fpfh == True):
        pcd_fpfh = o3d.pipelines.registration.compute_fpfh_feature(pcd_down,
                                                                   o3d.geometry.KDTreeSearchParamHybrid(
                                                                       radius=voxel_size * 5, max_nn=100))
        return pcd_down, pcd_fpfh
    else:
        return pcd_down

def fast_global_registration(target,source, voxel_size,correspondence_distance,iteration):
    source_down, source_fpfh = preprocess_point_cloud(source, voxel_size, True)
    target_down, target_fpfh = preprocess_point_cloud(target, voxel_size, True)
    result = o3d.pipelines.registration.registration_fgr_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh,
        o3d.pipelines.registration.FastGlobalRegistrationOption(maximum_correspondence_distance=correspondence_distance, iteration_number=iteration)
    )
    return result


def icp_local_registraion(target,source, voxel_size_list,iteration,current_transformation):
    for voxel_size in voxel_size_list:
        source_down = preprocess_point_cloud(source, voxel_size)
        target_down = preprocess_point_cloud(target, voxel_size)
        result = o3d.pipelines.registration.registration_icp(source_down, target_down, voxel_size,
                                                             current_transformation,
                                                             o3d.pipelines.registration.TransformationEstimationPointToPlane(),
                                                             o3d.pipelines.registration.ICPConvergenceCriteria(
                                                                 max_iteration=iteration))
        current_transformation = result.transformation
    return result


def icp_color_local_registraion(target,source, voxel_size_list,iteration, current_transformation):
    for voxel_size in voxel_size_list:
        source_down = preprocess_point_cloud(source, voxel_size)
        target_down = preprocess_point_cloud(target, voxel_size)
        result = o3d.pipelines.registration.registration_colored_icp(source_down, target_down, voxel_size,
                                                                     current_transformation,
                                                                     o3d.pipelines.registration.TransformationEstimationForColoredICP(),
                                                                     o3d.pipelines.registration.ICPConvergenceCriteria(
                                                                         max_iteration=iteration))

        current_transformation = result.transformation
    return result


def pair_registration(source,sourcefpfh,target,targetfpfh,voxel_size,correspondence_distance,iteration):
    result = o3d.pipelines.registration.registration_fgr_based_on_feature_matching(
        source, target, sourcefpfh, targetfpfh,
        o3d.pipelines.registration.FastGlobalRegistrationOption(maximum_correspondence_distance=correspondence_distance,
                                                                iteration_number=iteration)
    )
    transformation = result.transformation
    information = o3d.pipelines.registration.get_information_matrix_from_point_clouds(source, target, voxel_size,
                                                                                      transformation)
    return transformation, information


def full_registration(pcds, voxel_size,correspondence_distance,iteration,edge_threshold,preference_loop,reference_node):
    downpcds=[]
    fpfhs=[]
    for pcd in pcds:
        downpcd,fpfh=preprocess_point_cloud(pcd, voxel_size,True)
        downpcds.append(downpcd)
        fpfhs.append(fpfh)

    pose_graph = o3d.pipelines.registration.PoseGraph()
    odometry = np.identity(4)
    pose_graph.nodes.append(o3d.pipelines.registration.PoseGraphNode(odometry))
    for source_id in range(len(pcds)):
        for target_id in range(source_id + 1, len(pcds)):
            transformation, information = pair_registration(downpcds[source_id],fpfhs[source_id],downpcds[target_id],fpfhs[target_id],voxel_size,correspondence_distance,iteration)
            if target_id == source_id + 1:
                odometry = np.dot(transformation, odometry)
                pose_graph.nodes.append(o3d.pipelines.registration.PoseGraphNode(np.linalg.inv(odometry)))
                pose_graph.edges.append(
                    o3d.pipelines.registration.PoseGraphEdge(source_id, target_id, transformation, information,
                                                             uncertain=False))
            else:
                pose_graph.edges.append(
                    o3d.pipelines.registration.PoseGraphEdge(source_id, target_id, transformation, information,
                                                          uncertain=True))
    o3d.pipelines.registration.global_optimization(pose_graph,
                                                   o3d.pipelines.registration.GlobalOptimizationLevenbergMarquardt(),
                                                   o3d.pipelines.registration.GlobalOptimizationConvergenceCriteria(),
                                                   o3d.pipelines.registration.GlobalOptimizationOption(
                                                       max_correspondence_distance=correspondence_distance, edge_prune_threshold=edge_threshold,preference_loop_closure=preference_loop,
                                                       reference_node=reference_node))
    return pose_graph

def ballpivot(pcd,voxelsize,normalr,normaln,orientk,radii):
 # 下采样

        # 点云下采样
        pcd = pcd.voxel_down_sample(voxelsize)

        # 法向量估计
        pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=normalr, max_nn=normaln))
        pcd.orient_normals_consistent_tangent_plane(orientk)
        print(pcd)
        # ballpivot

        out_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
            pcd, o3d.utility.DoubleVector(radii))
        out_mesh.compute_vertex_normals()
        return out_mesh

def poisson(pcd,voxelsize,normalr,normaln,orientk,depth,width,scale,linear_fit,n_threads):
 # 下采样
        # 点云下采样
        # voxelsize = 0.01
        pcd = pcd.voxel_down_sample(voxelsize)

        # 法向量估计
        pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=normalr, max_nn=normaln))
        pcd.orient_normals_consistent_tangent_plane(orientk)
        print(pcd)
        out_mesh,_=  o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd=pcd, depth=depth,width=width,scale=scale,linear_fit=linear_fit,n_threads=n_threads)
        out_mesh.compute_vertex_normals()
        return out_mesh

def alpha(pcd,voxelsize,normalr,normaln,orientk,alpha):
 # 下采样
        # 点云下采样
        pcd = pcd.voxel_down_sample(voxelsize)

        # 法向量估计
        pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=normalr, max_nn=normaln))
        pcd.orient_normals_consistent_tangent_plane(orientk)
        print(pcd)
        #alpha
        # maxdistance = np.max(pcd.compute_nearest_neighbor_distance())
        out_mesh=o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd,alpha)
        out_mesh.compute_vertex_normals()
        return out_mesh

def densitycluster(pcd,voxelsize):
    # 点云下采样
    pcd = pcd.voxel_down_sample(voxelsize)
    # 点云密度分类降噪
    labels = np.array(pcd.cluster_dbscan(voxelsize * 3, 36))
    print(labels.max())
    g_list = []
    for i in range(-1,labels.max()+1):
        index = np.where(labels == i)[0]
        g_list.append(pcd.select_by_index(index))
    return g_list
def close_holes(mesh,maxholesize,refinehole,refineholeedgelen):
    colors=mesh.vertex_colors
    ms = pymeshlab.MeshSet()
    ms.add_mesh(pymeshlab.Mesh(vertex_matrix=np.array(mesh.vertices), face_matrix=np.array(mesh.triangles),v_normals_matrix=np.array(mesh.vertex_normals), f_normals_matrix=np.array(mesh.triangle_normals)))
    ms.meshing_repair_non_manifold_edges()
    ms.meshing_close_holes(maxholesize=maxholesize, selected=False, newfaceselected=False, selfintersection=True,
                           refinehole=refinehole, refineholeedgelen=pymeshlab.PercentageValue(refineholeedgelen))
    mesh = o3d.geometry.TriangleMesh(o3d.utility.Vector3dVector(ms.current_mesh().vertex_matrix()),
                                      o3d.utility.Vector3iVector(ms.current_mesh().face_matrix()))
    mesh.vertex_normals = o3d.utility.Vector3dVector(ms.current_mesh().vertex_normal_matrix())
    mesh.triangle_normals = o3d.utility.Vector3dVector(ms.current_mesh().face_normal_matrix())
    mesh.vertex_colors=colors

    return mesh
def mashlab_ball_piovt(pcd,voxelsize,normalr,normaln,orientk,clustering,creasethr):
    pcd = pcd.voxel_down_sample(voxelsize)
    # 法向量估计
    if not len(pcd.normals)>0:
        pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=normalr, max_nn=normaln))
        pcd.orient_normals_consistent_tangent_plane(orientk)
    ms = pymeshlab.MeshSet()

    ms.add_mesh(pymeshlab.Mesh(vertex_matrix=np.array(pcd.points),
                               v_normals_matrix=np.array(pcd.normals)))
    ms.generate_surface_reconstruction_ball_pivoting(ballradius=pymeshlab.PercentageValue(0), clustering=clustering,
                                                     creasethr=creasethr, deletefaces=False)
    mesh = o3d.geometry.TriangleMesh(o3d.utility.Vector3dVector(ms.current_mesh().vertex_matrix()),
                                      o3d.utility.Vector3iVector(ms.current_mesh().face_matrix()))
    mesh.vertex_normals = o3d.utility.Vector3dVector(ms.current_mesh().vertex_normal_matrix())
    mesh.triangle_normals = o3d.utility.Vector3dVector(ms.current_mesh().face_normal_matrix())
    mesh.vertex_colors=pcd.colors
    return mesh
# def mashlab_ball_piovt(pcd,normalr,normaln,orientk,clustering,creasethr):
#     # 法向量估计
#     if not len(pcd.normals)>0:
#         pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=normalr, max_nn=normaln))
#         pcd.orient_normals_consistent_tangent_plane(orientk)
#     ms = pymeshlab.MeshSet()
#
#     ms.add_mesh(pymeshlab.Mesh(vertex_matrix=np.array(pcd.points),
#                                v_normals_matrix=np.array(pcd.normals)))
#     ms.generate_surface_reconstruction_ball_pivoting(ballradius=pymeshlab.PercentageValue(0), clustering=clustering,
#                                                      creasethr=creasethr, deletefaces=False)
#     mesh = o3d.geometry.TriangleMesh(o3d.utility.Vector3dVector(ms.current_mesh().vertex_matrix()),
#                                       o3d.utility.Vector3iVector(ms.current_mesh().face_matrix()))
#     mesh.vertex_normals = o3d.utility.Vector3dVector(ms.current_mesh().vertex_normal_matrix())
#     mesh.triangle_normals = o3d.utility.Vector3dVector(ms.current_mesh().face_normal_matrix())
#     mesh.vertex_colors=pcd.colors
#     return mesh
# def mashlab_ball_piovt(pcd,clustering,creasethr):
#     ms = pymeshlab.MeshSet()
#     ms.add_mesh(pymeshlab.Mesh(vertex_matrix=np.array(pcd.points),
#                                v_normals_matrix=np.array(pcd.normals)))
#     ms.generate_surface_reconstruction_ball_pivoting(ballradius=pymeshlab.PercentageValue(0), clustering=clustering,
#                                                      creasethr=creasethr, deletefaces=False)
#     mesh = o3d.geometry.TriangleMesh(o3d.utility.Vector3dVector(ms.current_mesh().vertex_matrix()),
#                                       o3d.utility.Vector3iVector(ms.current_mesh().face_matrix()))
#     mesh.vertex_normals = o3d.utility.Vector3dVector(ms.current_mesh().vertex_normal_matrix())
#     mesh.triangle_normals = o3d.utility.Vector3dVector(ms.current_mesh().face_normal_matrix())
#     mesh.vertex_colors=pcd.colors
#     return mesh
def read_las(path):
    las = laspy.read(path)
    pos = las.xyz - np.array(((las.header.x_min+las.header.x_max)/2, (las.header.y_min+las.header.y_max)/2, las.header.z_min))
    color = np.vstack((las.red / 65535, las.green / 65535, las.blue / 65535)).transpose()
    pcd=o3d.geometry.PointCloud()
    pcd.points=o3d.utility.Vector3dVector(pos)
    pcd.colors = o3d.utility.Vector3dVector(color)
    return pcd
def mashlab_screened_poisson(pcd):
    ms = pymeshlab.MeshSet()
    mesh=pymeshlab.Mesh(vertex_matrix=np.array(pcd.points),
                               v_normals_matrix=np.array(pcd.normals))
    ms.add_mesh(mesh)
    ms.generate_surface_reconstruction_screened_poisson()
    mesh = o3d.geometry.TriangleMesh(o3d.utility.Vector3dVector(ms.current_mesh().vertex_matrix()),
                                      o3d.utility.Vector3iVector(ms.current_mesh().face_matrix()))
    mesh.vertex_normals = o3d.utility.Vector3dVector(ms.current_mesh().vertex_normal_matrix())
    mesh.triangle_normals = o3d.utility.Vector3dVector(ms.current_mesh().face_normal_matrix())
    return mesh
class KeyPressInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):

    def __init__(self,parent=None):
        self.parent = vtk.vtkRenderWindowInteractor()
        if(parent is not None):
            self.parent = parent

        self.AddObserver("KeyPressEvent",self.keyPress)
    def keyPress(self,obj,event):
        key = self.parent.GetKeySym()
        if key == 'Up':
            #下面这一行是关键，实现了actor的更新
            renWin.Render()
class Render(object):
    def __init__(self):
        # [创建一个渲染器]
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(1.0, 1.0, 1.0)                # 设置背景颜色
        # [创建一个渲染窗口]
        self.vtkWidget = QVTKRenderWindowInteractor()
        self.renWin=self.vtkWidget.GetRenderWindow()
        self.renWin.AddRenderer(self.ren)
        self.renWin.SetSize(600, 600)                        # 设置窗口尺寸
        # [创建交互器]
        self.iren =self.vtkWidget.GetRenderWindow().GetInteractor()
        self.iren.SetRenderWindow(self.renWin)                    # 加载渲染窗口
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.iren.SetInteractorStyle(style)
        self.volDataul=[]
        self.textActor = vtk.vtkTextActor()
        self.textActor.GetTextProperty().SetFontFamily(vtk.VTK_FONT_FILE)
        self.textActor.GetTextProperty().SetFontFile("font/simsun.ttc")
        vtk.vtkCommand.ActiveCameraEvent
        self.cameraInfo()
    def cameraInfo(self):
        self.ren.RemoveActor2D(self.textActor)
        self.textActor.SetInput("相机\n"+"位置:"+self.ren.GetActiveCamera().GetPosition().__str__()+"\n"+"范围:"+self.ren.GetActiveCamera().GetClippingRange().__str__())
        self.textActor.SetPosition2(20, 40)
        self.textActor.GetTextProperty().SetColor(0.8, 0.7, 0.0)
        self.textActor.GetTextProperty().SetFontSize(24)
        self.ren.AddActor2D(self.textActor)
        self.renWin.Render()                                 # 渲染
        self.iren.Initialize()                               # 初始化交互器
        self.iren.Start()                                    # show
    def addVolObject(self,file_path):
        data=np.fromfile(file_path,dtype=np.float32)
        data = data.reshape((200,200,80),order='F').copy()
        datanozero=data[data!=0]
        uperbound=datanozero.max()
        lowerbound=datanozero.min()
        alphacolordegree=255
        
        image = vtkImageImportFromArray.vtkImageImportFromArray()
        image.SetArray(data)                           # 加载三维矩阵
        image.SetDataSpacing((25,25,25))
        image.Update()
        # [创建渲染算法]
        volumeMapper =vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputData(image.GetOutput())    # 加载渲染对象（原始提数据）
        # volumeMapper.SetLook
        self.volDataul.append([uperbound,lowerbound])
        # [创建物体颜色函数]
        colorFunc = vtk.vtkColorTransferFunction()      # 创建伪彩转换函数
        # [创建物体不透明度函数]
        opacityFunc = vtk.vtkPiecewiseFunction()        # 创建分段函数
        opacityFunc.AddPoint(0, 0.0005) 
        opacityFunc.AddPoint(lowerbound, 0.005) 
        opacityFunc.AddPoint(uperbound, 0.1) 
        gradientOpacity=vtk.vtkPiecewiseFunction()      # 创建分段函数
        gradientOpacity.AddPoint(0, 0.1)
        gradientOpacity.AddPoint(0.5, 0.5)
        gradientOpacity.AddPoint(1, 1)
        cmap = plt.get_cmap('jet')
        colorFunc.AddRGBPoint(0,cmap(0)[0], cmap(0)[1], cmap(0)[2])   
        for i in range(1,alphacolordegree):
            t=(i/(alphacolordegree-1))
            color=cmap((int)(t*255.0))
            colorFunc.AddRGBPoint(lowerbound+t*(uperbound-lowerbound), color[0],color[1],color[2])   
        

        # [创建物体属性]
        volumeProperty = vtk.vtkVolumeProperty()         
        volumeProperty.SetColor(colorFunc)              # 设置颜色转换
        volumeProperty.SetScalarOpacity(opacityFunc)    # 设置不透明度
        volumeProperty.SetGradientOpacity(gradientOpacity)
        volumeProperty.SetInterpolationTypeToLinear()   # 设置插值方案
        # volumeProperty.ShadeOn()                        # 阴影

        # [创建物体]
        vol = vtk.vtkVolume()    
        vol.SetMapper(volumeMapper)                     # 加载渲染算法
        vol.SetProperty(volumeProperty)                 # 加载物体属性   
        vol.SetPosition(0,0,-1000) 
        vol.GetCenter()
        # [开始绘制] 
        self.ren.AddVolume(vol)                              # 加载物体
        self.ren.ResetCamera()                               # 重置相机
        self.renWin.Render()                                 # 渲染
        self.iren.Initialize()                               # 初始化交互器
        self.iren.Start()                                    # show
        self.cameraInfo()
    
    def addTransMesh(self,file_path):
        filetype=file_path.split('.')[-1]
        print(file_path)
        print(filetype)
        if filetype=='ply':
            reader = vtk.vtkPLYReader()
            reader.SetFileName(file_path)
            reader.Update()
            poly=reader.GetOutput()
        elif filetype=='obj':
            reader = vtk.vtkOBJReader()
            reader.SetFileName(file_path)
            reader.Update()
            poly=reader.GetOutput()
        elif filetype=='stl':
            reader = vtk.vtkSTLReader()
            reader.SetFileName(file_path)
            reader.Update()
            poly=reader.GetOutput()
        elif filetype=='las':
            poly=read_lasvtk(file_path)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(poly)

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.SetScale(100)
        actor.SetPosition(0,0,0)
        actor.SetForceTranslucent(1)
        self.ren.AddActor(actor)
        self.ren.ResetCamera()                               # 重置相机
        self.renWin.Render()                                 # 渲染
        self.iren.Initialize()                               # 初始化交互器
        self.iren.Start()                                    # show
        self.cameraInfo()
    def addairpath(self,coord_position):
        # coord_position=np.random.rand(100,6)
        # coord_position=np.sort(coord_position,axis=0)
        vtk_points = vtk.vtkPoints()
        vtk_points.SetData(numpy_to_vtk(coord_position[:,:3]))
        lines = vtk.vtkCellArray()
        lines.InsertNextCell(coord_position.shape[0])  
        for i in range(coord_position.shape[0]):  # 将点的索引添加到线段中
            lines.InsertCellPoint(i)
        # 创建 vtkPolyData 对象，添加点和线段
        poly_data = vtk.vtkPolyData()
        poly_data.SetPoints(vtk_points)
        poly_data.SetLines(lines)
        # 创建 mapper 和 actor
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(poly_data)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0, 0, 1)
        self.ren.AddActor(actor)
        self.ren.ResetCamera()                               # 重置相机
        self.renWin.Render()                                 # 渲染
        self.iren.Initialize()                               # 初始化交互器
        self.iren.Start()                                    # show
    def addMulVolObject(self,files):
        for file in files:
            data=np.fromfile(file,dtype=np.float32)
            data = data.reshape((200,200,80),order='F').copy()
            datanozero=data[data!=0]
            uperbound=datanozero.max()
            lowerbound=datanozero.min()
            alphacolordegree=255
            
            image = vtkImageImportFromArray.vtkImageImportFromArray()
            image.SetArray(data)                           # 加载三维矩阵
            image.SetDataSpacing((25,25,25))
            image.Update()
            # [创建渲染算法]
            volumeMapper =vtk.vtkGPUVolumeRayCastMapper()
            volumeMapper.SetInputData(image.GetOutput())    # 加载渲染对象（原始提数据）
            # volumeMapper.SetLook
            self.volDataul.append([uperbound,lowerbound])
            # [创建物体颜色函数]
            colorFunc = vtk.vtkColorTransferFunction()      # 创建伪彩转换函数
            # [创建物体不透明度函数]
            opacityFunc = vtk.vtkPiecewiseFunction()        # 创建分段函数
            opacityFunc.AddPoint(0, 0.0005) 
            opacityFunc.AddPoint(lowerbound, 0.005) 
            opacityFunc.AddPoint(uperbound, 0.1) 
            gradientOpacity=vtk.vtkPiecewiseFunction()      # 创建分段函数
            gradientOpacity.AddPoint(0, 0.1)
            gradientOpacity.AddPoint(0.5, 0.5)
            gradientOpacity.AddPoint(1, 1)
            cmap = plt.get_cmap('jet')
            colorFunc.AddRGBPoint(0,cmap(0)[0], cmap(0)[1], cmap(0)[2])   
            for i in range(1,alphacolordegree):
                t=(i/(alphacolordegree-1))
                color=cmap((int)(t*255.0))
                colorFunc.AddRGBPoint(lowerbound+t*(uperbound-lowerbound), color[0],color[1],color[2])   

            # [创建物体属性]
            volumeProperty = vtk.vtkVolumeProperty()         
            volumeProperty.SetColor(colorFunc)              # 设置颜色转换
            volumeProperty.SetScalarOpacity(opacityFunc)    # 设置不透明度
            volumeProperty.SetGradientOpacity(gradientOpacity)
            volumeProperty.SetInterpolationTypeToLinear()   # 设置插值方案
            # volumeProperty.ShadeOn()                        # 阴影

            # [创建物体]
            vol = vtk.vtkVolume()    
            vol.SetMapper(volumeMapper)                     # 加载渲染算法
            vol.SetProperty(volumeProperty)                 # 加载物体属性   
            vol.SetPosition(0,0,-1000) 
            vol.GetCenter()
            # [开始绘制] 
            self.ren.AddVolume(vol)                              # 加载物体
            self.ren.ResetCamera()                               # 重置相机
            self.renWin.Render()                                 # 渲染
            self.iren.Initialize()                               # 初始化交互器
            self.iren.Start()                                    # show
            self.cameraInfo()

    # def __del__(self):
    #     del self.vtkWidget
    #     del self.iren
    #     del self.ren
    #     del self.renWin

def read_lasvtk(filename):
    """Reads a LAS lidar point cloud to vtkPolyData"""
    las = laspy.read(filename)
    pos = las.xyz - np.array(((las.header.x_min+las.header.x_max)/2, (las.header.y_min+las.header.y_max)/2, las.header.z_min))
    color = np.vstack((las.red/ 257, las.green/ 257, las.blue/ 257)).transpose()
    color=color.astype(np.uint8)
    points=vtk.vtkPoints()
    points.SetData(numpy_to_vtk(pos))
    vertices=vtk.vtkCellArray()
    for i in range(pos.shape[0]):
        vertices.InsertNextCell(1,[i])
        # vertices.InsertCellPoint(i)
    # vertices.SetData(numpy_to_vtkIdTypeArray(np.arange(pos.shape[0],dtype=np.int64)),numpy_to_vtk(np.arange(pos.shape[0],dtype=np.int64)))
    print(vertices)
    poly = vtk.vtkPolyData()
    poly.SetPoints(points)
    poly.SetVerts(vertices)
    poly.GetPointData().SetScalars(numpy_to_vtk(color))
    return poly

def read_coordposition_from_txt(file_path):
    with open(file_path, "r") as file:
        json_data = json.load(file)
    coord_position=np.zeros([len(json_data["info"]["frameTimeStates"]),6],dtype=float)
    for i,frame_state in enumerate(json_data["info"]["frameTimeStates"]):
        coord_position[i,:3]=[frame_state["flightControllerState"]["aircraftLocation"]["latitude"],frame_state["flightControllerState"]["aircraftLocation"]["longitude"],frame_state["flightControllerState"]["altitude"]]
        coord_position[i,3:]=[frame_state["flightControllerState"]["aircraftLocation"]["latitude"],frame_state["flightControllerState"]["aircraftLocation"]["longitude"],frame_state["flightControllerState"]["altitude"]]
    return coord_position
def plot_coordposition(coord_position):
    path=o3d.geometry.LineSet()
    path.points=o3d.utility.Vector3dVector(coord_position[:,:3])
    lines=np.array([np.arange(0,99),np.arange(1,100)]).transpose()
    path.lines=o3d.utility.Vector2iVector(lines)
    # path.rotate=o3d.geometry.get_rotation_matrix_from_xyz(coord_position[:,3:])
    return path

def plot_airplane(coord_position,idx):
    airplane = o3d.geometry.TriangleMesh.create_cone(radius=0.01, height=0.02)
    airplane.compute_vertex_normals()
    airplane.paint_uniform_color([1, 0.3, 0.2])  # 红色
    airplane.translate(coord_position[idx,:3])  # 将尾翼移动到机身的末端
    airplane.rotate(o3d.geometry.get_rotation_matrix_from_xyz(coord_position[idx,3:]))
    return airplane


