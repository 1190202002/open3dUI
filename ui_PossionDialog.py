# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PossionDialog.ui'
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

class Ui_PossionDialog(object):
    def setupUi(self, PossionDialog):
        if not PossionDialog.objectName():
            PossionDialog.setObjectName(u"PossionDialog")
        PossionDialog.resize(428, 324)
        self.pushButton = QPushButton(PossionDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 280, 75, 24))
        self.verticalLayoutWidget = QWidget(PossionDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 341, 231))
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
        self.normalr.setWrapping(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.normalr)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.normaln = QSpinBox(self.verticalLayoutWidget)
        self.normaln.setObjectName(u"normaln")
        self.normaln.setMaximum(999)
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

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.depth = QSpinBox(self.verticalLayoutWidget)
        self.depth.setObjectName(u"depth")
        self.depth.setMinimum(1)
        self.depth.setMaximum(15)
        self.depth.setValue(8)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.depth)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.width = QDoubleSpinBox(self.verticalLayoutWidget)
        self.width.setObjectName(u"width")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.width)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.scale = QDoubleSpinBox(self.verticalLayoutWidget)
        self.scale.setObjectName(u"scale")
        self.scale.setValue(1.100000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.scale)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.comboBox)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)

        self.nthreads = QSpinBox(self.verticalLayoutWidget)
        self.nthreads.setObjectName(u"nthreads")
        self.nthreads.setMinimum(-1)
        self.nthreads.setMaximum(16)
        self.nthreads.setValue(-1)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.nthreads)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(PossionDialog)
        self.pushButton.clicked.connect(PossionDialog.buttonok)

        QMetaObject.connectSlotsByName(PossionDialog)
    # setupUi

    def retranslateUi(self, PossionDialog):
        PossionDialog.setWindowTitle(QCoreApplication.translate("PossionDialog", u"\u5c0f\u578b\u95ed\u66f2\u9762\u91cd\u5efa", None))
        self.pushButton.setText(QCoreApplication.translate("PossionDialog", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("PossionDialog", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.label_6.setText(QCoreApplication.translate("PossionDialog", u"\u534a\u5f84", None))
        self.label_7.setText(QCoreApplication.translate("PossionDialog", u"\u91c7\u6837\u70b9", None))
        self.label_8.setText(QCoreApplication.translate("PossionDialog", u"\u5b9a\u5411\u70b9", None))
        self.label_2.setText(QCoreApplication.translate("PossionDialog", u"\u6df1\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("PossionDialog", u"\u5bbd\u5ea6", None))
        self.label_4.setText(QCoreApplication.translate("PossionDialog", u"\u653e\u7f29\u56e0\u5b50", None))
        self.label_5.setText(QCoreApplication.translate("PossionDialog", u"\u7ebf\u6027\u62df\u5408", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("PossionDialog", u"False", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("PossionDialog", u"True", None))

        self.label_9.setText(QCoreApplication.translate("PossionDialog", u"\u7ebf\u7a0b\u6570", None))
    # retranslateUi

