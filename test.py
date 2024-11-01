import os

import open3d as o3d
import numpy as np
# import utility
import laspy


# point_cloud_path = 'data/colorpointcloud.las'
# las = laspy.read(point_cloud_path)
# # # 写入点
# point_data = np.stack([las.x, las.y, las.z], axis=0).transpose((1, 0))
# pcd = o3d.geometry.PointCloud()
# pcd.points = o3d.utility.Vector3dVector(point_data)
# if las.red.max() >= 256: las.red >>= 8
# if las.green.max() >= 256: las.green >>= 8
# if las.blue.max() >= 256: las.blue >>= 8
# colors = np.stack([las.red * 256 / 65535, las.green * 256 / 65535, las.blue * 256 / 65535], axis=0).transpose(
#     (1, 0))
# pcd.colors = o3d.utility.Vector3dVector(colors)
# pcd.remove_duplicated_points()
# pcd=pcd.voxel_down_sample(1)
# pcd.estimate_normals()
# pcd.orient_normals_consistent_tangent_plane(100)
# pcd.translate(-pcd.get_center())
# # os.mkdir('build')
# np.savez('build/pointcloud.npz', points=pcd.points,normals=pcd.normals)
#
#
#
# # plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
# #                                          ransac_n=3,
# #                                          num_iterations=1000)
# # [a, b, c, d] = plane_model
# # print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")
# oboxes = pcd.detect_planar_patches(
#     normal_variance_threshold_deg=60,
#     coplanarity_deg=75,
#     outlier_ratio=0.75,
#     min_plane_edge_length=0,
#     min_num_points=0,
#     search_param=o3d.geometry.KDTreeSearchParamKNN(knn=30))
# geometries = []
# for obox in oboxes:
#     mesh = o3d.geometry.TriangleMesh.create_from_oriented_bounding_box(obox, scale=[1, 1, 0.0001])
#
#     print(mesh)
#     mesh.paint_uniform_color(obox.color)
#     geometries.append(mesh)
#     geometries.append(obox)
# geometries.append(pcd)
#
# o3d.visualization.draw_geometries(geometries,
#                                   zoom=0.62,
#                                   front=[0.4361, -0.2632, -0.8605],
#                                   lookat=[2.4947, 1.7728, 1.5541],
#                                   up=[-0.1726, -0.9630, 0.2071])

# inlier_cloud = pcd.select_by_index(inliers)
# inlier_cloud.paint_uniform_color([1.0, 0, 0])
# outlier_cloud = pcd.select_by_index(inliers, invert=True)
# o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
# las=laspy.read('./data/colorpointcloud.las')
# pcd=o3d.geometry.PointCloud()
# pcd.points=o3d.utility.Vector3dVector(las.xyz)
# o3d.io.write_point_cloud("./data/pointcloud.ply",pcd)
a=np.load('data/points_iou.npz')
print(a['occupancies'])