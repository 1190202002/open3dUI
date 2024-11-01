from PySide6.QtWidgets import QDialog
from ui_ballautoguessDialog import Ui_Dialog
from PySide6.QtCore import Signal
class BallautoGuess(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.voxel.valueChanged.connect(self.updatevalue)
    def buttonok(self):
        info=[self.ui.voxel.value(),self.ui.normalr.value(),self.ui.normaln.value(),
              self.ui.orientk.value(),self.ui.clustering.value(),self.ui.creasethr.value()]
        self.sign.emit(info)
    def updatevalue(self):
        self.ui.normalr.setValue(1.4 * self.ui.voxel.value())
