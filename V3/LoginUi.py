from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from todoManager import TodoManager
import sys

class LoginUi:
    def login(self, parent):
        username = parent.loginUsernameLineEdit.text()
        password = parent.loginPasswordLineEdit.text()

        if (username == ""):
            parent.errorLabel.setText('Enter a username')
            return

        if (password == ""):
            parent.errorLabel.setText('Enter a password')
            return

        code = parent.sessionManager.start_session(username, password)
        if (code == 2):
            parent.errorLabel.setText('User not found')
            return

        if (code == 3):
            parent.errorLabel.setText('Incorrect password')
            return

        if (code != 0):
            parent.errorLabel.setText('Something went wrong.')
            return

        parent.user = username
        parent.todoManager = TodoManager(f'./users/{username}.json')
        parent.errorLabel.setText('')
        parent.showWindow('collection')

    def goToSignupPage(self, parent):
        parent.errorLabel.setText('')
        parent.showWindow('signup')

    def show(self, parent):
        loadUi('./layouts/login.ui', parent)

        parent.loginCloseButton.setIcon(QIcon('./resources/close.png'))
        parent.loginCloseButton.clicked.connect(lambda: sys.exit(0))
        # parent.loginSubmitButton.clicked.connect(lambda : self.login(parent))
        # parent.signupLink.clicked.connect(lambda : self.goToSignupPage(parent))

loginUi = LoginUi()
