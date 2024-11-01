from PySide6.QtWidgets import QDialog
from ui_MulregDialog import Ui_MulregDialog
from PySide6.QtCore import Signal
class MulregDialog(QDialog):
    sign = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MulregDialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.voxel.value(),self.ui.correspondence_distance.value(),self.ui.iteration.value(),self.ui.edge_threshold.value(),self.ui.preference_loop.value(),self.ui.reference_node.value()]
        self.sign.emit(info)
    def valuechange(self):
        self.ui.correspondence_distance.setValue(self.ui.voxel.value() * 0.5)