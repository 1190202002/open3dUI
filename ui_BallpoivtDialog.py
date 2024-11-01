# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BallpoivtDialog.ui'
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

class Ui_ballpiovtingConfig(object):
    def setupUi(self, ballpiovtingConfig):
        if not ballpiovtingConfig.objectName():
            ballpiovtingConfig.setObjectName(u"ballpiovtingConfig")
        ballpiovtingConfig.resize(390, 282)
        self.verticalLayoutWidget = QWidget(ballpiovtingConfig)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 311, 204))
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

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.r1 = QDoubleSpinBox(self.verticalLayoutWidget)
        self.r1.setObjectName(u"r1")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.r1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.r2 = QDoubleSpinBox(self.verticalLayoutWidget)
        self.r2.setObjectName(u"r2")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.r2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.r3 = QDoubleSpinBox(self.verticalLayoutWidget)
        self.r3.setObjectName(u"r3")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.r3)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.r4 = QDoubleSpinBox(self.verticalLayoutWidget)
        self.r4.setObjectName(u"r4")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.r4)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.normaln = QSpinBox(self.verticalLayoutWidget)
        self.normaln.setObjectName(u"normaln")
        self.normaln.setValue(30)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.normaln)

        self.orientk = QSpinBox(self.verticalLayoutWidget)
        self.orientk.setObjectName(u"orientk")
        self.orientk.setMaximum(999)
        self.orientk.setValue(100)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.orientk)

        self.normalr = QDoubleSpinBox(self.verticalLayoutWidget)
        self.normalr.setObjectName(u"normalr")
        self.normalr.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.normalr)

        self.pushButton = QPushButton(ballpiovtingConfig)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 250, 75, 24))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ballpiovtingConfig)
        self.pushButton.clicked.connect(ballpiovtingConfig.buttonok)

        QMetaObject.connectSlotsByName(ballpiovtingConfig)
    # setupUi

    def retranslateUi(self, ballpiovtingConfig):
        ballpiovtingConfig.setWindowTitle(QCoreApplication.translate("ballpiovtingConfig", u"\u5c0f\u578b\u5f00\u66f2\u9762\u91cd\u5efa", None))
        self.label.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u534a\u5f841", None))
        self.label_3.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u534a\u5f842", None))
        self.label_4.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u534a\u5f843", None))
        self.label_5.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u534a\u5f844", None))
        self.label_6.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u534a\u5f84", None))
        self.label_7.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u91c7\u6837\u70b9", None))
        self.label_8.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u5b9a\u5411\u70b9", None))
        self.pushButton.setText(QCoreApplication.translate("ballpiovtingConfig", u"\u786e\u8ba4", None))
    # retranslateUi

