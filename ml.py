import open3d as o3d
import numpy as np
from copy import deepcopy
from sklearn import cluster
import matplotlib.pyplot as plt
import laspy
import utility

def KMeans():
    # KMeans聚类，非监督

    #read
    point_cloud_path = 'data/colorpointcloud.las'
    las = laspy.read(point_cloud_path)
    point_data = np.stack([las.x, las.y, las.z], axis=0).transpose((1, 0))
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_data)
    if las.red.max() >= 256: las.red >>= 8
    if las.green.max() >= 256: las.green >>= 8
    if las.blue.max() >= 256: las.blue >>= 8
    colors = np.stack([las.red * 256 / 65535, las.green * 256 / 65535, las.blue * 256 / 65535], axis=0).transpose(
        (1, 0))
    pcd.colors = o3d.utility.Vector3dVector(colors)
    pcd=pcd.remove_duplicated_points()
    pcd=pcd.voxel_down_sample(0.5)
    pcd.translate(-pcd.get_center())


    points = np.array(pcd.points)[:,:2]
    print(points.shape[0])
    n_clusters =points.shape[0]//100000
    # 将点云数据转换为 numpy 数组，并使用 sklearn 的 KMeans 进行聚类
    kmeans = cluster.KMeans(n_clusters=n_clusters, random_state=42, n_init=10, init="k-means++")
    kmeans.fit(points)  # 获取聚类结果，这里主要是每个点的类别标签
    labels = kmeans.labels_
    print(labels)
    pcdlist=[]
    for i in range(n_clusters):
        pcdv = o3d.geometry.PointCloud()
        pcdv.points=o3d.utility.Vector3dVector(np.array(pcd.points)[labels == i])
        pcdv.colors = o3d.utility.Vector3dVector(np.array(pcd.colors)[labels == i])
        pcdlist.append(pcdv)
    o3d.visualization.draw_geometries(pcdlist)
    mesh = o3d.geometry.TriangleMesh()
    for pcd in pcdlist:
        mesh+=utility.mashlab_ball_piovt(pcd,normalr=2,normaln=30,orientk=100,clustering=20,creasethr=90)
        print("1")
    o3d.visualization.draw_geometries([mesh])
    o3d.io.write_triangle_mesh("kmeanscity.ply",mesh)


if __name__ == "__main__":
    KMeans()
