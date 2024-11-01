# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FastregDialog.ui'
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
        Dialog.resize(387, 299)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 250, 75, 24))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 311, 81))
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

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.correspondence_distance = QDoubleSpinBox(self.verticalLayoutWidget)
        self.correspondence_distance.setObjectName(u"correspondence_distance")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.correspondence_distance)

        self.iteration = QSpinBox(self.verticalLayoutWidget)
        self.iteration.setObjectName(u"iteration")
        self.iteration.setMaximum(999)
        self.iteration.setValue(64)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.iteration)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.buttonok)
        self.voxel.valueChanged.connect(Dialog.valuechange)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5feb\u901f\u5168\u5c40\u914d\u51c6", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6700\u5927\u8ddd\u79bb", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8fed\u4ee3\u6b21\u6570", None))
    # retranslateUi

