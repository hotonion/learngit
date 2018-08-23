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
        打开数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None,("无法打开数据库"),("myLoginUI:初始化数据库失败"),QtWidgets.QMessageBox.Cancel)
            return False
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = myMainwin()
    test.show()
    exit(app.exec_())