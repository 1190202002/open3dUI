from PySide6.QtWidgets import QDialog
from ui_PossionDialog import Ui_PossionDialog
from PySide6.QtCore import Signal
class PossionDialog(QDialog):
    sign = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_PossionDialog()
        self.ui.setupUi(self)
        self.ui.voxel.valueChanged.connect(self.updatevalue)
    def buttonok(self):
        info = [self.ui.voxel.value(), self.ui.normalr.value(), self.ui.normaln.value(), self.ui.orientk.value()
                ,self.ui.depth.value(), self.ui.width.value(), self.ui.scale.value(),bool(self.ui.comboBox.currentIndex()),self.ui.nthreads.value()]
        self.sign.emit(info)
    def updatevalue(self):
        self.ui.normalr.setValue(1.4 * self.ui.voxel.value())