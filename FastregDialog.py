from ui_FastregDialog import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal, Slot, QTimer
class FastregDialog(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.voxel.value(),self.ui.correspondence_distance.value(),self.ui.iteration.value()]
        self.sign.emit(info)
    def valuechange(self):
        self.ui.correspondence_distance.setValue(self.ui.voxel.value()*0.5)