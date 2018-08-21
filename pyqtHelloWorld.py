#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QAction,QApplication, QWidget, QPushButton, QToolTip, QMessageBox,QDesktopWidget,QMainWindow,qApp
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        #
        self.setToolTip('This is a <b>QWidget</b> widget 哈哈')

        self.setGeometry(300, 200, 400, 300)
        self.setWindowTitle("主要看气质")
        self.setWindowIcon(QIcon("icon-96x96.png"))
        self.setWindowTitle('Tooltips')
        #初始化按钮
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a QPushButton widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('&Quit', self)
        qbtn.setToolTip('This is a QPushButton widget')
        qbtn.resize(btn.sizeHint())
        qbtn.move(50, 150)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage("Ready")
        self.initMenu()
        self.center()
        self.show()

    def initMenu(self):
        exitAction = QAction(QIcon('icon-96x96.png'),'&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)
        newAction = QAction('&Add',self)
        newAction.setShortcut('Ctrl+A')
        menubar = self.menuBar()
        taskMenu = menubar.addMenu('&Task')
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(newAction)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        retmsgbox = QMessageBox.question(self, 'Msg', "A U to Quit?",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
        if retmsgbox == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mainWinodw = QWidget()
    # mainWinodw.resize(300,200)
    # mainWinodw.move(400,300)
    # mainWinodw.setWindowTitle("测试")
    # mainWinodw.setWindowIcon(QIcon("icon-96x96.png"))
    # mainWinodw.show()
    hello = mainUi()

    sys.exit(app.exec_())