from PySide6.QtWidgets import QDialog
from ui_sample_points_poisson_disk import Ui_Dialog
from PySide6.QtCore import Signal
class SamplepoissonDialog(QDialog):
    sign = Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def buttonok(self):
        info=[self.ui.number_of_points.value(),self.ui.doubleSpinBox.value(), bool(self.ui.tranglenormal.currentIndex())]
        self.sign.emit(info)
