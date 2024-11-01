from ui_Laplacian import Ui_Laplacian
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class Laplacian(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Laplacian()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonok)
    def buttonok(self):
        info=[self.ui.iterations.value(),self.ui.lamda.value()]
        self.sign.emit(info)
