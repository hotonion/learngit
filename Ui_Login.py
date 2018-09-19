# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        Dialog_login.setObjectName("Dialog_login")
        Dialog_login.resize(392, 264)
        self.label = QtWidgets.QLabel(Dialog_login)
        self.label.setGeometry(QtCore.QRect(40, 34, 71, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_login)
        self.label_2.setGeometry(QtCore.QRect(57, 92, 51, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_login)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 51, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_user = QtWidgets.QLineEdit(Dialog_login)
        self.lineEdit_user.setGeometry(QtCore.QRect(120, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_passwd = QtWidgets.QLineEdit(Dialog_login)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(120, 88, 211, 31))
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.comboBox_gongdui = QtWidgets.QComboBox(Dialog_login)
        self.comboBox_gongdui.setGeometry(QtCore.QRect(120, 145, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_gongdui.setFont(font)
        self.comboBox_gongdui.setObjectName("comboBox_gongdui")
        self.pushButton = QtWidgets.QPushButton(Dialog_login)
        self.pushButton.setGeometry(QtCore.QRect(170, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_login)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog_login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_login)

    def retranslateUi(self, Dialog_login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_login.setWindowTitle(_translate("Dialog_login", "电力设备履历录入系统"))
        self.label.setText(_translate("Dialog_login", "用户名："))
        self.label_2.setText(_translate("Dialog_login", "密码："))
        self.label_3.setText(_translate("Dialog_login", "单位："))
        self.pushButton.setText(_translate("Dialog_login", "登陆"))
        self.pushButton_2.setText(_translate("Dialog_login", "退出"))

