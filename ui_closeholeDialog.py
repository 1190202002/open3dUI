# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'closeholeDialog.ui'
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
    QFormLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 50, 271, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.maxholesize = QSpinBox(self.formLayoutWidget)
        self.maxholesize.setObjectName(u"maxholesize")
        self.maxholesize.setMaximum(100000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.maxholesize)

        self.refinehole = QComboBox(self.formLayoutWidget)
        self.refinehole.addItem("")
        self.refinehole.addItem("")
        self.refinehole.setObjectName(u"refinehole")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.refinehole)

        self.refineholeedgelen = QDoubleSpinBox(self.formLayoutWidget)
        self.refineholeedgelen.setObjectName(u"refineholeedgelen")
        self.refineholeedgelen.setDecimals(1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.refineholeedgelen)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 220, 75, 24))

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.buttonok)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8865\u6d1e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6700\u5927\u6d1e\u957f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u4f18\u5316", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4f18\u5316\u8fb9\u957f", None))
        self.refinehole.setItemText(0, QCoreApplication.translate("Dialog", u"False", None))
        self.refinehole.setItemText(1, QCoreApplication.translate("Dialog", u"True", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
    # retranslateUi

