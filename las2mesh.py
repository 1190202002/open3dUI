import os

import open3d as o3d
import numpy as np
import laspy
def readlas(filename):
    las = laspy.read(filename)
    pos=las.xyz - np.array((las.header.x_min, las.header.y_min, las.header.z_min))
    color=np.vstack((las.red / 65535, las.green / 65535, las.blue / 65535)).transpose()
    return pos,color
def writenpz(pcd,voxel,filename):
    pcd=pcd.voxel_down_sample(voxel)
    print(len(pcd.points))
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(100)
    np.savez(os.path.join(filename,'pointcloud.npz'),points=np.array(pcd.points),normals=np.array(pcd.normals),allow_pickle=True)
def readmesh(filename):
    mesh = o3d.io.read_triangle_mesh(filename)
    mesh.compute_vertex_normals()
    return mesh
if __name__=='__main__':
    pos,color=readlas('data/colorpointcloud.las')
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(pos)
    pcd.colors = o3d.utility.Vector3dVector(color)
    pcd_tree=o3d.geometry.KDTreeFlann(pcd)
    npzdir='../convolutional_occupancy_networks/data/demo/build'
    buildname='14'
    npzpath=os.path.join(npzdir,buildname)
    meshdir='../convolutional_occupancy_networks/out/build/generation/meshes'
    if not os.path.exists(npzpath):
        print('no npz file found')
        os.mkdir(npzpath)
        writenpz(pcd,1,npzpath)
    os.system('cd ../convolutional_occupancy_networks && python generate.py data/demo/build/a.yaml')
    # os.system('pause')
    meshpath=os.path.join(meshdir,buildname+'.off')
    mesh=readmesh(meshpath)
    print(len(mesh.vertices))
    mvcolors=np.ndarray(shape=(len(mesh.vertices),3))
    pcdcolors=np.array(pcd.colors)
    for i,v in enumerate(mesh.vertices):
        [k,idx,_]=pcd_tree.search_knn_vector_3d(v,1)
        mvcolors[i,:]=pcdcolors[idx,:]
    mesh.vertex_colors=o3d.utility.Vector3dVector(mvcolors)
    o3d.visualization.draw_geometries([mesh])


