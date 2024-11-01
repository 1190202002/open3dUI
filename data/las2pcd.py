import laspy
import numpy as np
import open3d as o3d

def read_las(path):
    las = laspy.read(path)
    scale = np.fmax((las.header.x_max - las.header.x_min), (las.header.y_max - las.header.y_min))
    center = np.array(((las.header.x_max + las.header.x_min) / 2, (las.header.y_max + las.header.y_min) / 2, las.header.z_min))
    pos = (las.xyz - center) / scale
    pcd=o3d.geometry.PointCloud()
    pcd.points=o3d.utility.Vector3dVector(pos)
    return pcd
pcd=read_las('./colorpointcloud.las')
pcd=pcd.voxel_down_sample(0.001)
print(pcd)
o3d.io.write_point_cloud("colorpointcloud.pcd", pcd)