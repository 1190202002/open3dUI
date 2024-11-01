import laspy
import numpy as np
import open3d as o3d
from scipy.spatial import Delaunay, ConvexHull

from sklearn.cluster import HDBSCAN
import matplotlib.cm as cm
# import  utility
colormap=cm.get_cmap('tab20')
#读取点云，分类
las=laspy.read('colorpointcloud.las')
all=np.concatenate((las.xyz-np.array((las.header.x_min,las.header.y_min,las.header.z_min)),np.vstack((las.red/65535,las.green/65535,las.blue/65535)).transpose()),axis=1)
# unclass=all[las.classification==1]
# lowtree=all[las.classification==3]
ground=all[las.classification==2]
midtree=all[las.classification==4]
hightree=all[las.classification==5]
build=all[las.classification==6]
#转换为带颜色点

# pbuild=o3d.geometry.PointCloud()
# pmidtree=o3d.geometry.PointCloud()
# phightree=o3d.geometry.PointCloud()
# punclass=o3d.geometry.PointCloud()

# pbuild.points=o3d.utility.Vector3dVector(build[:,:3])
# pbuild.colors=o3d.utility.Vector3dVector(build[:,3:])
# pmidtree.points=o3d.utility.Vector3dVector(midtree[:,:3])
# pmidtree.colors=o3d.utility.Vector3dVector(midtree[:,3:])
# phightree.points=o3d.utility.Vector3dVector(hightree[:,:3])
# phightree.colors=o3d.utility.Vector3dVector(hightree[:,3:])
# punclass.points=o3d.utility.Vector3dVector(unclass[:,:3])
# punclass.colors=o3d.utility.Vector3dVector(unclass[:,3:])
# pground+=punclass


#地面网格 Delaunay三角剖分
mground=o3d.geometry.TriangleMesh()
print(ground.shape[0])
mground.vertices=o3d.utility.Vector3dVector(ground[:,:3])
mground.vertex_colors=o3d.utility.Vector3dVector(ground[:,3:])
mground.vertex_normals=o3d.utility.Vector3dVector(np.array([[0,0,1]]).repeat(ground.shape[0],axis=0))
mground.triangles=o3d.utility.Vector3iVector(Delaunay(ground[:,:2]).simplices)
o3d.visualization.draw_geometries([mground])
# #地面网格
# pground=o3d.geometry.PointCloud()
# pground.points=o3d.utility.Vector3dVector(ground[:,:3])
# pground.colors=o3d.utility.Vector3dVector(ground[:,3:])
# pground.normals=o3d.utility.Vector3dVector(np.array([[0,0,1]]).repeat(ground.shape[0],axis=0))
# mground=utility.mashlab_ball_piovt(pground,20,90)
# o3d.visualization.draw_geometries([mground])
#地面网格
# pground=o3d.geometry.PointCloud()
# pground.points=o3d.utility.Vector3dVector(ground[:,:3])
# pground.colors=o3d.utility.Vector3dVector(ground[:,3:])
# pground.normals=o3d.utility.Vector3dVector(np.array([[0,0,1]]).repeat(ground.shape[0],axis=0))
# mground=utility.mashlab_screened_poisson(pground)
# pground_tree = o3d.geometry.KDTreeFlann(pground)
# colorarray=np.ndarray((len(mground.vertices),3))
# i=0
# for v in mground.vertices:
#     [k, idx, _] = pground_tree.search_knn_vector_3d(v, 1)
#     colorarray[i,:]=ground[idx,3:]
#     i+=1
# mground.vertex_colors=o3d.utility.Vector3dVector(colorarray)
#
# o3d.visualization.draw_geometries([mground])

#build重建
pbuild=o3d.geometry.PointCloud()
print(build.shape[0])
pbuild.points=o3d.utility.Vector3dVector(build[:,:3])
downpbuild=pbuild.voxel_down_sample(3)
print(len(downpbuild.points))
# o3d.visualization.draw_geometries([downpbuild])
# print(downpbuild.points)
# o3d.io.write_point_cloud('build.ply',pbuild)
hdb = HDBSCAN(algorithm='kdtree',n_jobs=-1)
buildlabels= hdb.fit_predict(np.array(downpbuild.points))
print('finish')
meshbuildlist=[]
for i in range(0,np.max(buildlabels)):
    everybuild=np.array(downpbuild.points)[buildlabels == i]
    xmin=np.min(everybuild[:,0])
    ymin=np.min(everybuild[:,1])
    xmax = np.max(everybuild[:,0])
    ymax = np.max(everybuild[:,1])
    condation=np.all([xmin<=build[:,0],build[:,0]<=xmax,ymin<=build[:,1],build[:,1]<=ymax],axis=0)
    ebuildp=o3d.geometry.PointCloud()
    ebuildp.points=o3d.utility.Vector3dVector(build[condation][:,:3])
    ebuildp=ebuildp.voxel_down_sample(2)
    ebuildp.estimate_normals()
    np.savez(str(i)+'build.npz',points=np.array(ebuildp.points),normals=np.array(ebuildp.normals),allow_pickle=True)

    # # ebuildp.colors = o3d.utility.Vector3dVector(build[condation][:, 3:])
    # o3d.visualization.draw_geometries([ebuildp])
    # o3d.io.write_point_cloud(str(i)+'b.ply', ebuildp)
    # ebuildp = o3d.geometry.PointCloud()
    # ebuildp.points = o3d.utility.Vector3dVector(everybuild)
    # ebuildp.colors = o3d.utility.Vector3dVector(build[condation][:, 3:])
    # o3d.io.write_point_cloud(str(i) + 'b.ply', ebuildp)
    # projectbuild=everybuild[:,:2]
    # hull=ConvexHull(projectbuild)
    # v=projectbuild[hull.vertices]
    # v=np.concatenate((v,np.array([[0]]).repeat(v.shape[0],axis=0)),axis=1)
    # footarray=np.ndarray((v.shape[0],3))
    # footarray[:,0]=np.array(range(1,v.shape[0]+1))
    # footarray[:, 2] = np.array(range(1, v.shape[0] + 1))
    # footarray[:, 1] = np.array(range(2, v.shape[0] + 2))
    # footarray[v.shape[0]-1, 1]=1
    # print(footarray)
    # footprint=o3d.geometry.TriangleMesh()
    # footprint.vertices=o3d.utility.Vector3dVector(v)
    #
    # footprint.triangles=o3d.utility.Vector3iVector(footarray)
    # o3d.io.write_triangle_mesh(str(i) + 'foot.obj', footprint)
    # o3d.visualization.draw_geometries([ebuildp,footprint])


# o3d.visualization.draw_geometries(meshbuildlist)








