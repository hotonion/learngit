#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from Ui_Login import Ui_Dialog_login
from TestUi import myMainwin
from PyQt5.QtCore import pyqtSignal
from functools import partial
import sys

unit = ["灵寿网电工队","安国网电工队","肃宁北网电工队","行别营网电工队","沧西网电工队","黄骅南网电工队","黄骅港网电工队","北港电务电力工队","神港电务电力工队","定西供电工队"]


class myLoginUI(QtWidgets.QDialog,Ui_Dialog_login):

    login_success_signal = pyqtSignal(str)

    def __init__(self):
        super(QtWidgets.QDialog,self).__init__()
        self.setupUi(self)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.comboBox_gongdui.addItems(unit)
        
 
        
    #点击登录按钮操作
    def accept(self):
        unit = ''
        username = self.lineEdit_user.text()       
        password = self.lineEdit_passwd.text()
        unit = self.comboBox_gongdui.currentText()
        if (username == "" or password == ""):
            print(QtWidgets.QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes))
            return False

        if QSqlDatabase.contains("qt_sql_default_connection"):
            self.db = QSqlDatabase.database("qt_sql_default_connection")
        else:
            self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None,("无法打开数据库"),("myLoginUI:初始化数据库失败"),QtWidgets.QMessageBox.Cancel)
            return False
        query = QSqlQuery()
        query.prepare("select * from user where name == ? and password == ? and unit ==?");
        query.bindValue(0, username);
        query.bindValue(1, password);
        query.bindValue(2, unit);
        query.exec_()
        if (not query.next()):
            QtWidgets.QMessageBox.information(self, "提示", "该账号不存在!", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)
            self.db.close()
        else:
            #验证正确，隐藏当前窗口，给主窗口发消息
            self.db.close()
            print(query.value(3))
            self.hide()
            self.login_success_signal.emit(unit)
        return True

    def closeEvent(self,event):
        self.db.close()
    #点击退出按钮操作
    # def reject(self):
    #     pass
class myDb():
    
    def __init__(self):

        self.createDb()

    def createDb(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None,("无法打开数据库"),("creataDb:无法打开数据库"),QtWidgets.QMessageBox.Cancel)
            return False
        query = QSqlQuery()
        query.exec_("create table user(id int primary key, name varchar(20), password varchar(20),unit varchar(40))")
        query.exec_("insert into user values(1,'1','1','灵寿网电工队')")
        query.exec_("insert into user values(2,'1','1','安国网电工队')")
        query.exec_("insert into user values(3,'1','1','肃宁北网电工队')")
        query.exec_("insert into user values(4,'1','1','行别营网电工队')")
        query.exec_("insert into user values(5,'1','1','沧西网电工队')")
        query.exec_("insert into user values(6,'1','1','黄骅南网电工队')")
        query.exec_("insert into user values(7,'1','1','黄骅港网电工队')")
        query.exec_("insert into user values(8,'1','1','北港电务电力工队')")
        query.exec_("insert into user values(9,'1','1','神港电务电力工队')")

        self.db.close()
        return True




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = myLoginUI()
    test.show()
    mainui = myMainwin()
    test.login_success_signal.connect(mainui.initData)
    # database = myDb()
    exit(app.exec_())