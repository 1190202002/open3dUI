from PySide6.QtWidgets import QDialog
from ui_closeholeDialog import Ui_Dialog
from PySide6.QtCore import Signal
class closeholesDialog(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.maxholesize.value(),bool(self.ui.refinehole.currentIndex()),self.ui.refineholeedgelen.value()]
        self.sign.emit(info)