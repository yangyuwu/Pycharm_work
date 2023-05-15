#!/usr/bin/env python
#!/usr/bin/env python
# -*--2023-5-12 -wyy*-
import sys
import MainWinVerticalLayout
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = MainWinVerticalLayout.Ui_MainWindow()

    # 向主窗口添加控件
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

