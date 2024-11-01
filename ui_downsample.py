# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downsample.ui'
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
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_downsample(object):
    def setupUi(self, downsample):
        if not downsample.objectName():
            downsample.setObjectName(u"downsample")
        downsample.resize(400, 300)
        self.pushButton = QPushButton(downsample)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 190, 75, 24))
        self.verticalLayoutWidget = QWidget(downsample)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 80, 311, 22))
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

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(downsample)
        self.pushButton.clicked.connect(downsample.buttonok)

        QMetaObject.connectSlotsByName(downsample)
    # setupUi

    def retranslateUi(self, downsample):
        downsample.setWindowTitle(QCoreApplication.translate("downsample", u"\u4e0b\u91c7\u6837", None))
        self.pushButton.setText(QCoreApplication.translate("downsample", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("downsample", u"\u4f53\u7d20\u5927\u5c0f", None))
    # retranslateUi

