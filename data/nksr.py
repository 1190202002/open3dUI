import nksr
import torch
import open3d as o3d
import numpy as np
device = torch.device("cuda:0")
reconstructor = nksr.Reconstructor(device)
pcd=o3d.io.read_point_cloud("./fragment.ply")
o3d.visualization.draw_geometries([])
# Note that input_xyz and input_normal are torch tensors of shape [N, 3] and [N, 3] respectively.
field = reconstructor.reconstruct(pcd.points, pcd.normals)
# Increase the dual mesh's resolution.
mesh = field.extract_dual_mesh(mise_iter=2)