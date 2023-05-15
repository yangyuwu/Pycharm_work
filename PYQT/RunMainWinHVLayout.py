#!/usr/bin/env python
# -*--coding:utf-8 -*-

import sys
import MainWinHVLayout
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainWinHVLayout.Ui_MainWindow()

    # 向主窗口添加控件
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

