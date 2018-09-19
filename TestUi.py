#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAction, QFileDialog, QTableWidgetItem, QMessageBox,QHeaderView
from Ui_TestUi import Ui_MainWin
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRecord
from PyQt5.QtGui import QMouseEvent, QIcon
from PyQt5.QtCore import Qt, qDebug
from textEditDialog import textEditDialog
import xlsxwriter
import MyXlsx

class myMainwin(QMainWindow, Ui_MainWin):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.unit = ''
        self.setWindowIcon(QIcon("icon-96x96.png"))
        # 隐藏垂直表头
        self.tableWidget.verticalHeader().setVisible(False)
        # 隐藏水平表头
        # self.tableWidget.horizontalHeader().setVisible(False)
        # tableWidget
        # self.textEdit = QtWidgets.QTextEdit()
        # self.tableWidget.setCellWidget(1, 1, self.textEdit)
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.setColumnWidth(1,600)
        self.tableWidget.setWordWrap(True)

        # 设置最后一行沾满整个格
        tableHeader = self.tableWidget.horizontalHeader()
        tableHeader.setStretchLastSection(True)
        # 设置表头背景颜色
        tableHeader.setStyleSheet("QHeaderView::section{background-color:rgb(00,00,255);}")
        self.tableWidget.cellDoubleClicked.connect(self.mycellDoubleClicked)
        self.pushButton.clicked.connect(self.saveData)
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
        ret = MyXlsx.saveSheet(filename, self.unit, self.tableWidget)
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
        self.unit = msg
        # 打开数据库
        self.opendb()
        #读数据并显示
        strFilter = "unit = '%s'"%msg
        print("strFilter = "+strFilter)
        model = QSqlTableModel()
        model.setTable("history")
        model.setFilter(strFilter)
        model.setSort(0,Qt.AscendingOrder)
        model.select()
        print("model.rowCount = %d"%model.rowCount())
        rowNum = 0
        # newItem = QTableWidgetItem()
        # todo model.rowCount>17的异常处理
        if model.rowCount()>17:
            self.tableWidget.setRowCount(model.rowCount())
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
        while rowNum < 17:
            column = 0
            while column < 2:
                newItem = QTableWidgetItem('')
                self.tableWidget.setItem(rowNum, column, newItem)
                column += 1
            rowNum += 1

        self.tableWidget.resizeRowsToContents()
        #关闭数据库
        # self.tableWidget.verticalHeader.hide()
        self.db.close()
        self.show()


    # 将表格中的数据保存到数据库存储
    def saveData(self):

        #todo 弹出警告对话框，要求用户确认是否保存数据
        reply = QtWidgets.QMessageBox.warning(self, "警告", "即将保存更改至数据库是否继续?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        if reply == QMessageBox.No:
            return True

        if self.db.isOpen() != True:
            if self.opendb() != True:
                # todo 打开数据库失败错误处理退出
                return
        rowNum = 0
        query = QSqlQuery()

        while rowNum < self.tableWidget.rowCount():
            year = self.tableWidget.item(rowNum,0)
            profilo = self.tableWidget.item(rowNum,1)
            query.prepare("select * from history where unit == ? and year == ?")
            query.bindValue(0, self.unit)
            query.bindValue(1, year.text())
            query.exec_()
            if (query.next()):
                # 数据存在，更新数据
                query.prepare("update history set profilo = ? where year = ? and unit = ?")
                query.bindValue(2, self.unit)
                query.bindValue(1, year.text())
                query.bindValue(0, profilo.text())
                query.exec_()

            else:
                #数据不存在，插入数据
                query.prepare("insert into history values(?, ?, ?)")
                query.bindValue(2, self.unit)
                query.bindValue(0, year.text())
                query.bindValue(1, profilo.text())
                query.exec_()

            error = self.db.lastError()
            print("error.type = %d" %error.type())
            qDebug(error.text())
            rowNum += 1
        self.db.close()
        return True

    def saveDataOld(self):
        if self.db.isOpen() != True:
            if self.opendb() != True:
                # todo 打开数据库失败错误处理退出
                return
        rowNum = 0
        model = QSqlTableModel()
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        while rowNum < self.tableWidget.rowCount():
            year = self.tableWidget.item(rowNum,0)
            profilo = self.tableWidget.item(rowNum,1)
            model.setTable("history")
            strFilter = "unit = '%s' and year = '%s'" %(self.unit,year.text())
            model.setFilter(strFilter)
            model.select()
            if model.rowCount() != 0:
                curRecord = model.record(0)
                curRecord.setValue(self.tableWidget.item(rowNum,1))
                model.setRecord(0,curRecord)
                model.submitAll()
            else:
                curRecord = QSqlRecord()
                curRecord.setValue("year",year.text())
                curRecord.setValue("profilo",profilo.text())
                curRecord.setValue("unit",self.unit)

                ret = model.insertRecord(-1,curRecord)
                if ret == True:
                    print("数据库插入成功")
                else:
                    print("数据插入失败ret = %d" %ret)

                ret = model.submitAll()
                if ret == True:
                    print("提交成功")
                else:
                    error = self.db.lastError()
                    print("提交失败,ret = %d" %ret)
                    # print(error.text())
                    qDebug(error.text())
            rowNum += 1
        self.db.close()
        return True
    def opendb(self):
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
    sys.exit(app.exec_())