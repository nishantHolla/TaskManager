from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from todoManager import TodoManager
import sys

class SignupUi:
    def signup(self, parent):
        username = parent.signupUsernameLineEdit.text()
        password = parent.signupPasswordLineEdit.text()
        confirmPassword = parent.signupConfirmPasswordLineEdit.text()

        if (username == ''):
            parent.setError('Enter a username.')
            return

        if (password == ''):
            parent.setError('Enter a password.')
            return

        if (confirmPassword == ''):
            parent.setError('Confirm your password.')
            return

        if (password != confirmPassword):
            parent.setError('Passwords do not match.')
            return

        code = parent.sessionManager.new_user(username, password)
        parent.todoManager = TodoManager(parent.base_path / 'users' / f'{username}.json')
        if (code == 1):
            parent.setError('Username already taken.')
            return

        parent.user = username

        parent.setError()
        parent.showWindow('collection')

    def goToLoginPage(self, parent):
        parent.setError()
        parent.showWindow('login')

    def show(self, parent):
        loadUi('./layouts/signup.ui', parent)

        parent.signupCloseButton.setIcon(QIcon('./resources/close.png'))
        parent.signupCloseButton.clicked.connect(lambda : sys.exit(0))
        parent.signupButton.clicked.connect(lambda : self.signup(parent))
        parent.signupToLoginButton.clicked.connect(lambda : self.goToLoginPage(parent))
        parent.setError()

signupUi = SignupUi()
