# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConvDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 220, 75, 24))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 30, 281, 181))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GCcomboBox = QComboBox(self.layoutWidget)
        self.GCcomboBox.addItem("")
        self.GCcomboBox.addItem("")
        self.GCcomboBox.setObjectName(u"GCcomboBox")

        self.verticalLayout_3.addWidget(self.GCcomboBox)

        self.unitsizeSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.unitsizeSpinBox.setObjectName(u"unitsizeSpinBox")
        self.unitsizeSpinBox.setDecimals(4)
        self.unitsizeSpinBox.setMaximum(1.000000000000000)
        self.unitsizeSpinBox.setSingleStep(0.000500000000000)
        self.unitsizeSpinBox.setValue(0.002000000000000)

        self.verticalLayout_3.addWidget(self.unitsizeSpinBox)

        self.queryvolsizespinBox = QSpinBox(self.layoutWidget)
        self.queryvolsizespinBox.setObjectName(u"queryvolsizespinBox")
        self.queryvolsizespinBox.setMaximum(180)
        self.queryvolsizespinBox.setSingleStep(10)
        self.queryvolsizespinBox.setValue(90)

        self.verticalLayout_3.addWidget(self.queryvolsizespinBox)

        self.resolutionspinBox_2 = QSpinBox(self.layoutWidget)
        self.resolutionspinBox_2.setObjectName(u"resolutionspinBox_2")
        self.resolutionspinBox_2.setMaximum(512)
        self.resolutionspinBox_2.setValue(128)

        self.verticalLayout_3.addWidget(self.resolutionspinBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.buttonok)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5927\u578b\u901a\u7528\u91cd\u5efa", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u663e\u5361", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5355\u4f4d\u5927\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u67e5\u8be2\u4f53\u957f\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5206\u8fa8\u7387", None))
        self.GCcomboBox.setItemText(0, QCoreApplication.translate("Dialog", u"CUDA", None))
        self.GCcomboBox.setItemText(1, QCoreApplication.translate("Dialog", u"CPU", None))

    # retranslateUi

