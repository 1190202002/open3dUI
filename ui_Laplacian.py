# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Laplacian.ui'
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

class Ui_Laplacian(object):
    def setupUi(self, Laplacian):
        if not Laplacian.objectName():
            Laplacian.setObjectName(u"Laplacian")
        Laplacian.resize(400, 300)
        self.pushButton = QPushButton(Laplacian)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 240, 75, 24))
        self.formLayoutWidget = QWidget(Laplacian)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 60, 281, 51))
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


        self.retranslateUi(Laplacian)

        QMetaObject.connectSlotsByName(Laplacian)
    # setupUi

    def retranslateUi(self, Laplacian):
        Laplacian.setWindowTitle(QCoreApplication.translate("Laplacian", u"\u516c\u5f0f\u5e73\u6ed1", None))
        self.pushButton.setText(QCoreApplication.translate("Laplacian", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("Laplacian", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Laplacian", u"\u60e9\u7f5a\u56e0\u5b50", None))
    # retranslateUi

