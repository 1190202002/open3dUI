import sys
import torch
import tqdm
import matplotlib.pyplot as plt
from pytorch3d.io import load_obj,save_obj,load_ply
from pytorch3d.vis import plotly_vis
from pytorch3d.utils import ico_sphere
from pytorch3d.structures import Meshes,Pointclouds
from pytorch3d.ops import sample_points_from_meshes,sample_farthest_points
from pytorch3d.loss import chamfer_distance,mesh_edge_loss,mesh_normal_consistency,mesh_laplacian_smoothing
import open3d as o3d
device=torch.device("cuda")
def plot_pointcloud(points,title=""):
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot(111,projection='3d')
    ax.scatter3D(points[:,0],points[:,1],points[:,2])
    ax.set_title(title)
    plt.show()
verts,aux=load_ply('./data/fragment.ply')
verts=verts.to(device)
# faces_idx=faces.verts_idx.to(device)
center=verts.mean(0)
verts=verts-center
scale=max(verts.abs().max(0)[0])
verts=verts/scale
trg_point=Pointclouds(points=[verts])
src_mesh=ico_sphere(4,device=device)
deform_verts=torch.full(src_mesh.verts_packed().shape,0.0,device=device,requires_grad=True)
optimizer=torch.optim.SGD([deform_verts],lr=1.0,momentum=0.9)
# Number of optimization steps
Niter = 2000
# Weight for the chamfer loss
w_chamfer = 1.0
# Weight for mesh edge loss
w_edge = 1.0
# Weight for mesh normal consistency
w_normal = 0.01
# Weight for mesh laplacian smoothing
w_laplacian = 0.1
# Plot period for the losses
plot_period = 250
loop=tqdm.tqdm(range(Niter))

chamfer_losses = []
laplacian_losses = []
edge_losses = []
normal_losses = []

for i in loop:
    # Initialize optimizer
    optimizer.zero_grad()

    # Deform the mesh
    new_src_mesh = src_mesh.offset_verts(deform_verts)

    # We sample 5k points from the surface of each mesh
    sample_trg = trg_point.subsample(50000)
    sample_src = sample_points_from_meshes(new_src_mesh, 50000)

    # We compare the two sets of pointclouds by computing (a) the chamfer loss
    loss_chamfer, _ = chamfer_distance(sample_trg, sample_src)

    # and (b) the edge length of the predicted mesh
    loss_edge = mesh_edge_loss(new_src_mesh)

    # mesh normal consistency
    loss_normal = mesh_normal_consistency(new_src_mesh)

    # mesh laplacian smoothing
    loss_laplacian = mesh_laplacian_smoothing(new_src_mesh, method="uniform")

    # Weighted sum of the losses
    loss = loss_chamfer * w_chamfer + loss_edge * w_edge + loss_normal * w_normal + loss_laplacian * w_laplacian

    # Print the losses
    loop.set_description('total_loss = %.6f' % loss)

    # Save the losses for plotting
    chamfer_losses.append(float(loss_chamfer.detach().cpu()))
    edge_losses.append(float(loss_edge.detach().cpu()))
    normal_losses.append(float(loss_normal.detach().cpu()))
    laplacian_losses.append(float(loss_laplacian.detach().cpu()))

    # Plot mesh
    if i % plot_period == 0:
        plot_pointcloud(sample_points_from_meshes(new_src_mesh).clone().detach().cpu().squeeze().numpy(), title="iter: %d" % i)

    # Optimization step
    loss.backward()
    optimizer.step()
fig = plt.figure(figsize=(13, 5))
ax = fig.gca()
ax.plot(chamfer_losses, label="chamfer loss")
ax.plot(edge_losses, label="edge loss")
ax.plot(normal_losses, label="normal loss")
ax.plot(laplacian_losses, label="laplacian loss")
ax.legend(fontsize="16")
ax.set_xlabel("Iteration", fontsize="16")
ax.set_ylabel("Loss", fontsize="16")
ax.set_title("Loss vs iterations", fontsize="16")
final_verts, final_faces = new_src_mesh.get_mesh_verts_faces(0)

# Scale normalize back to the original target size
final_verts = final_verts * scale + center

# Store the predicted mesh using save_obj
final_obj = 'final_model.obj'
save_obj(final_obj, final_verts, final_faces)