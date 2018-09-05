# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\swallow\learngit\Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        Dialog_login.setObjectName("Dialog_login")
        Dialog_login.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_login)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog_login)
        self.label.setGeometry(QtCore.QRect(50, 50, 48, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_login)
        self.label_2.setGeometry(QtCore.QRect(66, 90, 36, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_login)
        self.label_3.setGeometry(QtCore.QRect(66, 140, 36, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_user = QtWidgets.QLineEdit(Dialog_login)
        self.lineEdit_user.setGeometry(QtCore.QRect(120, 50, 133, 20))
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_passwd = QtWidgets.QLineEdit(Dialog_login)
        self.lineEdit_passwd.setGeometry(QtCore.QRect(120, 90, 133, 20))
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.comboBox_gongdui = QtWidgets.QComboBox(Dialog_login)
        self.comboBox_gongdui.setGeometry(QtCore.QRect(120, 140, 131, 20))
        self.comboBox_gongdui.setObjectName("comboBox_gongdui")

        self.retranslateUi(Dialog_login)
        self.buttonBox.accepted.connect(Dialog_login.accept)
        self.buttonBox.rejected.connect(Dialog_login.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_login)

    def retranslateUi(self, Dialog_login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_login.setWindowTitle(_translate("Dialog_login", "电力设备履历录入系统"))
        self.label.setText(_translate("Dialog_login", "用户名："))
        self.label_2.setText(_translate("Dialog_login", "密码："))
        self.label_3.setText(_translate("Dialog_login", "单位："))

