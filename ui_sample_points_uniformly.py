# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample_points_uniformly.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 80, 281, 51))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.number_of_points = QSpinBox(self.formLayoutWidget)
        self.number_of_points.setObjectName(u"number_of_points")
        self.number_of_points.setMaximum(10000000)
        self.number_of_points.setValue(3000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.number_of_points)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.tranglenormal = QComboBox(self.formLayoutWidget)
        self.tranglenormal.addItem("")
        self.tranglenormal.addItem("")
        self.tranglenormal.setObjectName(u"tranglenormal")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.tranglenormal)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 210, 75, 24))

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.buttonok)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5747\u5300\u70b9\u91c7\u6837", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u91c7\u6837\u70b9\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4f18\u5316", None))
        self.tranglenormal.setItemText(0, QCoreApplication.translate("Dialog", u"False", None))
        self.tranglenormal.setItemText(1, QCoreApplication.translate("Dialog", u"True", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
    # retranslateUi

