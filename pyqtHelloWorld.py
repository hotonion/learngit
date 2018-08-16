#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont


class mainUi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        QToolTip.setFont(QFont('SansSerif', 10))

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
        self.show()


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