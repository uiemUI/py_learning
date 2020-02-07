# -*- coding:utf-8  -*-
# author: zhuchuang time:2020/1/2

from opencv_qt_ui import *
import copy
import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget, QMainWindow, QApplication
from PyQt5.QtGui import *

import numpy as np


def cv_imread(file_path, flag=-1):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), flag)

    return cv_img


# cvMat与qimage转换


def cv2qimage(cv_img):
    shape = cv_img.shape
    # image_height, image_width, image_depth = image.shape,列表
    if shape[2] == 4:

        qimg = QImage(cv_img.data, shape[1], shape[0], shape[1] * 4,
                      QImage.Format_ARGB32)
        return qimg

    elif shape[2] == 3:

        qimg = QImage(cv_img.data, shape[1], shape[0], shape[1] * 3,
                      QImage.Format_RGB888)
        return qimg.rgbSwapped()
    elif shape[2] == 1:
        qimg = QImage(cv_img.data, shape[1], shape[0], shape[1] * 1, QImage.Format_Grayscale8)
        return qimg
    else:
        raise Exception("image channels must be 1 3 4")


class MyMainWindow(QMainWindow):  # 单继承方法，父类是QMainwindow
    def __init__(self, parent=None):
        # super(MyMainWindow, self).__init__(parent)
        super().__init__(parent)
        self.ui = Ui_MainWindow()   # self.ui是一个MyMainWindow的共有属性，私有属性改成self.__ui=Ui_MainWindow()
        self.ui.setupUi(self)  # self是QMainWindow窗口，作为参数传给Ui_MainWindow的setupUI(),QMainWindow作为了各组件的容器
        self.loadSwttings()
        # self.setWindowIcon(QIcon('sdu.ico'))
        self.faceDEtector = cv2.CascadeClassifier()
        self.faceDEtector.load('haarcascade_frontalface_alt.xml')

    def show_image(self):
        self.flag = 1
        Frame = copy.deepcopy(self.image)
        gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
        eq_image = cv2.equalizeHist(gray)
        flags = cv2.CASCADE_FIND_BIGGEST_OBJECT | cv2.CASCADE_DO_ROUGH_SEARCH
        faces = self.faceDEtector.detectMultiScale(eq_image, 1.1, 4, flags)
        if len(faces) > 0:
            for faceRect in faces:
                x, y, w, h = faceRect
                cv2.rectangle(Frame, (x - 10, y - 10), (x + w, y + h), (0, 255, 0))
        self.show_camer(Frame)

    def show_camer(self, frame):

        Qim = cv2qimage(frame)
        self.ui.label_2.setPixmap(QPixmap.fromImage(Qim))

    def open_dir(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'open image', QtCore.QDir.currentPath(), 'image (*.jpg\
                 *.png *.bmp)')

        # print(fileName.encode('utf-8').decode('gbk'))
        if QtCore.QFile.exists(fileName):
            self.ui.input_line.setText(fileName)
            print(type(fileName))
            self.image = cv_imread(self.ui.input_line.text())

    def open_camewr(self):

        self.flag = 0
        self.camera = cv2.VideoCapture(0)
        while self.isVisible():  # 窗口未关闭时
            ret, Frame = self.camera.read()
            gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
            eq_image = cv2.equalizeHist(gray)
            flags = cv2.CASCADE_FIND_BIGGEST_OBJECT | cv2.CASCADE_DO_ROUGH_SEARCH
            faces = self.faceDEtector.detectMultiScale(eq_image, 1.1, 4, flags)
            if len(faces) > 0:
                for faceRect in faces:
                    x, y, w, h = faceRect
                    cv2.rectangle(Frame, (x - 10, y - 10), (x + w, y + h), (0, 255, 0))
            cv2.flip(Frame, 1, Frame)

            self.show_camer(Frame)
            cv2.waitKey(1)
            # if (c&0xFF==ord('q'))or self.flag==1:
            if self.flag == 1:
                break

        self.camera.release()

    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.warning(self, 'Exit',
                                               'Are you sure you want to close this program?',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            # self.camera.release()
            self.saveSettings()
            event.accept()

        else:
            event.ignore()

    def loadSwttings(self):
        settings = QSettings('packet', 'open_cv_main', self)
        # print(type(settings.value('input_line','')))
        if len(settings.value('input_line', '')) != 0:
            self.ui.input_line.setText(settings.value('input_line', ''))
            self.image = cv_imread(self.ui.input_line.text())

    def saveSettings(self):
        settings = QSettings('packet', 'open_cv_main', self)
        settings.setValue('input_line', self.ui.input_line.text())
