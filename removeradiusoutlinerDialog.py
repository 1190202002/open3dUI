from ui_removeradiusoutlinerDialog import Ui_Dialog
from PySide6.QtWidgets import QApplication,QDialog
from PySide6.QtCore import Signal
class removeradiusoutlinerDialog(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.nb_points.value(),self.ui.radius.value()]
        self.sign.emit(info)