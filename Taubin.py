from ui_Taubin import Ui_Taubin
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class Taubin(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Taubin()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonok)
    def buttonok(self):
        info=[self.ui.iterations.value(),self.ui.lamda.value(),self.ui.mu.value()]
        self.sign.emit(info)
