from ui_AlphaDialog import Ui_AlphaDialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal


class AlphaDialog(QDialog):
    sign = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_AlphaDialog()
        self.ui.setupUi(self)
        self.ui.voxel.valueChanged.connect(self.updatevalue)

    def buttonok(self):
        info = [self.ui.voxel.value(), self.ui.normalr.value(), self.ui.normaln.value(), self.ui.orientk.value(),self.ui.doubleSpinBox.value()]
        self.sign.emit(info)
    def updatevalue(self):
        self.ui.normalr.setValue(1.4 * self.ui.voxel.value())