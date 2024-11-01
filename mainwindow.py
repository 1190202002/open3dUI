import open3d as o3d
import os
from scipy.spatial import KDTree
from PySide6.QtWidgets import QApplication,QMainWindow, QFileDialog,QWidget
from PySide6.QtGui import QWindow
from PySide6.QtCore import  Slot,Qt,QTimer,QTranslator
import convlas2mesh as convlas
from ui_mainwindow import Ui_MainWindow
from BallpiovtDialog import BallConfig
from FastregDialog import FastregDialog
from AlphaDialog import AlphaDialog
from ColorregDialog import ColorregDialog
from ICPregDialog import ICPregDialog
from MulregDialog import MulregDialog
from PossionDialog import PossionDialog
from DensityclusterDialog import DensityclusterDialog
from Taubin import Taubin
from Laplacian import Laplacian
from Average import Average
from normal import normal
from downsample import downsample
from removeradiusoutlinerDialog import removeradiusoutlinerDialog
from removestaticoutlinerDialog import removestaticoutlinerDialog
from samplepoissonDialog import SamplepoissonDialog
from sampleuniformlyDialog import SampleuniformlyDialog
from closeholesDialog import closeholesDialog
from ballautoguess import BallautoGuess
from ConvDialog import Conv_Dialog
import win32gui
import sys
import numpy as np
import utility
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtkmodules.all as vtk
from vtkmodules.util import vtkImageImportFromArray,vtkImageExportToArray
from vtkmodules.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray,vtk_to_numpy
import matplotlib.pyplot as plt
import open3d
class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.trans=QTranslator()
        self.Render=utility.Render()
        self.pcd = o3d.geometry.PointCloud()
        self.pcd_result = o3d.geometry.PointCloud()
        self.mesh=o3d.geometry.TriangleMesh()
        self.pcd_list=[]
        self.mesh_list=[]
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename=""
        self.meandistance=0.01
        self.vis = o3d.visualization.VisualizerWithKeyCallback()
        #将open3d创建的glfw3.0窗体转换为QT窗体
        self.vis.create_window(visible=False)
        self.option=self.vis.get_render_option()
        sub_window = QWindow.fromWinId(win32gui.FindWindow("GLFW30",None))
        self.displayer = QWidget.createWindowContainer(sub_window)
        self.ui.gridLayout.addWidget(self.displayer,0,0)
        self.ui.gridLayout.addWidget(self.Render.vtkWidget,0,0)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_B:
            self.option.mesh_show_back_face=not self.option.mesh_show_back_face

        elif event.key() == Qt.Key.Key_W:
            self.option.mesh_show_wireframe=not self.option.mesh_show_wireframe
        elif event.key() == Qt.Key.Key_C:
            self.option.show_coordinate_frame=not self.option.show_coordinate_frame

        elif event.key() == Qt.Key.Key_N:
            self.option.point_show_normal=not self.option.point_show_normal

        elif event.key() == Qt.Key.Key_L:
            self.option.light_on=not self.option.light_on
        self.vis.update_renderer()
    def closeEvent(self, event):
        self.vis.destroy_window()
        self.Render.vtkWidget.deleteLater()
#文件操作
    def choosefile(self):
        self.showopen3d()
        filename,_= QFileDialog.getOpenFileName(self,"Select file","","File(*.pcd *.las *.obj *.stl *.xyz *.ply)")
        self.filename=filename
        filetype=filename.split('.')[-1]

        if filetype in ['pcd','xyz']:
            self.pcd=o3d.io.read_point_cloud(filename)
        elif filetype in ['obj','stl']:
            self.mesh=o3d.io.read_triangle_mesh(filename)
        elif filetype in ['las']:
            self.pcd=utility.read_las(filename)
        else:
            self.mesh=o3d.io.read_triangle_mesh(filename)
            if len(self.mesh.triangles)==0:
                self.mesh=o3d.geometry.TriangleMesh()
                self.pcd=o3d.io.read_point_cloud(filename)

        if len(self.pcd.points)>0:
            self.pcd.remove_duplicated_points()
            self.meandistance = np.mean(self.pcd.compute_nearest_neighbor_distance())
        self.vis.clear_geometries()
        self.vis.add_geometry(self.pcd)
        self.vis.add_geometry(self.mesh)
        self.vis.run()

    def addfile(self):
        self.showopen3d()
        filename, _ = QFileDialog.getOpenFileName(self, "Select file", "", "All Files (*)")
        filetype = filename.split('.')[-1]
        if filetype in ['pcd', 'xyz']:
            self.pcd = o3d.io.read_point_cloud(filename)
        elif filetype in ['obj', 'stl']:
            self.mesh = o3d.io.read_triangle_mesh(filename)
        elif filetype in ['las']:
            self.pcd=utility.read_las(filename)
        else:
            self.mesh = o3d.io.read_triangle_mesh(filename)
            if len(self.mesh.triangles) == 0:
                self.mesh = o3d.geometry.TriangleMesh()
                self.pcd = o3d.io.read_point_cloud(filename)

        if len(self.pcd.points)>0:
            self.pcd.remove_duplicated_points()
            self.meandistance = np.mean(self.pcd.compute_nearest_neighbor_distance())

        self.pcd_list.append(self.pcd)
        self.vis.add_geometry(self.pcd)
        self.vis.run()
    def savefile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Pcd Files (*.pcd);;Ply Files (*.ply);;Obj Files (*.obj);;Xyz Files (*.xyz);;Stl Files (*.stl)")
        filetype = fileName.split('.')[-1]
        if filetype in ['pcd', 'xyz']:
            o3d.io.write_point_cloud(fileName, self.pcd)
        elif filetype in ['obj', 'stl']:
            o3d.io.write_triangle_mesh(fileName, self.mesh)
        else:
           if len(self.mesh.triangles)>0:
               o3d.io.write_triangle_mesh(fileName, self.mesh)
           else:
               o3d.io.write_point_cloud(fileName, self.pcd)
    def clearfile(self):
        self.pcd = o3d.geometry.PointCloud()
        self.pcd_result = o3d.geometry.PointCloud()
        self.mesh = o3d.geometry.TriangleMesh()
        self.pcd_list = []
        self.mesh_list = []
        self.vis.clear_geometries()
#重建
    def Configball(self):
        self.dialog=BallConfig()
        self.dialog.ui.voxel.setValue(5*self.meandistance)
        self.dialog.sign.connect(self.ballpiovt)
        self.dialog.exec()
    @Slot(list)
    def ballpiovt(self,config):
        # 下采样
        # 点云下采样
        self.dialog.close()
        self.mesh=utility.ballpivot(self.pcd, config[0], config[1], config[2], config[3], config[4])
        print(self.mesh)
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configAlpha(self):
        self.dialog=AlphaDialog()
        self.dialog.ui.voxel.setValue(5 * self.meandistance)
        self.dialog.sign.connect(self.alpha)
        self.dialog.exec()
    @Slot(float)
    def alpha(self,config):
        self.dialog.close()
        self.mesh = utility.alpha(self.pcd, config[0], config[1], config[2], config[3], config[4])
        print(self.mesh)
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configPossion(self):
        self.dialog=PossionDialog()
        self.dialog.ui.voxel.setValue(5 * self.meandistance)
        self.dialog.sign.connect(self.possion)
        self.dialog.exec()
    @Slot(list)
    def possion(self,config):
        self.dialog.close()
        self.mesh= utility.poisson(self.pcd,config[0], config[1], config[2], config[3], config[4],config[5],config[6],config[7],config[8])
        print(self.mesh)
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configFastreg(self):
        self.dialog=FastregDialog()
        self.dialog.ui.voxel.setValue(self.meandistance)
        self.dialog.sign.connect(self.fastreg)
        self.dialog.exec()
#配准
    @Slot(list)
    def fastreg(self,config):
        self.dialog.close()
        result=utility.fast_global_registration(target=self.pcd_list[0],source=self.pcd_list[1],voxel_size=config[0],correspondence_distance=config[1],iteration=config[2])
        self.pcd_list[1].transform(result.transformation)
        self.vis.update_geometry(self.pcd_list[1])

    def configColorreg(self):
        self.dialog=ColorregDialog()
        self.dialog.ui.voxel.setValue(self.meandistance)
        self.dialog.sign.connect(self.colorreg)
        self.dialog.exec()
    @Slot(list)
    def colorreg(self,config):
        self.dialog.close()
        result=utility.icp_color_local_registraion(self.pcd_list[0],self.pcd_list[1],[config[0]],config[1],np.identity(4))
        self.pcd_list[1].transform(result.transformation)
        self.vis.update_geometry(self.pcd_list[1])
    def configICPreg(self):
        self.dialog=ICPregDialog()
        self.dialog.ui.voxel.setValue(self.meandistance)
        self.dialog.sign.connect(self.icpreg)
        self.dialog.exec()
    @Slot(list)
    def icpreg(self,config):
        self.dialog.close()
        result = utility.icp_local_registraion(self.pcd_list[0],self.pcd_list[1],[config[0]],config[1],np.identity(4))
        self.pcd_list[1].transform(result.transformation)
        self.vis.update_geometry(self.pcd_list[1])

    def configMulreg(self):
        self.dialog=MulregDialog()
        self.dialog.ui.voxel.setValue(self.meandistance)
        self.dialog.sign.connect(self.mulreg)
        self.dialog.exec()
    @Slot(list)
    def mulreg(self,config):
        self.dialog.close()
        pose_graph=utility.full_registration(pcds=self.pcd_list,voxel_size=config[0],correspondence_distance=config[1],iteration=config[2],edge_threshold=config[3],preference_loop=config[4],reference_node=config[5])

        for point_id in range(len(self.pcd_list)):
            self.pcd_list[point_id].transform(pose_graph.nodes[point_id].pose)
            self.vis.update_geometry(self.pcd_list[point_id])

    def configDensitycluster(self):
        self.dialog=DensityclusterDialog()
        self.dialog.sign.connect(self.densitycluster)
        self.dialog.exec()
    @Slot(float)
    def densitycluster(self,voxelsize):
        self.dialog.close()
        self.pcd_list=utility.densitycluster(self.pcd,voxelsize)
        self.vis.clear_geometries()
        n=len(self.pcd_list)
        colors_list=[]
        color=np.linspace(0, 1, n)
        for i in range(n):
            colors_list.append([color[i],1-color[i],color[i]])
        for point_id in range(n):
             self.pcd_list[point_id].paint_uniform_color(colors_list[point_id])
             self.vis.add_geometry(self.pcd_list[point_id])
        self.vis.run()
    def configTaubin(self):
        self.dialog=Taubin()
        self.dialog.sign.connect(self.taubin)
        self.dialog.exec()
    def taubin(self,config):
        self.dialog.close()
        self.mesh.filter_smooth_taubin(config[0],config[1],config[2])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configLaplacian(self):
        self.dialog=Laplacian()
        self.dialog.sign.connect(self.laplacian)
        self.dialog.exec()
    def laplacian(self,config):
        self.dialog.close()
        self.mesh.filter_smooth_laplacian(config[0],config[1])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configAverage(self):
        self.dialog=Average()
        self.dialog.sign.connect(self.average)
        self.dialog.exec()
    def average(self,config):
        self.dialog.close()
        self.mesh.filter_smooth_simple(config[0])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configNormal(self):
        self.dialog=normal()
        self.dialog.ui.normalr.setValue(1.4 *5*self.meandistance)
        self.dialog.sign.connect(self.esmitnormal)
        self.dialog.exec()
    @Slot(list)
    def esmitnormal(self,config):
        self.dialog.close()
        self.pcd.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(config[0],config[1]))
        self.pcd.orient_normals_consistent_tangent_plane(config[2])
    def configDownsample(self):
        self.dialog=downsample()
        self.dialog.ui.voxel.setValue(5*self.meandistance)
        self.dialog.sign.connect(self.downsample)
        self.dialog.exec()
    @Slot(float)
    def downsample(self,config):
        self.dialog.close()
        self.pcd=self.pcd.voxel_down_sample(config)
        self.vis.clear_geometries()
        self.vis.add_geometry(self.pcd)
        self.vis.run()
    def mergepoint(self):
        self.pcd=self.pcd_list[0]
        for i in range(1,len(self.pcd_list)):
            self.pcd=self.pcd+self.pcd_list[i]
    def configradius_outliers(self):
        self.dialog = removeradiusoutlinerDialog()
        self.dialog.sign.connect(self.remove_radius_outliers)
        self.dialog.exec()
    @Slot(list)
    def remove_radius_outliers(self,config):
        self.dialog.close()
        self.pcd = self.pcd.remove_statistical_outlier(config[0], config[1])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.pcd)
        self.vis.run()

    def configstatistical_outliers(self):
        self.dialog = removestaticoutlinerDialog()
        self.dialog.sign.connect(self.remove_statistical_outliers)
        self.dialog.exec()
    @Slot(list)
    def remove_statistical_outliers(self,config):
        self.dialog.close()
        self.pcd=self.pcd.remove_statistical_outlier(config[0],config[1])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.pcd)
        self.vis.run()
    def configpoisson_disk(self):
        self.dialog = SamplepoissonDialog()
        self.dialog.sign.connect(self.poisson_disk)
        self.dialog.exec()
    @Slot(list)
    def poisson_disk(self,config):
        self.dialog.close()
        self.pcd=self.mesh.sample_points_poisson_disk(number_of_points=config[0],init_factor=config[1],use_triangle_normal=config[2])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.pcd)
        self.vis.run()
    def configuniformly(self):
        self.dialog = SampleuniformlyDialog()
        self.dialog.sign.connect(self.uniformly)
        self.dialog.exec()
    @Slot(list)
    def uniformly(self,config):
        self.dialog.close()
        self.pcd = self.mesh.sample_points_uniformly(number_of_points=config[0],use_triangle_normal=config[1])
    def configcloseholes(self):
        self.dialog =closeholesDialog()
        self.dialog.sign.connect(self.closeholes)
        self.dialog.exec()
    @Slot(list)
    def closeholes(self,config):
        self.dialog.close()
        self.mesh=utility.close_holes(self.mesh,config[0],config[1],config[2])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configballautoguess(self):
        self.dialog =BallautoGuess()
        self.dialog.ui.voxel.setValue(5 * self.meandistance)
        self.dialog.sign.connect(self.ballautoguess)
        self.dialog.exec()
    @Slot(list)
    def ballautoguess(self,config):
        self.dialog.close()
        self.mesh=utility.mashlab_ball_piovt(self.pcd,config[0],config[1],config[2],config[3],config[4],config[5])
        self.vis.clear_geometries()
        self.vis.add_geometry(self.mesh)
        self.vis.run()
    def configconvmesh(self):
        self.dialog=Conv_Dialog()
        self.dialog.sign.connect(self.las_convonet)
        self.dialog.exec()
    @Slot(dict)
    def las_convonet(self,config):
        self.dialog.close()
        out_folder='convolutional_occupancy_networks/data/demo/build'
        if self.filename.split('.')[-1] in ['las']:
            print(config[0])
            print(config[1])
            print(config[2])
            print(config[3])
            points, colors,scale= convlas.make_temp_dataset(self.filename, out_folder)
            os.system(f"cd convolutional_occupancy_networks && python generate.py data/demo/build/a.yaml {config[0]} --unitsize {config[1]} --queryvolsize {config[2]} --resolution {config[3]}")
            meshdir = 'convolutional_occupancy_networks/out/build/generation/meshes'
            meshpath = os.path.join(meshdir, '1.off')
            mesh = convlas.readmesh(meshpath)
            ##paint
            p_kdtree = KDTree(points)
            _, index = p_kdtree.query(np.array(mesh.vertices), 1)
            mesh.vertex_colors = o3d.utility.Vector3dVector(colors[index])
            mesh.scale(scale,mesh.get_center())
            self.mesh=mesh
            self.vis.clear_geometries()
            self.vis.add_geometry(self.mesh)
            self.vis.run()
        elif self.filename.split('.')[-1] in ['pcd','ply']:
            os.makedirs(out_folder, exist_ok=True)
            pcd=o3d.io.read_point_cloud(self.filename)
            scale=pcd.get_max_bound().max()
            pcd.scale(1/scale, pcd.get_center())
            pcd.translate(-pcd.get_center())
            points=o3d.utility.Vector3dVector(pcd.points)
            try:
                n=pcd.normals
            except:
                n = np.ones_like(points)
                n = n / (np.linalg.norm(n, axis=1).reshape([-1, 1]) + 1e-6)
            normals = n
            buildname = '1'
            npzpath = os.path.join(out_folder, buildname)
            os.makedirs(npzpath, exist_ok=True)
            npz_dict = dict(points=points,
                            normals=normals)
            np.savez(os.path.join(npzpath, 'pointcloud.npz'), **npz_dict)
            os.system('cd convolutional_occupancy_networks && python generate.py data/demo/build/a.yaml')
            meshdir = 'convolutional_occupancy_networks/out/build/generation/meshes'
            meshpath = os.path.join(meshdir, '1.off')
            mesh = convlas.readmesh(meshpath)
            try:
                colors=np.array(pcd.colors)
            except:
                colors=np.array([0,0,0])
            ##paint
            if colors.shape[0]>1:
                p_kdtree = KDTree(points)
                _, index = p_kdtree.query(np.array(mesh.vertices), 1)
                mesh.vertex_colors = o3d.utility.Vector3dVector(colors[index])
            mesh.scale(scale, mesh.get_center())
            self.mesh = mesh
            self.vis.clear_geometries()
            self.vis.add_geometry(self.mesh)
            self.vis.run()
    def addvolumefile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select file", "", "dat Files (*.dat)")
        filetype = filename.split('.')[-1]
        if filetype=='dat':
            self.showvtk()
            self.Render.addVolObject(filename)   
    def VolumeAddmodelfile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select file", "", "All Files (*)")
        filetype = filename.split('.')[-1]
        if filetype in ['ply', 'obj', 'stl','las']:
            self.showvtk()
            self.Render.addTransMesh(filename)
    def showopen3d(self):
        self.Render.vtkWidget.setDisabled(True)
        self.displayer.setDisabled(False)
        self.Render.vtkWidget.setVisible(False)
        self.displayer.setVisible(True)
    def showvtk(self):
        self.Render.vtkWidget.setVisible(True)
        self.Render.vtkWidget.setDisabled(False)
        self.displayer.setDisabled(True)
        self.displayer.setVisible(False)
    def MulVolumefile(self):
        options=QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(self, "Select file", "", "All Files (*)")
        self.showvtk()
        self.Render.addMulVolObject(filenames)
    def viewup(self):
        # self.Render.ren.ResetCamera()
        camra=self.Render.ren.GetActiveCamera()
        self.Render.ren.GetActiveCamera().SetPosition(camra.GetFocalPoint()[0],camra.GetFocalPoint()[1]+camra.GetDistance(),camra.GetFocalPoint()[2])
        self.Render.ren.GetActiveCamera().SetViewUp(0,0,-1)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def viewfront(self):
        # self.Render.ren.ResetCamera()
        camra=self.Render.ren.GetActiveCamera()
        self.Render.ren.GetActiveCamera().SetPosition(camra.GetFocalPoint()[0],camra.GetFocalPoint()[1],camra.GetFocalPoint()[2]+camra.GetDistance())
        self.Render.ren.GetActiveCamera().SetViewUp(0,1,0)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def viewleft(self):
        # self.Render.ren.ResetCamera()
        camra=self.Render.ren.GetActiveCamera()
        self.Render.ren.GetActiveCamera().SetPosition(camra.GetFocalPoint()[0]-camra.GetDistance(),camra.GetFocalPoint()[1],camra.GetFocalPoint()[2])
        self.Render.ren.GetActiveCamera().SetViewUp(0,1,0)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def viewdown(self):
        camra=self.Render.ren.GetActiveCamera()
        self.Render.ren.GetActiveCamera().SetPosition(camra.GetFocalPoint()[0],camra.GetFocalPoint()[1]-camra.GetDistance(),camra.GetFocalPoint()[2])
        self.Render.ren.GetActiveCamera().SetViewUp(0,0,-1)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def viewright(self):
        camra=self.Render.ren.GetActiveCamera()
        self.Render.ren.GetActiveCamera().SetPosition(camra.GetFocalPoint()[0]+camra.GetDistance(),camra.GetFocalPoint()[1],camra.GetFocalPoint()[2])
        self.Render.ren.GetActiveCamera().SetViewUp(0,1,0)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def viewback(self):
        camra=self.Render.ren.GetActiveCamera()
        print(camra)
        self.Render.ren.GetActiveCamera().SetPosition(camra.GetFocalPoint()[0],camra.GetFocalPoint()[1],camra.GetFocalPoint()[2]-camra.GetDistance())
        self.Render.ren.GetActiveCamera().SetViewUp(0,1,0)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    
    # def cameramove(self,value):
    #     camra=self.Render.ren.GetActiveCamera()
    #     print(camra.GetClippingRange())
    #     if value>=0:
    #         camra.SetClippingRange(camra.GetClippingRange()[0]+value,camra.GetClippingRange()[1]) 
    #     else:
    #         camra.SetClippingRange(camra.GetClippingRange()[0]-value,camra.GetClippingRange()[1])
    #     self.Render.renWin.Render()
    def clipforward(self):
        camra=self.Render.ren.GetActiveCamera()
        print(camra.GetClippingRange())
        camra.SetClippingRange(camra.GetClippingRange()[0]+1,camra.GetClippingRange()[1]) 
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def clipbackoff(self):
        camra=self.Render.ren.GetActiveCamera()
        print(camra.GetClippingRange())
        camra.SetClippingRange(camra.GetClippingRange()[0]-1,camra.GetClippingRange()[1]) 
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def clipfastforward(self):
        camra=self.Render.ren.GetActiveCamera()
        print(camra.GetClippingRange())
        camra.SetClippingRange(camra.GetClippingRange()[0]+100,camra.GetClippingRange()[1]) 
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def clipfastbackoff(self):
        camra=self.Render.ren.GetActiveCamera()
        print(camra.GetClippingRange())
        camra.SetClippingRange(camra.GetClippingRange()[0]-100,camra.GetClippingRange()[1]) 
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def clipreset(self):
        self.Render.ren.ResetCamera()
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def cameramovefront(self):
        camra=self.Render.ren.GetActiveCamera()
        scale=100
        camra.SetPosition(camra.GetPosition()[0]-camra.GetViewPlaneNormal()[0]*scale,camra.GetPosition()[1]-camra.GetViewPlaneNormal()[1]*scale,camra.GetPosition()[2]-camra.GetViewPlaneNormal()[2]*scale)
        camra.SetFocalPoint(camra.GetFocalPoint()[0]-camra.GetViewPlaneNormal()[0]*scale,camra.GetFocalPoint()[1]-camra.GetViewPlaneNormal()[1]*scale,camra.GetFocalPoint()[2]-camra.GetViewPlaneNormal()[2]*scale)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
    def cameramoveback(self):
        camra=self.Render.ren.GetActiveCamera()
        scale=100
        camra.SetPosition(camra.GetPosition()[0]+camra.GetViewPlaneNormal()[0]*scale,camra.GetPosition()[1]+camra.GetViewPlaneNormal()[1]*scale,camra.GetPosition()[2]+camra.GetViewPlaneNormal()[2]*scale)
        camra.SetFocalPoint(camra.GetFocalPoint()[0]+camra.GetViewPlaneNormal()[0]*scale,camra.GetFocalPoint()[1]+camra.GetViewPlaneNormal()[1]*scale,camra.GetFocalPoint()[2]+camra.GetViewPlaneNormal()[2]*scale)
        self.Render.cameraInfo()
        self.Render.renWin.Render()
        
    def changeAlpha(self,value):
        actors=self.Render.ren.GetVolumes()
        actors.InitTraversal()
        opacityFunc = vtk.vtkPiecewiseFunction()        # 创建分段函数
        opacityFunc.AddPoint(0, self.ui.doubleSpinBoxZeroAlpha.value()) 
        idx=0
        actor=actors.GetNextItem()
        while actor is not None:
            [uperbound,lowerbound]=self.Render.volDataul[idx] 
            opacityFunc.AddPoint(lowerbound, self.ui.doubleSpinBoxLowalpha.value())
            opacityFunc.AddPoint(uperbound, self.ui.doubleSpinBoxHighAlpha.value())
            actor.GetProperty().SetScalarOpacity(opacityFunc)
            actor=actors.GetNextItem()
            idx+=1
        self.Render.renWin.Render()
    def changegradientAlpha(self,value):
        gradientOpacity=vtk.vtkPiecewiseFunction()
        gradientOpacity.AddPoint(0, self.ui.doubleSpinBox0_gradientAlpha.value())
        gradientOpacity.AddPoint(0.5, self.ui.doubleSpinBox05_gradientAlpha.value())
        gradientOpacity.AddPoint(1, self.ui.doubleSpinBox1_gradientAlpha.value())
        actors=self.Render.ren.GetVolumes()
        actors.InitTraversal()
        actor=actors.GetNextItem()
        while actor is not None:
            actor.GetProperty().SetGradientOpacity(gradientOpacity)
            actor=actors.GetNextItem()
        self.Render.renWin.Render()
    def changeColorBar(self,colorbar):
        actors=self.Render.ren.GetVolumes()
        actors.InitTraversal()
        if self.ui.radioButtonColorReverse.isChecked():
            cmap = plt.get_cmap(colorbar+'_r')
        else:
            cmap = plt.get_cmap(colorbar)
        colorFunc = vtk.vtkColorTransferFunction()      # 创建伪彩转换函数
        colorFunc.AddRGBPoint(0,cmap(0)[0], cmap(0)[1], cmap(0)[2])     
        actor=actors.GetNextItem()
        idx=0
        while actor is not None:
            [uperbound,lowerbound]=self.Render.volDataul[idx] 
            for i in range(1,255):
                t=(i/(255-1))
                color=cmap((int)(t*255.0))
                colorFunc.AddRGBPoint(lowerbound+t*(uperbound-lowerbound), color[0],color[1],color[2])
            actor.GetProperty().SetColor(colorFunc)
            actor=actors.GetNextItem()
            idx+=1
        self.Render.renWin.Render()
    def ColorReverse(self):
        actors=self.Render.ren.GetVolumes()
        actors.InitTraversal()
        if self.ui.radioButtonColorReverse.isChecked():
            cmap = plt.get_cmap(self.ui.comboBox.currentText()+'_r')
        else:
            cmap = plt.get_cmap(self.ui.comboBox.currentText())
        colorFunc = vtk.vtkColorTransferFunction()      # 创建伪彩转换函数
        colorFunc.AddRGBPoint(0,cmap(0)[0], cmap(0)[1], cmap(0)[2])     
        actor=actors.GetNextItem()
        idx=0
        while actor is not None:
            [uperbound,lowerbound]=self.Render.volDataul[idx] 
            for i in range(1,255):
                t=(i/(255-1))
                color=cmap((int)(t*255.0))
                colorFunc.AddRGBPoint(lowerbound+t*(uperbound-lowerbound), color[0],color[1],color[2])
            actor.GetProperty().SetColor(colorFunc)
            actor=actors.GetNextItem()
            idx+=1
        self.Render.renWin.Render()
    def AnimationStart(self):
        def animationfunction():
            actors=self.Render.ren.GetVolumes()
            actors.InitTraversal()
            initflag=True
            actor=actors.GetNextItem()
            while actor is not None:
                if not actor.GetVisibility():
                    initflag=False
                    break
                actor=actors.GetNextItem()
            if initflag:
                actors.InitTraversal()
                actor=actors.GetNextItem()
                actor=actors.GetNextItem()
                while actor is not None:
                    actor.SetVisibility(False)
                    actor=actors.GetNextItem()
            else:
                actors.InitTraversal()
                actor=actors.GetNextItem()
                while actor is not None:
                    if actor.GetVisibility():
                        actor.SetVisibility(False)
                        actor=actors.GetNextItem()
                        if actor is None:
                            actors.InitTraversal()
                            actor=actors.GetNextItem()
                            actor.SetVisibility(True)
                        else:
                            actor.SetVisibility(True)
                        actor=actors.GetNextItem()
                        while actor is not None:
                            actor.SetVisibility(False)
                            actor=actors.GetNextItem()
                    actor=actors.GetNextItem()
            self.Render.renWin.Render()
        self.timer = QTimer(self)
        self.timer.timeout.connect(animationfunction)
        self.timer.start(self.ui.doubleSpinBoxAnimationTime.value()*1000)
    def AnimationEnd(self):
        self.timer.stop()
        actors=self.Render.ren.GetVolumes()
        actors.InitTraversal()
        actor=actors.GetNextItem()
        while actor is not None:
            actor.SetVisibility(True)
            actor=actors.GetNextItem()
        self.Render.renWin.Render()
    def AnimationStop(self):
        self.timer.stop()
    def vtkClearmodel(self):
        actors=self.Render.ren.GetActors()
        num = actors.GetNumberOfItems()
        actors.InitTraversal()
        for i in range(num):
            actor = actors.GetNextActor()
            self.Render.ren.RemoveActor(actor)
        self.Render.ren.ResetCamera()
        self.Render.renWin.Render()
    def vtkClearvolume(self):
        volumes=self.Render.ren.GetVolumes()
        num = volumes.GetNumberOfItems()
        volumes.InitTraversal()
        for i in range(num):
            volume = volumes.GetNextItem()
            self.Render.ren.RemoveActor(volume)
        self.Render.ren.ResetCamera()
        self.Render.renWin.Render()
    def pathShow(self):
        coord_position=np.random.rand(100,6)
        self.coord_position=np.sort(coord_position,axis=0)
        # self.path=utility.plot_coordposition(self.coord_position)
        # # self.showopen3d()
        # self.vis.add_geometry(self.path)
        # self.vis.run()
        self.showvtk()
        self.Render.addairpath(self.coord_position)
    def pathCancel(self):
        pass
    def showCoord(self):
        airplane=utility.plot_airplane(self.coord_position,self.ui.airpathid.value())
        self.ui.coordlabel.setText("x:{:10.4f},y:{:10.4f},z:{:10.4f}".format(self.coord_position[self.ui.airpathid.value(),0],self.coord_position[self.ui.airpathid.value(),1],self.coord_position[self.ui.airpathid.value(),2]))
        self.ui.positionlable.setText("x:{:10.4f},y:{:10.4f},z:{:10.4f}".format(self.coord_position[self.ui.airpathid.value(),3],self.coord_position[self.ui.airpathid.value(),4],self.coord_position[self.ui.airpathid.value(),5]))
        self.vis.add_geometry(airplane)
        self.vis.run()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindows()
    window.showMaximized()
    window.show()
    sys.exit(app.exec())

    