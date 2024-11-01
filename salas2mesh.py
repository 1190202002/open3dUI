import os
import open3d as o3d
import numpy as np
import laspy
import argparse
from scipy.spatial import KDTree
def readlas(filename):
    las = laspy.read(filename)
    v=las.xyz
    c=np.vstack((las.red / 65535, las.green / 65535, las.blue / 65535)).transpose()
    n = np.ones_like(v)
    n = n / (np.linalg.norm(n, axis=1).reshape([-1, 1]) + 1e-6)
    return v, n, c
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
def make_temp_dataset(in_folder, out_folder, do_norm=True):

    os.makedirs(out_folder, exist_ok=True)
    pc_path=in_folder
    points, normals,colors= readlas(pc_path)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd=pcd.voxel_down_sample(1)
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(100)
    o3d.io.write_point_cloud("../SA-ConvONet/data/build/pointcloud.ply", pcd)
    points=np.array(pcd.points)
    normals=np.array(pcd.normals)
    vert_max = points.max(axis=0)
    vert_min = points.min(axis=0)
    if do_norm:
        loc = (vert_min + vert_max) / 2
        scale = (vert_max - vert_min).max()
    else:
        loc = np.array([0, 0, 0], dtype=np.float64)
        scale = np.array([1.0], dtype=np.float64)
    print('loc', loc, 'scale', scale)

    points = (points - loc) / scale
    # normals = normals / np.linalg.norm(normals, axis=1, keepdims=True)
    save_npz_path = os.path.join(out_folder,"pointcloud.npz")
    npz_dict = dict(points=points.astype(np.float16),
                    normals=normals.astype(np.float16),
                    loc=loc.astype(np.float64),
                    scale=scale.astype(np.float64))
    np.savez(save_npz_path, **npz_dict)
    print(f"we save pointcloud npz to: {save_npz_path}")

    save_npz_path = os.path.join(out_folder, "points_iou.npz")
    #if not do_norm: raise
    NUM_SPATIAL_PTS = 1000000 # 100w
    RATIO_SUR = 0.25
    RATIO_STD = 0.75
    if do_norm:
        STD = 0.1
    else:
        STD = 0.1 * ((vert_max - vert_min).max())
    spatial_points_xyz = np.concatenate([points[np.random.choice(len(points), size=(int(NUM_SPATIAL_PTS * RATIO_STD), ))] + \
                                            np.random.randn(int(NUM_SPATIAL_PTS * RATIO_STD), 3) * STD,
                                         np.random.rand(int(NUM_SPATIAL_PTS * (1-RATIO_SUR-RATIO_STD)), 3)*1.1-0.55,
                                         points[np.random.choice(len(points), size=(int(NUM_SPATIAL_PTS*RATIO_SUR), ))]], axis=0)
    spatial_points_occ = np.concatenate([np.ones([int(NUM_SPATIAL_PTS * (1-RATIO_SUR))]),
                                                  np.zeros([int(NUM_SPATIAL_PTS*RATIO_SUR)])], axis=0) # # dummy (0 for surface, 1 for space)
    shuffle_index = np.random.permutation(NUM_SPATIAL_PTS)
    spatial_points_xyz = spatial_points_xyz[shuffle_index]
    spatial_points_occ = spatial_points_occ[shuffle_index]
    npz_dict = dict(points=spatial_points_xyz.astype(dtype=np.float16), # for normalization
                    occupancies=np.packbits(spatial_points_occ.astype(dtype=bool)),
                    z_scale=np.array(0).astype(np.float64),
                    semantics=np.zeros([NUM_SPATIAL_PTS], dtype=np.int64))
    np.savez(save_npz_path, **npz_dict) # dummy file
    print(f"we save points_iou npz to: {save_npz_path}")

    test_lst_path = os.path.join(out_folder,"test.lst")
    with open(test_lst_path, "w") as f:
        f.write(pc_path.split('/')[-2] + "\n")
    print(f"we save test list to: {test_lst_path}")
    return points,colors
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_folder', type=str, default="./my_dataset",
                        help="the folder path containing point cloud ply files")
    parser.add_argument('--out_folder', type=str, default="./my_dataset_rec", help="the output dir")
    parser.add_argument('--do_norm', action="store_true", help="do normalization within -0.5 ~ +0.5")
    args = parser.parse_args()
    points,colors=make_temp_dataset(args.in_folder, args.out_folder, do_norm=args.do_norm)

    os.system('cd ../SA-ConvONet && python generate_optim_largescene.py configs/build.yaml')

    meshpath='../SA-ConvONet/out/build/generation/meshes/data.off'
    mesh=readmesh(meshpath)
    print(len(mesh.vertices))

    ##paint
    p_kdtree=KDTree(points)
    _,index=p_kdtree.query(np.array(mesh.vertices),1)
    mesh.vertex_colors=o3d.utility.Vector3dVector(colors[index])
    o3d.visualization.draw_geometries([mesh])


