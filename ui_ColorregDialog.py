# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ColorregDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFormLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_ColorregDialog(object):
    def setupUi(self, ColorregDialog):
        if not ColorregDialog.objectName():
            ColorregDialog.setObjectName(u"ColorregDialog")
        ColorregDialog.resize(400, 300)
        self.pushButton = QPushButton(ColorregDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 220, 75, 24))
        self.verticalLayoutWidget = QWidget(ColorregDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 50, 311, 51))
        self.formLayout = QFormLayout(self.verticalLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.voxel = QDoubleSpinBox(self.verticalLayoutWidget)
        self.voxel.setObjectName(u"voxel")
        self.voxel.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.voxel)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.iteration = QSpinBox(self.verticalLayoutWidget)
        self.iteration.setObjectName(u"iteration")
        self.iteration.setMaximum(999)
        self.iteration.setValue(64)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.iteration)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ColorregDialog)
        self.pushButton.clicked.connect(ColorregDialog.buttonok)

        QMetaObject.connectSlotsByName(ColorregDialog)
    # setupUi

    def retranslateUi(self, ColorregDialog):
        ColorregDialog.setWindowTitle(QCoreApplication.translate("ColorregDialog", u"\u989c\u8272\u5c40\u90e8\u914d\u51c6", None))
        self.pushButton.setText(QCoreApplication.translate("ColorregDialog", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("ColorregDialog", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.label_3.setText(QCoreApplication.translate("ColorregDialog", u"\u8fed\u4ee3\u6b21\u6570", None))
    # retranslateUi

