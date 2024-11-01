# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MulregDialog.ui'
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

class Ui_MulregDialog(object):
    def setupUi(self, MulregDialog):
        if not MulregDialog.objectName():
            MulregDialog.setObjectName(u"MulregDialog")
        MulregDialog.resize(400, 300)
        self.pushButton = QPushButton(MulregDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 230, 75, 24))
        self.verticalLayoutWidget = QWidget(MulregDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 50, 311, 152))
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
        self.iteration.setValue(10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.iteration)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.edge_threshold = QDoubleSpinBox(self.verticalLayoutWidget)
        self.edge_threshold.setObjectName(u"edge_threshold")
        self.edge_threshold.setMaximum(1.000000000000000)
        self.edge_threshold.setSingleStep(0.010000000000000)
        self.edge_threshold.setValue(0.250000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edge_threshold)

        self.preference_loop = QDoubleSpinBox(self.verticalLayoutWidget)
        self.preference_loop.setObjectName(u"preference_loop")
        self.preference_loop.setDecimals(2)
        self.preference_loop.setMaximum(5.000000000000000)
        self.preference_loop.setSingleStep(0.100000000000000)
        self.preference_loop.setValue(1.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.preference_loop)

        self.reference_node = QSpinBox(self.verticalLayoutWidget)
        self.reference_node.setObjectName(u"reference_node")
        self.reference_node.setMinimum(0)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.reference_node)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.voxel)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MulregDialog)
        self.pushButton.clicked.connect(MulregDialog.buttonok)
        self.voxel.valueChanged.connect(MulregDialog.valuechange)

        QMetaObject.connectSlotsByName(MulregDialog)
    # setupUi

    def retranslateUi(self, MulregDialog):
        MulregDialog.setWindowTitle(QCoreApplication.translate("MulregDialog", u"\u591a\u8def\u914d\u51c6", None))
        self.pushButton.setText(QCoreApplication.translate("MulregDialog", u"\u786e\u8ba4", None))
        self.label.setText(QCoreApplication.translate("MulregDialog", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("MulregDialog", u"\u6700\u5927\u8ddd\u79bb", None))
        self.label_3.setText(QCoreApplication.translate("MulregDialog", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.label_4.setText(QCoreApplication.translate("MulregDialog", u"\u5faa\u73af", None))
        self.label_5.setText(QCoreApplication.translate("MulregDialog", u"\u8fb9\u9608\u503c", None))
        self.label_6.setText(QCoreApplication.translate("MulregDialog", u"\u53c2\u8003\u70b9", None))
    # retranslateUi

