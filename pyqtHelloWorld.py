#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWinodw = QWidget()
    mainWinodw.resize(300,200)
    mainWinodw.move(400,300)
    mainWinodw.setWindowTitle("测试")
    mainWinodw.setWindowIcon(QIcon("icon-96x96.png"))


    mainWinodw.show()


    sys.exit(app.exec_())