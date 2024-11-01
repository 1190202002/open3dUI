# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Average.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Average(object):
    def setupUi(self, Average):
        if not Average.objectName():
            Average.setObjectName(u"Average")
        Average.resize(400, 300)
        self.pushButton = QPushButton(Average)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 220, 75, 24))
        self.formLayoutWidget = QWidget(Average)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(80, 50, 281, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.iterations = QSpinBox(self.formLayoutWidget)
        self.iterations.setObjectName(u"iterations")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.iterations)


        self.retranslateUi(Average)

        QMetaObject.connectSlotsByName(Average)
    # setupUi

    def retranslateUi(self, Average):
        Average.setWindowTitle(QCoreApplication.translate("Average", u"\u5e73\u5747\u5e73\u6ed1", None))
        self.pushButton.setText(QCoreApplication.translate("Average", u"\u786e\u5b9a", None))
        self.label.setText(QCoreApplication.translate("Average", u"\u8fed\u4ee3\u6b21\u6570", None))
    # retranslateUi

