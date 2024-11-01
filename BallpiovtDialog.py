import open3d as o3d
from PySide6.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QLineEdit, QTableWidget, \
    QTableWidgetItem, QMainWindow, QFileDialog,QWidget
from PySide6.QtGui import QWindow
from PySide6.QtCore import QObject, Signal, Slot
from ui_BallpoivtDialog import Ui_ballpiovtingConfig

class BallConfig(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_ballpiovtingConfig()
        self.ui.setupUi(self)
        self.ui.voxel.valueChanged.connect(self.updatevalue)
    def buttonok(self):
        info=[self.ui.voxel.value(),self.ui.normalr.value(),self.ui.normaln.value(),self.ui.orientk.value()]
        radius=[self.ui.r1.value(),self.ui.r2.value(),self.ui.r3.value(),self.ui.r4.value()]
        radius = [x for x in radius if x != 0]
        radius.sort()
        info.append(radius)
        self.sign.emit(info)
    def updatevalue(self):
        self.ui.normalr.setValue(1.4 * self.ui.voxel.value())
        self.ui.r1.setValue(0.5*self.ui.voxel.value())
        self.ui.r2.setValue(self.ui.voxel.value())
        self.ui.r3.setValue(2 * self.ui.voxel.value())
        self.ui.r4.setValue(4 * self.ui.voxel.value())