# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ballautoguessDialog.ui'
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
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 250, 75, 24))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 311, 161))
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

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.normalr = QDoubleSpinBox(self.verticalLayoutWidget)
        self.normalr.setObjectName(u"normalr")
        self.normalr.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.normalr)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.normaln = QSpinBox(self.verticalLayoutWidget)
        self.normaln.setObjectName(u"normaln")
        self.normaln.setValue(30)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.normaln)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.orientk = QSpinBox(self.verticalLayoutWidget)
        self.orientk.setObjectName(u"orientk")
        self.orientk.setMaximum(999)
        self.orientk.setValue(100)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.orientk)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.clustering = QDoubleSpinBox(self.verticalLayoutWidget)
        self.clustering.setObjectName(u"clustering")
        self.clustering.setValue(20.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.clustering)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_2)

        self.creasethr = QDoubleSpinBox(self.verticalLayoutWidget)
        self.creasethr.setObjectName(u"creasethr")
        self.creasethr.setValue(90.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.creasethr)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.buttonok)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5c0f\u578b\u5f00\u66f2\u9762\u91cd\u5efa", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u534a\u5f84", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u91c7\u6837\u70b9", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u5b9a\u5411\u70b9", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u9608\u503c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u89d2\u5ea6", None))
    # retranslateUi

