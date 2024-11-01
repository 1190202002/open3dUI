from PySide6.QtWidgets import QDialog
from ui_DensityclusterDialog import Ui_DensityclusterDialog
from PySide6.QtCore import Signal
class DensityclusterDialog(QDialog):
    sign = Signal(float)
    def __init__(self):
        super().__init__()
        self.ui = Ui_DensityclusterDialog()
        self.ui.setupUi(self)
    def buttonok(self):
        self.sign.emit(self.ui.doubleSpinBox.value())