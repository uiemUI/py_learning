# -*- coding:utf-8  -*-
# author: zhuchuang time:2020/1/2


import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from GUI import Ui_MainWindow
from sub_main import secondwindow


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    emit_image_signal = pyqtSignal(QImage)  # 创建pyqt信号，指定传递的变量类型为QImage


def __init__(self):
    super(mywindow, self).__init__()
    self.setupUi(self)

    self.second_window = secondwindow()  # 实例化子界面

    self.one_pushButton.clicked.connect(pushbutton_fuction)
    self.emit_image_signal.connect(self.second_window.show_label)  # 将pyqt信号连接到
    # 子窗口的show_label()函数


def pushbutton_fuction(self):
    Im = cv2.imread('***.jpg')  # 通过Opencv读入一张图片
    image_height, image_width, image_depth = Im.shape  # 获取图像的高，宽以及深度。
    QIm = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
    QIm = QImage(QIm.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                 image_width * image_depth,
                 QImage.Format_RGB888)
    self.second_window.show()  # 弹出子窗口
    self.emit_image_signal.emit(QIm)  # 释放pyqt信号


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
