# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 807)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionpointcloud = QAction(MainWindow)
        self.actionpointcloud.setObjectName(u"actionpointcloud")
        self.actionBall_pivoting = QAction(MainWindow)
        self.actionBall_pivoting.setObjectName(u"actionBall_pivoting")
        self.actionPoisson = QAction(MainWindow)
        self.actionPoisson.setObjectName(u"actionPoisson")
        self.actionAlpha_shapes = QAction(MainWindow)
        self.actionAlpha_shapes.setObjectName(u"actionAlpha_shapes")
        self.actionICP = QAction(MainWindow)
        self.actionICP.setObjectName(u"actionICP")
        self.actionColored_ICP = QAction(MainWindow)
        self.actionColored_ICP.setObjectName(u"actionColored_ICP")
        self.actionFast_global = QAction(MainWindow)
        self.actionFast_global.setObjectName(u"actionFast_global")
        self.actionMultiway = QAction(MainWindow)
        self.actionMultiway.setObjectName(u"actionMultiway")
        self.actionadd_file = QAction(MainWindow)
        self.actionadd_file.setObjectName(u"actionadd_file")
        self.actionsave_file = QAction(MainWindow)
        self.actionsave_file.setObjectName(u"actionsave_file")
        self.actiondensity = QAction(MainWindow)
        self.actiondensity.setObjectName(u"actiondensity")
        self.actionclear_file = QAction(MainWindow)
        self.actionclear_file.setObjectName(u"actionclear_file")
        self.actionTaubin = QAction(MainWindow)
        self.actionTaubin.setObjectName(u"actionTaubin")
        self.actionLaplacian = QAction(MainWindow)
        self.actionLaplacian.setObjectName(u"actionLaplacian")
        self.actionAverage = QAction(MainWindow)
        self.actionAverage.setObjectName(u"actionAverage")
        self.actionestimate_normals = QAction(MainWindow)
        self.actionestimate_normals.setObjectName(u"actionestimate_normals")
        self.actionvoxel = QAction(MainWindow)
        self.actionvoxel.setObjectName(u"actionvoxel")
        self.actiondownsample_2 = QAction(MainWindow)
        self.actiondownsample_2.setObjectName(u"actiondownsample_2")
        self.actionmerge_points = QAction(MainWindow)
        self.actionmerge_points.setObjectName(u"actionmerge_points")
        self.actionradius = QAction(MainWindow)
        self.actionradius.setObjectName(u"actionradius")
        self.actionstatistical = QAction(MainWindow)
        self.actionstatistical.setObjectName(u"actionstatistical")
        self.actionuniformly = QAction(MainWindow)
        self.actionuniformly.setObjectName(u"actionuniformly")
        self.actionpoisson_disk = QAction(MainWindow)
        self.actionpoisson_disk.setObjectName(u"actionpoisson_disk")
        self.actionclose_holes = QAction(MainWindow)
        self.actionclose_holes.setObjectName(u"actionclose_holes")
        self.actionBall_autoguess = QAction(MainWindow)
        self.actionBall_autoguess.setObjectName(u"actionBall_autoguess")
        self.actionreconstruction5 = QAction(MainWindow)
        self.actionreconstruction5.setObjectName(u"actionreconstruction5")
        self.actionAdd_Volume = QAction(MainWindow)
        self.actionAdd_Volume.setObjectName(u"actionAdd_Volume")
        self.actionAdd_model = QAction(MainWindow)
        self.actionAdd_model.setObjectName(u"actionAdd_model")
        self.actionMulti_Volume = QAction(MainWindow)
        self.actionMulti_Volume.setObjectName(u"actionMulti_Volume")
        self.actionClear_model = QAction(MainWindow)
        self.actionClear_model.setObjectName(u"actionClear_model")
        self.actionClear_Volume = QAction(MainWindow)
        self.actionClear_Volume.setObjectName(u"actionClear_Volume")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonviewfront = QPushButton(self.centralwidget)
        self.pushButtonviewfront.setObjectName(u"pushButtonviewfront")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonviewfront.sizePolicy().hasHeightForWidth())
        self.pushButtonviewfront.setSizePolicy(sizePolicy1)
        self.pushButtonviewfront.setMinimumSize(QSize(75, 0))

        self.horizontalLayout.addWidget(self.pushButtonviewfront)

        self.pushButtonviewup = QPushButton(self.centralwidget)
        self.pushButtonviewup.setObjectName(u"pushButtonviewup")
        sizePolicy1.setHeightForWidth(self.pushButtonviewup.sizePolicy().hasHeightForWidth())
        self.pushButtonviewup.setSizePolicy(sizePolicy1)
        self.pushButtonviewup.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButtonviewup)

        self.pushButtonviewleft = QPushButton(self.centralwidget)
        self.pushButtonviewleft.setObjectName(u"pushButtonviewleft")
        sizePolicy1.setHeightForWidth(self.pushButtonviewleft.sizePolicy().hasHeightForWidth())
        self.pushButtonviewleft.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButtonviewleft)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonviewback = QPushButton(self.centralwidget)
        self.pushButtonviewback.setObjectName(u"pushButtonviewback")
        sizePolicy1.setHeightForWidth(self.pushButtonviewback.sizePolicy().hasHeightForWidth())
        self.pushButtonviewback.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.pushButtonviewback)

        self.pushButtonviewDown = QPushButton(self.centralwidget)
        self.pushButtonviewDown.setObjectName(u"pushButtonviewDown")
        sizePolicy1.setHeightForWidth(self.pushButtonviewDown.sizePolicy().hasHeightForWidth())
        self.pushButtonviewDown.setSizePolicy(sizePolicy1)
        self.pushButtonviewDown.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButtonviewDown)

        self.pushButtonviewright = QPushButton(self.centralwidget)
        self.pushButtonviewright.setObjectName(u"pushButtonviewright")
        sizePolicy1.setHeightForWidth(self.pushButtonviewright.sizePolicy().hasHeightForWidth())
        self.pushButtonviewright.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.pushButtonviewright)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonclipforward = QPushButton(self.centralwidget)
        self.pushButtonclipforward.setObjectName(u"pushButtonclipforward")
        sizePolicy1.setHeightForWidth(self.pushButtonclipforward.sizePolicy().hasHeightForWidth())
        self.pushButtonclipforward.setSizePolicy(sizePolicy1)
        self.pushButtonclipforward.setAutoRepeat(True)
        self.pushButtonclipforward.setAutoRepeatDelay(300)
        self.pushButtonclipforward.setAutoRepeatInterval(1)

        self.horizontalLayout_3.addWidget(self.pushButtonclipforward)

        self.pushButtonclipbackoff = QPushButton(self.centralwidget)
        self.pushButtonclipbackoff.setObjectName(u"pushButtonclipbackoff")
        sizePolicy1.setHeightForWidth(self.pushButtonclipbackoff.sizePolicy().hasHeightForWidth())
        self.pushButtonclipbackoff.setSizePolicy(sizePolicy1)
        self.pushButtonclipbackoff.setAutoRepeat(True)
        self.pushButtonclipbackoff.setAutoRepeatDelay(300)
        self.pushButtonclipbackoff.setAutoRepeatInterval(1)

        self.horizontalLayout_3.addWidget(self.pushButtonclipbackoff)

        self.pushButtonclipreset = QPushButton(self.centralwidget)
        self.pushButtonclipreset.setObjectName(u"pushButtonclipreset")
        sizePolicy1.setHeightForWidth(self.pushButtonclipreset.sizePolicy().hasHeightForWidth())
        self.pushButtonclipreset.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.pushButtonclipreset)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setAutoRepeatInterval(1)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoRepeatInterval(1)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setAutoRepeat(True)
        self.pushButton_5.setAutoRepeatInterval(1)

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setAutoRepeat(True)
        self.pushButton_4.setAutoRepeatInterval(1)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.doubleSpinBoxZeroAlpha = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxZeroAlpha.setObjectName(u"doubleSpinBoxZeroAlpha")
        self.doubleSpinBoxZeroAlpha.setDecimals(4)
        self.doubleSpinBoxZeroAlpha.setMaximum(1.000000000000000)
        self.doubleSpinBoxZeroAlpha.setSingleStep(0.001000000000000)
        self.doubleSpinBoxZeroAlpha.setValue(0.000500000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBoxZeroAlpha)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.doubleSpinBoxLowalpha = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxLowalpha.setObjectName(u"doubleSpinBoxLowalpha")
        self.doubleSpinBoxLowalpha.setDecimals(4)
        self.doubleSpinBoxLowalpha.setMaximum(1.000000000000000)
        self.doubleSpinBoxLowalpha.setSingleStep(0.001000000000000)
        self.doubleSpinBoxLowalpha.setValue(0.000500000000000)

        self.horizontalLayout_7.addWidget(self.doubleSpinBoxLowalpha)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.doubleSpinBoxHighAlpha = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxHighAlpha.setObjectName(u"doubleSpinBoxHighAlpha")
        self.doubleSpinBoxHighAlpha.setDecimals(4)
        self.doubleSpinBoxHighAlpha.setMaximum(1.000000000000000)
        self.doubleSpinBoxHighAlpha.setSingleStep(0.001000000000000)
        self.doubleSpinBoxHighAlpha.setValue(0.100000000000000)

        self.horizontalLayout_8.addWidget(self.doubleSpinBoxHighAlpha)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.doubleSpinBox0_gradientAlpha = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox0_gradientAlpha.setObjectName(u"doubleSpinBox0_gradientAlpha")
        self.doubleSpinBox0_gradientAlpha.setDecimals(4)
        self.doubleSpinBox0_gradientAlpha.setMaximum(5.000000000000000)
        self.doubleSpinBox0_gradientAlpha.setSingleStep(0.001000000000000)
        self.doubleSpinBox0_gradientAlpha.setValue(0.100000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBox0_gradientAlpha)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.doubleSpinBox05_gradientAlpha = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox05_gradientAlpha.setObjectName(u"doubleSpinBox05_gradientAlpha")
        self.doubleSpinBox05_gradientAlpha.setDecimals(4)
        self.doubleSpinBox05_gradientAlpha.setMaximum(5.000000000000000)
        self.doubleSpinBox05_gradientAlpha.setSingleStep(0.001000000000000)
        self.doubleSpinBox05_gradientAlpha.setValue(0.500000000000000)

        self.horizontalLayout_12.addWidget(self.doubleSpinBox05_gradientAlpha)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.doubleSpinBox1_gradientAlpha = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox1_gradientAlpha.setObjectName(u"doubleSpinBox1_gradientAlpha")
        self.doubleSpinBox1_gradientAlpha.setDecimals(4)
        self.doubleSpinBox1_gradientAlpha.setMaximum(5.000000000000000)
        self.doubleSpinBox1_gradientAlpha.setSingleStep(0.001000000000000)
        self.doubleSpinBox1_gradientAlpha.setValue(1.000000000000000)

        self.horizontalLayout_13.addWidget(self.doubleSpinBox1_gradientAlpha)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.radioButtonColorReverse = QRadioButton(self.centralwidget)
        self.radioButtonColorReverse.setObjectName(u"radioButtonColorReverse")
        sizePolicy1.setHeightForWidth(self.radioButtonColorReverse.sizePolicy().hasHeightForWidth())
        self.radioButtonColorReverse.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.radioButtonColorReverse)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_9.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.doubleSpinBoxAnimationTime = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxAnimationTime.setObjectName(u"doubleSpinBoxAnimationTime")
        sizePolicy1.setHeightForWidth(self.doubleSpinBoxAnimationTime.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxAnimationTime.setSizePolicy(sizePolicy1)
        self.doubleSpinBoxAnimationTime.setDecimals(1)

        self.horizontalLayout_10.addWidget(self.doubleSpinBoxAnimationTime)

        self.pushButtonAnimationStart = QPushButton(self.centralwidget)
        self.pushButtonAnimationStart.setObjectName(u"pushButtonAnimationStart")
        sizePolicy1.setHeightForWidth(self.pushButtonAnimationStart.sizePolicy().hasHeightForWidth())
        self.pushButtonAnimationStart.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.pushButtonAnimationStart)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.pushButton_3)

        self.pushButtonAnimationEnd = QPushButton(self.centralwidget)
        self.pushButtonAnimationEnd.setObjectName(u"pushButtonAnimationEnd")
        sizePolicy1.setHeightForWidth(self.pushButtonAnimationEnd.sizePolicy().hasHeightForWidth())
        self.pushButtonAnimationEnd.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.pushButtonAnimationEnd)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetMinimumSize)
        self.pathshow = QPushButton(self.centralwidget)
        self.pathshow.setObjectName(u"pathshow")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pathshow.sizePolicy().hasHeightForWidth())
        self.pathshow.setSizePolicy(sizePolicy3)

        self.horizontalLayout_14.addWidget(self.pathshow)

        self.pathcancel = QPushButton(self.centralwidget)
        self.pathcancel.setObjectName(u"pathcancel")
        sizePolicy3.setHeightForWidth(self.pathcancel.sizePolicy().hasHeightForWidth())
        self.pathcancel.setSizePolicy(sizePolicy3)

        self.horizontalLayout_14.addWidget(self.pathcancel)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.airpathid = QSpinBox(self.centralwidget)
        self.airpathid.setObjectName(u"airpathid")
        sizePolicy3.setHeightForWidth(self.airpathid.sizePolicy().hasHeightForWidth())
        self.airpathid.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.airpathid)

        self.coordposition = QPushButton(self.centralwidget)
        self.coordposition.setObjectName(u"coordposition")
        sizePolicy3.setHeightForWidth(self.coordposition.sizePolicy().hasHeightForWidth())
        self.coordposition.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.coordposition)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label24 = QLabel(self.centralwidget)
        self.label24.setObjectName(u"label24")
        sizePolicy.setHeightForWidth(self.label24.sizePolicy().hasHeightForWidth())
        self.label24.setSizePolicy(sizePolicy)
        self.label24.setMinimumSize(QSize(24, 0))

        self.horizontalLayout_16.addWidget(self.label24, 0, Qt.AlignLeft)

        self.coordlabel = QLabel(self.centralwidget)
        self.coordlabel.setObjectName(u"coordlabel")
        sizePolicy.setHeightForWidth(self.coordlabel.sizePolicy().hasHeightForWidth())
        self.coordlabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.coordlabel)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(24, 0))
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_17, 0, Qt.AlignLeft)

        self.positionlable = QLabel(self.centralwidget)
        self.positionlable.setObjectName(u"positionlable")
        sizePolicy.setHeightForWidth(self.positionlable.sizePolicy().hasHeightForWidth())
        self.positionlable.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.positionlable)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.verticalLayout.addLayout(self.horizontalLayout_18)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 988, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menuregister = QMenu(self.menubar)
        self.menuregister.setObjectName(u"menuregister")
        self.menuReconstruction = QMenu(self.menubar)
        self.menuReconstruction.setObjectName(u"menuReconstruction")
        self.menuCluster = QMenu(self.menubar)
        self.menuCluster.setObjectName(u"menuCluster")
        self.menuMesh_Filter = QMenu(self.menubar)
        self.menuMesh_Filter.setObjectName(u"menuMesh_Filter")
        self.menuProcess = QMenu(self.menubar)
        self.menuProcess.setObjectName(u"menuProcess")
        self.menuremove_outliner = QMenu(self.menuProcess)
        self.menuremove_outliner.setObjectName(u"menuremove_outliner")
        self.menuMesh_Sample = QMenu(self.menubar)
        self.menuMesh_Sample.setObjectName(u"menuMesh_Sample")
        self.menuMesh_Repair = QMenu(self.menubar)
        self.menuMesh_Repair.setObjectName(u"menuMesh_Repair")
        self.menuVolume_Render = QMenu(self.menubar)
        self.menuVolume_Render.setObjectName(u"menuVolume_Render")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.BottomToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuregister.menuAction())
        self.menubar.addAction(self.menuReconstruction.menuAction())
        self.menubar.addAction(self.menuCluster.menuAction())
        self.menubar.addAction(self.menuMesh_Filter.menuAction())
        self.menubar.addAction(self.menuMesh_Sample.menuAction())
        self.menubar.addAction(self.menuMesh_Repair.menuAction())
        self.menubar.addAction(self.menuVolume_Render.menuAction())
        self.menu.addAction(self.actionpointcloud)
        self.menu.addAction(self.actionadd_file)
        self.menu.addAction(self.actionsave_file)
        self.menu.addAction(self.actionclear_file)
        self.menuregister.addAction(self.actionFast_global)
        self.menuregister.addAction(self.actionICP)
        self.menuregister.addAction(self.actionColored_ICP)
        self.menuregister.addAction(self.actionMultiway)
        self.menuReconstruction.addAction(self.actionBall_pivoting)
        self.menuReconstruction.addAction(self.actionPoisson)
        self.menuReconstruction.addAction(self.actionBall_autoguess)
        self.menuReconstruction.addAction(self.actionreconstruction5)
        self.menuCluster.addAction(self.actiondensity)
        self.menuMesh_Filter.addAction(self.actionTaubin)
        self.menuMesh_Filter.addAction(self.actionLaplacian)
        self.menuMesh_Filter.addAction(self.actionAverage)
        self.menuProcess.addAction(self.actiondownsample_2)
        self.menuProcess.addAction(self.actionestimate_normals)
        self.menuProcess.addAction(self.actionmerge_points)
        self.menuProcess.addAction(self.menuremove_outliner.menuAction())
        self.menuremove_outliner.addAction(self.actionradius)
        self.menuremove_outliner.addAction(self.actionstatistical)
        self.menuMesh_Sample.addAction(self.actionuniformly)
        self.menuMesh_Sample.addAction(self.actionpoisson_disk)
        self.menuMesh_Repair.addAction(self.actionclose_holes)
        self.menuVolume_Render.addAction(self.actionAdd_model)
        self.menuVolume_Render.addAction(self.actionMulti_Volume)
        self.menuVolume_Render.addAction(self.actionClear_model)
        self.menuVolume_Render.addAction(self.actionClear_Volume)

        self.retranslateUi(MainWindow)
        self.actionpointcloud.triggered.connect(MainWindow.choosefile)
        self.actionBall_pivoting.triggered.connect(MainWindow.Configball)
        self.actionadd_file.triggered.connect(MainWindow.addfile)
        self.actionFast_global.triggered.connect(MainWindow.configFastreg)
        self.actionColored_ICP.triggered.connect(MainWindow.configColorreg)
        self.actionICP.triggered.connect(MainWindow.configICPreg)
        self.actionMultiway.triggered.connect(MainWindow.configMulreg)
        self.actionsave_file.triggered.connect(MainWindow.savefile)
        self.actionAlpha_shapes.triggered.connect(MainWindow.configAlpha)
        self.actionPoisson.triggered.connect(MainWindow.configPossion)
        self.actiondensity.triggered.connect(MainWindow.configDensitycluster)
        self.actionclear_file.triggered.connect(MainWindow.clearfile)
        self.actionLaplacian.triggered.connect(MainWindow.configLaplacian)
        self.actionTaubin.triggered.connect(MainWindow.configTaubin)
        self.actionAverage.triggered.connect(MainWindow.configAverage)
        self.actionestimate_normals.triggered.connect(MainWindow.configNormal)
        self.actiondownsample_2.triggered.connect(MainWindow.configDownsample)
        self.actionmerge_points.triggered.connect(MainWindow.mergepoint)
        self.actionradius.triggered.connect(MainWindow.configradius_outliers)
        self.actionstatistical.triggered.connect(MainWindow.configstatistical_outliers)
        self.actionpoisson_disk.triggered.connect(MainWindow.configpoisson_disk)
        self.actionuniformly.triggered.connect(MainWindow.configuniformly)
        self.actionclose_holes.triggered.connect(MainWindow.configcloseholes)
        self.actionBall_autoguess.triggered.connect(MainWindow.configballautoguess)
        self.actionreconstruction5.triggered.connect(MainWindow.configconvmesh)
        self.actionAdd_Volume.triggered.connect(MainWindow.addvolumefile)
        self.actionAdd_model.triggered.connect(MainWindow.VolumeAddmodelfile)
        self.actionMulti_Volume.triggered.connect(MainWindow.MulVolumefile)
        self.pushButtonviewup.clicked.connect(MainWindow.viewup)
        self.pushButtonviewfront.clicked.connect(MainWindow.viewfront)
        self.pushButtonviewleft.clicked.connect(MainWindow.viewleft)
        self.pushButtonviewDown.clicked.connect(MainWindow.viewdown)
        self.pushButtonviewright.clicked.connect(MainWindow.viewright)
        self.pushButtonviewback.clicked.connect(MainWindow.viewback)
        self.pushButtonclipforward.pressed.connect(MainWindow.clipforward)
        self.pushButtonclipbackoff.pressed.connect(MainWindow.clipbackoff)
        self.pushButtonclipreset.clicked.connect(MainWindow.clipreset)
        self.pushButton_2.pressed.connect(MainWindow.clipfastforward)
        self.pushButton.pressed.connect(MainWindow.clipfastbackoff)
        self.pushButton_5.pressed.connect(MainWindow.cameramovefront)
        self.pushButton_4.clicked.connect(MainWindow.cameramoveback)
        self.doubleSpinBoxZeroAlpha.valueChanged.connect(MainWindow.changeAlpha)
        self.doubleSpinBoxLowalpha.valueChanged.connect(MainWindow.changeAlpha)
        self.doubleSpinBoxHighAlpha.valueChanged.connect(MainWindow.changeAlpha)
        self.comboBox.currentTextChanged.connect(MainWindow.changeColorBar)
        self.pushButtonAnimationStart.clicked.connect(MainWindow.AnimationStart)
        self.pushButtonAnimationEnd.clicked.connect(MainWindow.AnimationEnd)
        self.pushButton_3.clicked.connect(MainWindow.AnimationStop)
        self.radioButtonColorReverse.clicked.connect(MainWindow.ColorReverse)
        self.doubleSpinBox0_gradientAlpha.valueChanged.connect(MainWindow.changegradientAlpha)
        self.doubleSpinBox05_gradientAlpha.valueChanged.connect(MainWindow.changegradientAlpha)
        self.doubleSpinBox05_gradientAlpha.valueChanged.connect(MainWindow.changegradientAlpha)
        self.doubleSpinBox1_gradientAlpha.valueChanged.connect(MainWindow.changegradientAlpha)
        self.actionClear_model.triggered.connect(MainWindow.vtkClearmodel)
        self.actionClear_Volume.triggered.connect(MainWindow.vtkClearvolume)
        self.pathshow.clicked.connect(MainWindow.pathShow)
        self.pathcancel.clicked.connect(MainWindow.pathCancel)
        self.coordposition.clicked.connect(MainWindow.showCoord)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionpointcloud.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.actionBall_pivoting.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u578b\u5f00\u66f2\u9762", None))
        self.actionPoisson.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u578b\u95ed\u66f2\u9762", None))
        self.actionAlpha_shapes.setText(QCoreApplication.translate("MainWindow", u"reconstruction3", None))
        self.actionICP.setText(QCoreApplication.translate("MainWindow", u"\u5c40\u90e8\u914d\u51c6", None))
        self.actionColored_ICP.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272\u5c40\u90e8\u914d\u51c6", None))
        self.actionFast_global.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u5168\u5c40\u914d\u51c6", None))
        self.actionMultiway.setText(QCoreApplication.translate("MainWindow", u"\u591a\u8def\u914d\u51c6", None))
        self.actionadd_file.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.actionsave_file.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.actiondensity.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u5ea6", None))
        self.actionclear_file.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6587\u4ef6", None))
        self.actionTaubin.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u6ed1", None))
        self.actionLaplacian.setText(QCoreApplication.translate("MainWindow", u"\u516c\u5f0f\u5e73\u6ed1", None))
        self.actionAverage.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u5e73\u6ed1", None))
        self.actionestimate_normals.setText(QCoreApplication.translate("MainWindow", u"\u4f30\u8ba1\u6cd5\u5411\u91cf", None))
        self.actionvoxel.setText(QCoreApplication.translate("MainWindow", u"voxel", None))
        self.actiondownsample_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u91c7\u6837", None))
        self.actionmerge_points.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u70b9\u4e91", None))
        self.actionradius.setText(QCoreApplication.translate("MainWindow", u"\u534a\u5f84\u79fb\u9664\u6cd5", None))
        self.actionstatistical.setText(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1\u79fb\u9664\u6cd5", None))
        self.actionuniformly.setText(QCoreApplication.translate("MainWindow", u"\u5747\u5300\u91c7\u6837", None))
        self.actionpoisson_disk.setText(QCoreApplication.translate("MainWindow", u"\u5706\u76d8\u91c7\u6837", None))
        self.actionclose_holes.setText(QCoreApplication.translate("MainWindow", u"\u8865\u6d1e", None))
        self.actionBall_autoguess.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u578b\u5f00\u66f2\u9762", None))
        self.actionreconstruction5.setText(QCoreApplication.translate("MainWindow", u"\u5927\u578b\u901a\u7528", None))
        self.actionAdd_Volume.setText(QCoreApplication.translate("MainWindow", u"Add Volume", None))
        self.actionAdd_model.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6a21\u578b", None))
        self.actionMulti_Volume.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6570\u636e", None))
        self.actionClear_model.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6a21\u578b", None))
        self.actionClear_Volume.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u695a\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u5411\u89c6\u56fe", None))
        self.pushButtonviewfront.setText(QCoreApplication.translate("MainWindow", u"\u524d", None))
        self.pushButtonviewup.setText(QCoreApplication.translate("MainWindow", u"\u4e0a", None))
        self.pushButtonviewleft.setText(QCoreApplication.translate("MainWindow", u"\u5de6", None))
        self.pushButtonviewback.setText(QCoreApplication.translate("MainWindow", u"\u540e", None))
        self.pushButtonviewDown.setText(QCoreApplication.translate("MainWindow", u"\u4e0b", None))
        self.pushButtonviewright.setText(QCoreApplication.translate("MainWindow", u"\u53f3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u8303\u56f4", None))
        self.pushButtonclipforward.setText(QCoreApplication.translate("MainWindow", u"\u524d\u63a8", None))
        self.pushButtonclipbackoff.setText(QCoreApplication.translate("MainWindow", u"\u540e\u62c9", None))
        self.pushButtonclipreset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u524d\u63a8", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u8bfb\u540e\u62c9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u4f4d\u7f6e", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u524d\u79fb", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u540e\u79fb", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u89c6\u5316", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0\u503c\u4e0d\u900f\u660e\u5ea6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u4e0d\u900f\u660e\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u4e0d\u900f\u660e\u5ea6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0\u503c\u4e0d\u900f\u660e\u68af\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u4e0d\u900f\u660e\u68af\u5ea6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"1\u503c\u4e0d\u900f\u660e\u68af\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.radioButtonColorReverse.setText(QCoreApplication.translate("MainWindow", u"\u9006\u8f6c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"jet", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"rainbow", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"turbo", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"hsv", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"hot", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"spring", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"summer", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"autumn", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"winter", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"viridis", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u753b", None))
        self.pushButtonAnimationStart.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c", None))
        self.pushButtonAnimationEnd.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u98de\u884c\u8def\u5f84\u663e\u793a", None))
        self.pathshow.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.pathcancel.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u98de\u673a\u4f4d\u7f6e\u4e0e\u59ff\u6001", None))
        self.coordposition.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.label24.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None))
        self.coordlabel.setText(QCoreApplication.translate("MainWindow", u"x\uff1a0  y\uff1a0  z:0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u59ff\u6001", None))
        self.positionlable.setText(QCoreApplication.translate("MainWindow", u"x   y   z", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuregister.setTitle(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u914d\u51c6", None))
        self.menuReconstruction.setTitle(QCoreApplication.translate("MainWindow", u"\u91cd\u5efa", None))
        self.menuCluster.setTitle(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u805a\u7c7b", None))
        self.menuMesh_Filter.setTitle(QCoreApplication.translate("MainWindow", u"\u7f51\u683c\u4f18\u5316", None))
        self.menuProcess.setTitle(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u5904\u7406", None))
        self.menuremove_outliner.setTitle(QCoreApplication.translate("MainWindow", u"\u79fb\u9664\u79bb\u7fa4\u70b9", None))
        self.menuMesh_Sample.setTitle(QCoreApplication.translate("MainWindow", u"\u7f51\u683c\u91c7\u6837", None))
        self.menuMesh_Repair.setTitle(QCoreApplication.translate("MainWindow", u"\u7f51\u683c\u4fee\u590d", None))
        self.menuVolume_Render.setTitle(QCoreApplication.translate("MainWindow", u"\u4f53\u6e32\u67d3", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

