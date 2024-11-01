from ui_removestaticoutlinerDialog import Ui_Dialog
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class removestaticoutlinerDialog(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info = [self.ui.nb_neighbors.value(), self.ui.std_ratio.value()]
        self.sign.emit(info)