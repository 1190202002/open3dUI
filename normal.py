from ui_normal import Ui_normal
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class normal(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_normal()
        self.ui.setupUi(self)
    def buttonok(self):

        info = [self.ui.normalr.value(), self.ui.normaln.value(), self.ui.orientk.value()]
        self.sign.emit(info)