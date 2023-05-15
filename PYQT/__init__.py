#!/usr/bin/env python
# -*--coding:utf-8 -*-

import os
import sys
import cv2

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, qApp, QMessageBox, QMainWindow, QApplication

import torch
import torch.nn.functional as F
from torchvision import transforms

from project_code.model.model import create_regnet
from project_code.gui import Ui_MainWindow

class Steam:
    def __init__(self, view):
        self.view = view

    def write(self, *args):
        self.view.append(*args)

    def flush(self):
        return

class Signals(object):
    def open_pic(self, ui, text):

    @staticmethod
    def show_author():

    def show_gpu_information(self, mode)：

    def show_crop_delete(self, ui):

    def predict(self, ui):

    def save_dignosis(self, ui):

    def register_signal(self, ui):
        class Window(QMainWindow):
            resized = pyqtSignal()

            def __init__(self, parent=None):
                super(Window, self).__init__(parent=parent)

            def resizeEvent(self, event):
                self.resized.emit()
                return super(Window, self).resizeEvent(event)

        def main():
            app = QApplication(sys.argv)
            window = Window()

            # 设置UI界面
            ui = Ui_MainWindow()
            ui.setupUi(window)

            signals = Signals()
            signals.register_signal(ui)

            window.show()
            sys.exit(app.exec_())

        if __name__ == "__main__":
            main()
