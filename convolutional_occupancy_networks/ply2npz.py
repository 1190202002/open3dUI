import numpy as np
import open3d as o3d
ply=o3d.io.read_point_cloud('data/demo/build/a/pointcloud.ply')
ply.estimate_normals()
points=np.asarray(ply.points)
normals=np.asarray(ply.normals)
np.savez('data/demo/build/a/pointcloud.npz', points=points, normals=normals, allow_pickle=True)
