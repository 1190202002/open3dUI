import laspy
import numpy as np
import cv2 as cv
import open3d as o3d
las=laspy.read("./data/colorpointcloud.las")
all = np.concatenate((las.xyz-np.array((las.header.x_min, las.header.y_min, las.header.z_min)),np.vstack((las.red / 65535, las.green / 65535, las.blue / 65535)).transpose()), axis=1)
build = all[las.classification == 6][:,:3]
map=np.unique(np.int32(build[:,:2]),axis=0)
width=np.int32(las.header.x_max-las.header.x_min)
height=np.int32(las.header.y_max-las.header.y_min)
img=np.zeros((height,width,1),dtype=np.uint8)
for i in map:
    img[i[1]][i[0]]=255
img=cv.bilateralFilter(img,9,75,75)
contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt=contours[0]
pcd=o3d.geometry.PointCloud()
pcd.points=o3d.utility.Vector3dVector(build)
pcd=pcd.voxel_down_sample(10)
o3d.io.write_point_cloud("build.ply",pcd)

img=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
epsilon = 0.01*cv.arcLength(cnt,True)
vnf=[]
for i in range(0,len(contours)):
    approx = cv.approxPolyDP(contours[i],epsilon,True).reshape((-1,2))
    if approx.shape[0]>2:
        # cv.polylines(img,approx,True,(255,0,0))
        cv.drawContours(img, [approx], 0, (0,255,0), 1)
        cv.imshow("img",img)
        edgev=approx
        edgev=np.concatenate((edgev,np.zeros((edgev.shape[0],1))),axis=1)
        vn=np.repeat(np.array([[0,0,1]]),edgev.shape[0],axis=0)
        edgef=np.concatenate((np.arange(2,edgev.shape[0]).reshape(-1,1),np.arange(1,edgev.shape[0]-1).reshape(-1,1),np.zeros((edgev.shape[0]-2,1))),axis=1)
        vnf.append((edgev,vn,edgef))
        cv.waitKey(0)
with open('edge.obj','w') as f:
    vertices=''
    for vs,_,_ in vnf:
        for v in vs:
            vertices+='v '+str(v[0])+' '+str(v[1])+' '+str(v[2])+'\n'
    f.write(vertices)
    vn=''
    for vs, _, _ in vnf:
        for v in vs:
            vn+='vn 0 0 1'+'\n'
    f.write(vn)
    face=''
    len=0
    for v,_,_ in vnf:
        face += 'f'
        for i in range(len+v.shape[0],len,-1):
            face+=' '+str(i)+'//'+str(i)
        face+='\n'
        len=len+v.shape[0]
    f.write(face)


