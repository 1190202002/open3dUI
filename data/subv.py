import os
import open3d as o3d
import numpy as np
import laspy
from scipy.spatial import KDTree
from scipy.spatial import Delaunay
import utility
mesh=o3d.geometry.TriangleMesh()
path="simpobj"
for obj in os.listdir(path):
    m=o3d.io.read_triangle_mesh(os.path.join(path,obj))
    mesh+=m
print(mesh)
mesh=mesh.subdivide_midpoint(3)
print(mesh)
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
las = laspy.read('colorpointcloud.las')
all=np.concatenate((las.xyz,np.vstack((las.red/65535,las.green/65535,las.blue/65535)).transpose()),axis=1)
points=all[:,:3]
colors=all[:,3:]
p_kdtree=KDTree(points)
_,index=p_kdtree.query(np.array(mesh.vertices),1)
mesh.vertex_colors=o3d.utility.Vector3dVector(colors[index])
o3d.visualization.draw_geometries([mesh])

# ground=all[np.any([las.classification==2,las.classification==4,las.classification==5],axis=0)]
# gpcd=o3d.geometry.PointCloud()
# gpcd.points=o3d.utility.Vector3dVector(ground[:,:3])
# gpcd.colors=o3d.utility.Vector3dVector(ground[:,3:])
# gmesh=utility.mashlab_ball_piovt(gpcd,1,1.5,30,100,20,90)
# mesh+=gmesh
# o3d.visualization.draw_geometries([mesh])
ground=all[np.any([las.classification==2,las.classification==4,las.classification==5],axis=0)]
mground=o3d.geometry.TriangleMesh()
mground.vertices=o3d.utility.Vector3dVector(ground[:,:3])
mground.vertex_colors=o3d.utility.Vector3dVector(ground[:,3:])
mground.vertex_normals=o3d.utility.Vector3dVector(np.array([[0,0,1]]).repeat(ground.shape[0],axis=0))
mground.triangles=o3d.utility.Vector3iVector(Delaunay(ground[:,:2]).simplices)
o3d.visualization.draw_geometries([mground,mesh])


