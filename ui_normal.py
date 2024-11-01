# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'normal.ui'
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

class Ui_normal(object):
    def setupUi(self, normal):
        if not normal.objectName():
            normal.setObjectName(u"normal")
        normal.resize(400, 300)
        self.pushButton = QPushButton(normal)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 220, 75, 24))
        self.verticalLayoutWidget = QWidget(normal)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 50, 311, 81))
        self.formLayout = QFormLayout(self.verticalLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.normalr = QDoubleSpinBox(self.verticalLayoutWidget)
        self.normalr.setObjectName(u"normalr")
        self.normalr.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.normalr)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.normaln = QSpinBox(self.verticalLayoutWidget)
        self.normaln.setObjectName(u"normaln")
        self.normaln.setValue(30)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.normaln)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.orientk = QSpinBox(self.verticalLayoutWidget)
        self.orientk.setObjectName(u"orientk")
        self.orientk.setMaximum(999)
        self.orientk.setValue(100)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.orientk)


        self.retranslateUi(normal)
        self.pushButton.clicked.connect(normal.buttonok)

        QMetaObject.connectSlotsByName(normal)
    # setupUi

    def retranslateUi(self, normal):
        normal.setWindowTitle(QCoreApplication.translate("normal", u"\u6cd5\u5411\u4f30\u8ba1", None))
        self.pushButton.setText(QCoreApplication.translate("normal", u"\u786e\u8ba4", None))
        self.label_6.setText(QCoreApplication.translate("normal", u"\u534a\u5f84", None))
        self.label_7.setText(QCoreApplication.translate("normal", u"\u91c7\u6837\u70b9", None))
        self.label_8.setText(QCoreApplication.translate("normal", u"\u5b9a\u5411\u70b9", None))
    # retranslateUi

