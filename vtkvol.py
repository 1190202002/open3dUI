import vtkmodules.all as vtk
from vtkmodules.util import vtkImageImportFromArray
import numpy as np
import matplotlib.pyplot as plt
cmap = plt.get_cmap('winter')
file_path = 'data/Image_3.dat'  # 替换为你的.dat文件路径
data=np.fromfile(file_path,dtype=np.float32)
data = data.reshape((80,200,200))
data.transpose((2,0,1))
uperbound=data.max()
lowerbound=data.min()
alphacolordegree=5
image = vtkImageImportFromArray.vtkImageImportFromArray()
image.SetArray(data)                           # 加载三维矩阵
image.SetDataSpacing((1,1,1))
image.Update()

# [创建渲染算法]
volumeMapper =vtk.vtkGPUVolumeRayCastMapper()
volumeMapper.SetInputData(image.GetOutput())    # 加载渲染对象（原始提数据）

# [创建物体颜色函数]
colorFunc = vtk.vtkColorTransferFunction()      # 创建伪彩转换函数
# [创建物体不透明度函数]
opacityFunc = vtk.vtkPiecewiseFunction()        # 创建分段函数
for i in range(alphacolordegree):
    t=(i/(alphacolordegree-1))
    colorFunc.AddRGBPoint(lowerbound+t*(uperbound-lowerbound), cmap(t)[0],cmap(t)[1],cmap(t)[2])   
    opacityFunc.AddPoint(lowerbound+t*(uperbound-lowerbound), lowerbound+t*(uperbound-lowerbound)+0.05) 




# [创建物体属性]
volumeProperty = vtk.vtkVolumeProperty()         
volumeProperty.SetColor(colorFunc)              # 设置颜色转换
volumeProperty.SetScalarOpacity(opacityFunc)    # 设置不透明度
volumeProperty.SetInterpolationTypeToLinear()   # 设置插值方案
volumeProperty.ShadeOn()                        # 阴影

# [创建物体]
vol = vtk.vtkVolume()    
vol.SetMapper(volumeMapper)                     # 加载渲染算法
vol.SetProperty(volumeProperty)                 # 加载物体属性   
vol.SetPosition(0,0,0) 

filename = "data/buildresult64.ply"
reader = vtk.vtkPLYReader()
reader.SetFileName(filename)
reader.Update()

# vertex=vtk.vtkVertexGlyphFilter()
# vertex.AddInputData(reader.GetOutput())
# vertex.Update()


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(reader.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetScale(1)
actor.SetPosition(0,0,0)
actor.SetForceTranslucent(1)


# 创建坐标轴actor
axes = vtk.vtkAxesActor()
axes.SetTotalLength(5, 5, 5)  # 设置坐标轴的总长度
axes.SetShaftTypeToCylinder()  # 设置轴的类型为圆柱体
axes.GetXAxisCaptionActor2D().GetTextActor().SetTextScaleModeToNone()  # 设置X轴标签
axes.GetYAxisCaptionActor2D().GetTextActor().SetTextScaleModeToNone()  # 设置Y轴标签
axes.GetZAxisCaptionActor2D().GetTextActor().SetTextScaleModeToNone()  # 设置Z轴标签

# 设置坐标轴的位置（原点）
axes.SetOrigin(0, 0, 0)


# [创建一个渲染器]
ren = vtk.vtkRenderer()
ren.AddVolume(vol)                              # 加载物体
ren.AddActor(actor)
ren.AddActor(axes)
ren.SetBackground(1.0, 1.0, 1.0)                # 设置背景颜色

# [创建一个渲染窗口]
renWin= vtk.vtkRenderWindow()
renWin.AddRenderer(ren)                         # 加载渲染器
renWin.SetSize(600, 600)                        # 设置窗口尺寸

# [创建交互器]
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)                    # 加载渲染窗口

# [开始绘制]
ren.ResetCamera()                               # 重置相机    
renWin.Render()                                 # 渲染
iren.Initialize()                               # 初始化交互器
iren.Start()                                    # show
