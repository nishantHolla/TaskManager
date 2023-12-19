from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore
from PyQt5.QtCore import *


from constants import database_dir, resources_dir, style_dir
from sessionManager import SessionManager
from todoManager import TodoManager
from LoginUi import loginUi
from SignupUi import signupUi
from CollectionUi import collectionUi
from TaskUi import taskUi
from AccountUi import accountUi

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200,800)

        self.base_path = database_dir
        self.sessionManager = SessionManager()

        self.user = self.sessionManager.get_current_user()
        if self.user != '':
            self.todoManager = TodoManager(self.base_path / 'users' / f'{self.user}.json')
            collectionUi.show(self)
        else:
            loginUi.show(self)

        self.setError()

    def setError(self, error=None):
        if not error:
            self.errorFrame.setVisible(False)
            return

        self.errorLabel.setText(error)
        self.errorFrame.setVisible(True)

    def showWindow(self, windowName):

        if (windowName == 'login'):
            loginUi.show(self)

        elif (windowName == 'signup'):
            signupUi.show(self)

        elif (windowName == "collection"):
            collectionUi.show(self)

        elif (windowName == "task"):
            taskUi.show(self)

        elif (windowName == "account"):
            accountUi.show(self)




styleFiles = [
        str(style_dir / 'main.css')
        ]

if __name__ == '__main__':
    style = ''

    for file in styleFiles:
        file = open(file, 'r')
        style += file.read()
        file.close()

    app = qtw.QApplication([])
    qtg.QFontDatabase.addApplicationFont(str(resources_dir / 'Inter.ttf'))
    app.setStyleSheet(style)

    window = MainWindow()
    window.show()

    app.exec_()
