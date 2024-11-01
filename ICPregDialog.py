from PySide6.QtWidgets import QDialog
from ui_ICPregDialog import Ui_ICPregDialog
from PySide6.QtCore import Signal
class ICPregDialog(QDialog):
    sign = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_ICPregDialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.voxel.value(),self.ui.iteration.value()]
        self.sign.emit(info)