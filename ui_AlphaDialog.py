# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlphaDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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

class Ui_AlphaDialog(object):
    def setupUi(self, AlphaDialog):
        if not AlphaDialog.objectName():
            AlphaDialog.setObjectName(u"AlphaDialog")
        AlphaDialog.resize(411, 255)
        self.pushButton = QPushButton(AlphaDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 200, 75, 24))
        self.verticalLayoutWidget = QWidget(AlphaDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 341, 131))
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

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.normalr = QDoubleSpinBox(self.verticalLayoutWidget)
        self.normalr.setObjectName(u"normalr")
        self.normalr.setWrapping(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.normalr)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.normaln = QSpinBox(self.verticalLayoutWidget)
        self.normaln.setObjectName(u"normaln")
        self.normaln.setMaximum(999)
        self.normaln.setValue(30)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.normaln)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.orientk = QSpinBox(self.verticalLayoutWidget)
        self.orientk.setObjectName(u"orientk")
        self.orientk.setMaximum(999)
        self.orientk.setValue(100)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.orientk)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.doubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximum(10.000000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(0.010000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(AlphaDialog)
        self.pushButton.clicked.connect(AlphaDialog.buttonok)

        QMetaObject.connectSlotsByName(AlphaDialog)
    # setupUi

    def retranslateUi(self, AlphaDialog):
        AlphaDialog.setWindowTitle(QCoreApplication.translate("AlphaDialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("AlphaDialog", u"Yes", None))
        self.label.setText(QCoreApplication.translate("AlphaDialog", u"voxelsize", None))
        self.label_6.setText(QCoreApplication.translate("AlphaDialog", u"radius", None))
        self.label_7.setText(QCoreApplication.translate("AlphaDialog", u"max_nn", None))
        self.label_8.setText(QCoreApplication.translate("AlphaDialog", u"orient k", None))
        self.label_2.setText(QCoreApplication.translate("AlphaDialog", u"alpha", None))
    # retranslateUi

