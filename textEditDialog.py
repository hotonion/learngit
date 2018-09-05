#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication
#
# class textEditDialog(QtWidgets):
#     def __init__(self):
#         super(QtWidgets,self).__init__()
#


from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton,QDialog,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt
import sys


class textEditDialog(QDialog):
    def __init__(self, x, y, table):
        super(textEditDialog, self).__init__()
        self.table = table
        self.x = x
        self.y = y

        # self.setWindowTitle("QTextEdit 例子")
        self.resize(400, 300)
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("OK")
        # self.btnPress2 = QPushButton("Clean")
        layout = QVBoxLayout()

        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        # layout.addWidget(self.btnPress2)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        # self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        newItem = QTableWidgetItem(table.currentItem())
        # newItem = table.currentItem()
        self.textEdit.setText(newItem.text())
        flag = self.windowFlags()
        flag |= (~Qt.WindowTitleHint)
        self.setWindowFlags(Qt.CustomizeWindowHint)


    def btnPress1_Clicked(self):
        # self.textEdit.setPlainText("Hello PyQt5!\n点击按钮")
        newItem = QTableWidgetItem()
        newItem.setText(self.textEdit.toPlainText())
        print(newItem.text())
        self.table.setItem(self.x, self.y, newItem)
        # self.table.item(self.x, self.y).setText(self.textEdit.toPlainText())
        self.accept()

    def btnPress2_Clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n点击按钮。</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = textEditDialog()
    win.show()
    sys.exit(app.exec_())