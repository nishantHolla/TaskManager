from PyQt5 import QtWidgets as qtw
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
        self.setFixedSize(600, 800)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def showWindow(self, windowName):

        if (windowName == 'login'):
            loginUi.show(self)

        elif (windowName == 'signup'):
            signupUi.show(self)

        elif (windowName == "collection"):
            collectionUi.show(self)

        elif (windowName == "task"):
            taskUi.show(self)



if __name__ == '__main__':
    app = qtw.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
