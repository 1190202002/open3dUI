from PySide6.QtWidgets import QDialog
from ui_ColorregDialog import Ui_ColorregDialog
from PySide6.QtCore import Signal
class ColorregDialog(QDialog):
    sign = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_ColorregDialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.voxel.value(),self.ui.iteration.value()]
        self.sign.emit(info)