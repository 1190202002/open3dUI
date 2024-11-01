import open3d as o3d
import laspy
import numpy as np
point_cloud_path = 'data/colorpointcloud.las'
las = laspy.read(point_cloud_path)
# # 写入点
point_data = np.stack([las.x, las.y, las.z], axis=0).transpose((1, 0))
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_data)
if las.red.max() >= 256: las.red >>= 8
if las.green.max() >= 256: las.green >>= 8
if las.blue.max() >= 256: las.blue >>= 8
colors = np.stack([las.red * 256 / 65535, las.green * 256 / 65535, las.blue * 256 / 65535], axis=0).transpose(
    (1, 0))
pcd.colors = o3d.utility.Vector3dVector(colors)
pcd.remove_duplicated_points()
pcd=pcd.voxel_down_sample(1)
print(len(pcd.points))
pcd.translate(-pcd.get_center())

mesh=o3d.io.read_triangle_mesh('build/12.off')
mesh.compute_vertex_normals()
print("1")
pcdtree=o3d.geometry.KDTreeFlann(pcd)
o3d.geometry.TriangleMesh()
mcolors=np.ndarray(shape=(len(mesh.vertices), 3))
i=0
pcdcolors=np.array(pcd.colors)
for v in mesh.vertices:
    [k,idx,_]=pcdtree.search_knn_vector_3d(v,1)
    mcolors[i,:]=pcdcolors[k,:]
    i+=1
print("2")
mesh.vertex_colors=o3d.utility.Vector3dVector(mcolors)
o3d.visualization.draw_geometries([mesh])


