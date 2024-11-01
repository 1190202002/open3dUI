# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removestaticoutlinerDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(75, 59, 271, 51))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nb_neighbors = QSpinBox(self.formLayoutWidget)
        self.nb_neighbors.setObjectName(u"nb_neighbors")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nb_neighbors)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.std_ratio = QDoubleSpinBox(self.formLayoutWidget)
        self.std_ratio.setObjectName(u"std_ratio")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.std_ratio)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 220, 75, 24))

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.buttonok)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u79fb\u9664\u7edf\u8ba1\u79bb\u7fa4\u70b9", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u90bb\u8fd1\u70b9\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6807\u51c6\u5dee", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
    # retranslateUi

