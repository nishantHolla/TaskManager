from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from todoManager import TodoManager
import sys

class LoginUi:
    def login(self, parent):
        username = parent.loginUsernameLineEdit.text()
        password = parent.loginPasswordLineEdit.text()

        if (username == ""):
            parent.setError('Enter a username.')
            return

        if (password == ""):
            parent.setError('Enter a password.')
            return

        code = parent.sessionManager.start_session(username, password)
        if (code == 2):
            parent.setError('User not found.')
            return

        if (code == 3):
            parent.setError('Incorrect password.')
            return

        if (code != 0):
            print(code)
            parent.setError('Something went wrong.')
            return

        parent.user = username
        parent.todoManager = TodoManager(parent.base_path / 'users' / f'{username}.json')
        parent.setError()
        parent.showWindow('collection')

    def goToSignupPage(self, parent):
        parent.setError()
        parent.showWindow('signup')

    def show(self, parent):
        loadUi('./layouts/login.ui', parent)

        parent.loginCloseButton.setIcon(QIcon('./resources/close.png'))
        parent.loginCloseButton.clicked.connect(lambda: sys.exit(0))
        parent.loginButton.clicked.connect(lambda : self.login(parent))
        parent.loginToSignupButton.clicked.connect(lambda : self.goToSignupPage(parent))
        parent.setError()

loginUi = LoginUi()
