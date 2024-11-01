from ui_Average import Ui_Average
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class Average(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Average()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonok)
    def buttonok(self):
        info=[self.ui.iterations.value()]
        self.sign.emit(info)
