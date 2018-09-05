#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QHeaderView,QAction,QFileDialog,QTableWidgetItem,QMessageBox
from Ui_TestUi import Ui_MainWin
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlTableModel
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt
from textEditDialog import textEditDialog
import xlsxwriter
import MyXlsx

class myMainwin(QMainWindow, Ui_MainWin):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        # 隐藏垂直表头
        self.tableWidget.verticalHeader().setVisible(False)
        # 隐藏水平表头
        # self.tableWidget.horizontalHeader().setVisible(False)
        # tableWidget
        # self.textEdit = QtWidgets.QTextEdit()
        # self.tableWidget.setCellWidget(1, 1, self.textEdit)
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnWidth(1,600)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.cellDoubleClicked.connect(self.mycellDoubleClicked)
        # 菜单初始化
        self.menubar.triggered[QAction].connect(self.processtrigger)
    # 处理菜单trigger信号
    def processtrigger(self,q):
        if q.text() == "save":
            self.saveXlsxFile()

        elif q.text() == "open":
            # todo menu 'open' Action
            pass
        elif q.text() == "quit":
            # todo menu 'quit' Action
            pass
        elif q.text() == "close":
            # todo menu 'close' Action
            pass
        elif q.text() == "Help":
            # todo menu 'Help' Action
            pass
        elif q.text() == "About":
            # todo todo menu 'About' Action
            pass
        print(q.text()+" is triggered")

    def saveXlsxFile(self):
        # filename, _ = QFileDialog.getOpenFileName(self,'Open file','c:\\',"Excel Files (*.xlsx)")
        filename, _ = QFileDialog.getSaveFileName(self,'Save File','c:\\',"Excel Files (*.xlsx)")
        print(filename)
        ret = MyXlsx.saveSheet(filename,self.tableWidget)
        if ret == 0:
            QMessageBox.information(self,"saved","文件保存成功",QMessageBox.Yes,QMessageBox.Yes)
        else:
            return False
        return True

    def mycellDoubleClicked(self, x, y):
        print("received signal X=", x, " Y=", y)
        if y == 1:
            textDlg = textEditDialog(x,y,self.tableWidget)
            textDlg.setWindowModality(Qt.ApplicationModal)
            textDlg.exec_()
            print(self.tableWidget.item(x,y))
            # 刷新显示多行的情况
            self.tableWidget.resizeRowsToContents()
            # self.tableWidget.resizeColumnsToContents()


    def initData(self,msg):
        #收到login窗口的信号，根据传入参数，初始化主窗口数据并显示
        print("received signal :", msg)
        # 打开数据库
        self.opendb()
        #读数据并显示
        # query = QSqlQuery()
        # query.prepare("select * from history where unit ==?")
        # query.bindValue(0, msg)
        # if (query.next()):
        # query.exec_()
        strFilter = "unit = '%s'"%msg
        print("strFilter = "+strFilter)
        model = QSqlTableModel()
        model.setTable("history")
        model.setFilter(strFilter)
        model.select()
        print("model.rowCount = %d"%model.rowCount())
        rowNum = 0
        # newItem = QTableWidgetItem()
        while rowNum < model.rowCount():
            print("rowNum = %d"%rowNum)
            print(model.record(rowNum).value(0))
            print(model.record(rowNum).value(1))
            print(model.record(rowNum).value(2))
            column = 0
            while column < 2:
                newItem = QTableWidgetItem(model.record(rowNum).value(column))
                # print(newItem.text())
                self.tableWidget.setItem(rowNum,column, newItem)
                column += 1
            rowNum += 1
        self.tableWidget.resizeRowsToContents()
        #关闭数据库
        # self.tableWidget.verticalHeader.hide()
        self.db.close()
        self.show()

    def opendb(self):

        # if (QSqlDatabase::contains("qt_sql_default_connection"))
        # db = QSqlDatabase::database("qt_sql_default_connection");
        #
        # else
        # db = QSqlDatabase::addDatabase("QSQLITE");
        #
        if QSqlDatabase.contains("qt_sql_default_connection"):
            self.db = QSqlDatabase.database("qt_sql_default_connection")
        else:
            self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, ("无法打开数据库"),("myLoginUI:初始化数据库失败"),QtWidgets.QMessageBox.Cancel)
            return False
        return True
    def mouseDoubleClickEvent(self, *args, **kwargs):

        print("double click")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = myMainwin()
    test.show()
    # test.mouseDoubleClickEvent()
    exit(app.exec_())