# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opencv_qt_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):  #并不创建窗体Mainwindow，Mainwindow作为参数由外部传入
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 556)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sdu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setObjectName("input_line")
        self.horizontalLayout_2.addWidget(self.input_line)
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_2.addWidget(self.open_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 5)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 4, 1, 3, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(602, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.open_camer = QtWidgets.QPushButton(self.centralwidget)
        self.open_camer.setObjectName("open_camer")
        self.horizontalLayout.addWidget(self.open_camer)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.open_button.clicked.connect(MainWindow.open_dir)
        self.pushButton.clicked.connect(MainWindow.show_image)
        self.open_camer.pressed.connect(MainWindow.open_camewr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸检测"))
        self.label.setText(_translate("MainWindow", "input image: "))
        self.open_button.setText(_translate("MainWindow", "选择图片"))
        self.open_camer.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton.setText(_translate("MainWindow", "打开图片"))
