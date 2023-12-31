# Form implementation generated from reading ui file 'App_Second_Window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginInterface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


# from curses import ERR
# from pickle import TRUE
# from tkinter import Button


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import os
import subprocess
from os import *


class StrikeOutDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
        if index.data(QtCore.Qt.DecorationRole) == QtCore.Qt.Checked:
            rect = option.rect
            pen = QtGui.QPen(QtGui.QColor(255, 0, 0))
            pen.setStyle(QtCore.Qt.SolidLine)
            pen.setWidth(2)
            painter.setPen(pen)
            painter.drawLine(rect.topLeft(), rect.bottomRight())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)

        # Translucent Background for the Window
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Make the Window frameless
        MainWindow.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 20, 511, 690))
        self.widget.setStyleSheet(
            "QPushButton#pushButton{\n"
            "    background-color: qlinegradient(spread:pad, x1:0, y1:0,505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "QPushButton#pushButton:hover{\n"
            "    background-color: qlinegradient(spread:pad, x1:0, y1:0,505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
            "}\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding:top;\n"
            "    background-color:rgba(105, 118, 132, 200);\n"
            "}\n"
            "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_6, #pushButton_7{\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "    color:rgba(85, 98, 112, 255);\n"
            "}\n"
            "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_6:hover, #pushButton_7:hover{\n"
            "    color: rgba(155, 168, 182, 200);\n"
            "}\n"
            "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_6:pressed, #pushButton_7:pressed{\n"
            "    padding-left:5px;\n"
            "    padding:top;\n"
            "    background-color:rgba(115, 128, 142, 255);\n"
            "}"
        )
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(40, 40, 431, 611))
        self.label.setStyleSheet(
            "border-image: url(pexels-pixabay-355288.jpg);\n" "border-radius:20px;\n" ""
        )
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 461, 651))
        self.label_2.setStyleSheet(
            "background-color: qlinegradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
            "border-radius:20px;\n"
            ""
        )
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 361, 541))
        self.label_3.setStyleSheet(
            "background: rgba(0,0,0,100);\n" "border-radius : 15px"
        )
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(200, 120, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);\n" "")
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 230, 310, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
            "color:rgba(255, 255, 255, 230);\n"
            "padding-bottom:7px;"
        )
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 310, 310, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\n"
            "border:none;\n"
            "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
            "color:rgba(255, 255, 255, 230);\n"
            "padding-bottom:7px;"
        )
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 430, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton#pushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(122, 63, 147, 255), stop:1 rgba(219, 147, 232, 255));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "QPushButton#pushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(122, 83, 167, 255), stop:1 rgba(239, 167, 252, 255));\n"
            "}\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(239, 167, 252, 200);\n"
            "}\n"
            ""
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 490, 191, 21))
        self.pushButton_5.setStyleSheet(
            "QPushButton#pushButton_5{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(122, 63, 147, 255), stop:1 rgba(219, 147, 232, 255));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "QPushButton#pushButton_5:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0.364, y1:1, x2:1, y2:1, stop:0 rgba(122, 83, 167, 255), stop:1 rgba(239, 167, 252, 255));\n"
            "}\n"
            "QPushButton#pushButton_5:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(239, 167, 252, 200);\n"
            "}\n"
            ""
        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 90, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_username(self):
        username = self.lineEdit.text()

    def get_password(self):
        password = self.lineEdit_2.text()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.pushButton_5.setText(_translate("MainWindow", "New User Register Here !!"))
        self.pushButton_2.setText(_translate("MainWindow", "X"))
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
