import os
import open3d as o3d
import numpy as np
import laspy
import argparse
from scipy.spatial import KDTree
def readlas(filename):
    las = laspy.read(filename)
    all = np.concatenate((las.xyz,np.vstack((las.red / 65535, las.green / 65535, las.blue / 65535)).transpose()), axis=1)
    # ground = all[las.classification == 2]
    # midtree = all[las.classification == 4]
    # hightree = all[las.classification == 5]
    build = all[las.classification == 6][:,:3]
    pc=all[np.any([las.classification !=1,np.all([las.classification==1,all[:,2]<las.header.z_min+2],axis=0)],axis=0)]
    scale=np.fmax((las.header.x_max-las.header.x_min),(las.header.y_max-las.header.y_min))
    center=np.array(((las.header.x_max+las.header.x_min)/2, (las.header.y_max+las.header.y_min)/2, las.header.z_min))
    v=(pc[:,:3]-center)/scale
    c=pc[:,3:]
    build=(build-center)/scale
    combuild=completebuild(build)

    pcdc = o3d.geometry.PointCloud()
    pcdc.points = o3d.utility.Vector3dVector(np.concatenate([v,combuild],axis=0))
    pcdc = pcdc.voxel_down_sample(0.001)
    return v, c, np.array(pcdc.points), scale

def completebuild(build):
    lowh=1*(build[:,2].max(axis=0)+build[:,2].min(axis=0))/10
    highh= 9*(build[:, 2].max(axis=0) + build[:, 2].min(axis=0))/10
    toh =7*(build[:, 2].max(axis=0) + build[:, 2].min(axis=0)) / 10
    wall=build[np.all([lowh<build[:,2],build[:,2]<highh],axis=0)]
    wall=np.concatenate((wall[:, :2], np.repeat([[0.001]], wall.shape[0], axis=0)), axis=1)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(wall)
    pcd = pcd.voxel_down_sample(0.001)
    wall = np.array(pcd.points)
    wallsize=wall.shape[0]
    complete=np.ndarray((wallsize*int((toh-0.002)/0.002),3))
    len = complete.shape[0]
    complete[:,:2]=np.repeat(wall[:,:2],len/wallsize,axis=0)
    for idx,i in enumerate(range(0,len,wallsize)):
        complete[i:i+wallsize,2]=np.repeat([0.001+idx*0.002],wallsize,axis=0)
    return complete

def readmesh(filename):
    mesh = o3d.io.read_triangle_mesh(filename)
    mesh.compute_vertex_normals()
    return mesh
def make_temp_dataset(in_folder, out_folder):
    os.makedirs(out_folder, exist_ok=True)
    pc_path=in_folder
    points,colors,compoints,scale= readlas(pc_path)

    n = np.ones_like(compoints)
    n = n / (np.linalg.norm(n, axis=1).reshape([-1, 1]) + 1e-6)
    normals = n
    buildname='1'
    npzpath=os.path.join(out_folder,buildname)
    os.makedirs(npzpath,exist_ok=True)
    npz_dict = dict(points=compoints,
                    normals=normals)
    np.savez(os.path.join(npzpath,'pointcloud.npz'), **npz_dict)
    return points,colors,scale
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_folder', type=str, default="./my_dataset",
                        help="the folder path containing point cloud ply files")
    parser.add_argument('--out_folder', type=str, default="./my_dataset_rec", help="the output dir")
    args = parser.parse_args()
    points,colors,scale=make_temp_dataset(args.in_folder, args.out_folder)

    os.system('cd convolutional_occupancy_networks && python generate.py data/demo/build/a.yaml')
    meshdir = 'convolutional_occupancy_networks/out/build/generation/meshes'
    meshpath = os.path.join(meshdir, '1.off')
    mesh = readmesh(meshpath)
    ##paint
    p_kdtree=KDTree(points)
    _,index=p_kdtree.query(np.array(mesh.vertices),1)
    mesh.vertex_colors=o3d.utility.Vector3dVector(colors[index])
    o3d.visualization.draw_geometries([mesh])
