from ui_downsample import Ui_downsample
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class downsample(QDialog):
    sign=Signal(float)
    def __init__(self):
        super().__init__()
        self.ui = Ui_downsample()
        self.ui.setupUi(self)
    def buttonok(self):
        self.sign.emit(self.ui.voxel.value())