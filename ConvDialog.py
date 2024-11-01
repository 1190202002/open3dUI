from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from ui_ConvDialog  import Ui_Dialog
class Conv_Dialog(QDialog):
    sign=Signal(list)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    def buttonok(self):
        cg=''
        if(self.ui.GCcomboBox.currentText()!='CUDA'):
            cg='--no-cuda'
        info=[cg,self.ui.unitsizeSpinBox.value(),self.ui.queryvolsizespinBox.value(),self.ui.resolutionspinBox_2.value()]
        self.sign.emit(info)
