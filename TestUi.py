#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_TestUi import Ui_MainWin

class myMainwin(QMainWindow,Ui_MainWin):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setupUi(self)
    def initData(self,msg):
        #收到login窗口的信号，根据传入参数，初始化主窗口数据并显示
        print("recive signle :",msg)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = myMainwin()
    test.show()
    exit(app.exec_())