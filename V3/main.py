from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore
from PyQt5.QtCore import *


from sessionManager import SessionManager
from LoginUi import loginUi
from SignupUi import signupUi
from CollectionUi import collectionUi
from TaskUi import taskUi

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        loginUi.show(self)
        self.sessionManager = SessionManager()
        self.setFixedSize(800, 600)

    def showWindow(self, windowName):

        if (windowName == 'login'):
            loginUi.show(self)

        elif (windowName == 'signup'):
            signupUi.show(self)

        elif (windowName == "collection"):
            collectionUi.show(self)

        elif (windowName == "task"):
            taskUi.show(self)



styleFiles = [
        './styles/main.css',
        ]

if __name__ == '__main__':
    style = ''

    for file in styleFiles:
        file = open(file, 'r')
        style += file.read()
        file.close()

    app = qtw.QApplication([])
    qtg.QFontDatabase.addApplicationFont('./resources/Inter.ttf')
    app.setStyleSheet(style)

    window = MainWindow()
    window.show()

    app.exec_()
