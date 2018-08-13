#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWinodw = QWidget()
    mainWinodw.resize(300,400)
    mainWinodw.move(400,300)
    mainWinodw.setWindowTitle("TEST")
    
    mainWinodw.show()


    sys.exit(app.exec_())