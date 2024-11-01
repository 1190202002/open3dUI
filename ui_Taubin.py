# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Taubin.ui'
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

class Ui_Taubin(object):
    def setupUi(self, Taubin):
        if not Taubin.objectName():
            Taubin.setObjectName(u"Taubin")
        Taubin.resize(400, 300)
        self.formLayoutWidget = QWidget(Taubin)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 60, 281, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.iterations = QSpinBox(self.formLayoutWidget)
        self.iterations.setObjectName(u"iterations")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.iterations)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lamda = QDoubleSpinBox(self.formLayoutWidget)
        self.lamda.setObjectName(u"lamda")
        self.lamda.setMinimum(-1.000000000000000)
        self.lamda.setMaximum(1.000000000000000)
        self.lamda.setValue(0.500000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lamda)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.mu = QDoubleSpinBox(self.formLayoutWidget)
        self.mu.setObjectName(u"mu")
        self.mu.setMinimum(-1.000000000000000)
        self.mu.setMaximum(1.000000000000000)
        self.mu.setValue(-0.530000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.mu)

        self.pushButton = QPushButton(Taubin)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 240, 75, 24))

        self.retranslateUi(Taubin)

        QMetaObject.connectSlotsByName(Taubin)
    # setupUi

    def retranslateUi(self, Taubin):
        Taubin.setWindowTitle(QCoreApplication.translate("Taubin", u"\u5e73\u6ed1", None))
        self.label.setText(QCoreApplication.translate("Taubin", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Taubin", u"\u53c2\u65701", None))
        self.label_3.setText(QCoreApplication.translate("Taubin", u"\u53c2\u65702", None))
        self.pushButton.setText(QCoreApplication.translate("Taubin", u"\u786e\u8ba4", None))
    # retranslateUi

