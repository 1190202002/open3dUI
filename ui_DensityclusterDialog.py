# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DensityclusterDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_DensityclusterDialog(object):
    def setupUi(self, DensityclusterDialog):
        if not DensityclusterDialog.objectName():
            DensityclusterDialog.setObjectName(u"DensityclusterDialog")
        DensityclusterDialog.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(DensityclusterDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(120, 60, 181, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.pushButton = QPushButton(DensityclusterDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 240, 75, 24))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.doubleSpinBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DensityclusterDialog)
        self.pushButton.clicked.connect(DensityclusterDialog.buttonok)

        QMetaObject.connectSlotsByName(DensityclusterDialog)
    # setupUi

    def retranslateUi(self, DensityclusterDialog):
        DensityclusterDialog.setWindowTitle(QCoreApplication.translate("DensityclusterDialog", u"\u5bc6\u5ea6", None))
        self.label.setText(QCoreApplication.translate("DensityclusterDialog", u"\u4f53\u7d20\u5927\u5c0f", None))
        self.pushButton.setText(QCoreApplication.translate("DensityclusterDialog", u"\u786e\u8ba4", None))
    # retranslateUi

