from PyQt5.uic import loadUi
from todoManager import TodoManager

class SignupUi:
    def signup(self, parent):
        username = parent.signupUsernameLineEdit.text()
        password = parent.signupPasswordLineEdit.text()
        confirmPassword = parent.signupConfirmPasswordLineEdit.text()

        if (username == ''):
            parent.errorLabel.setText('Enter a username')
            return

        if (password == ''):
            parent.errorLabel.setText('Enter a password')
            return

        if (confirmPassword == ''):
            parent.errorLabel.setText('Confirm your password')
            return

        if (password != confirmPassword):
            parent.errorLabel.setText('Passwords do not match')
            return

        code = parent.sessionManager.new_user(username, password)
        parent.todoManager = TodoManager(f'./users/{username}')
        if (code == 1):
            parent.errorLabel.setText('Username already taken.')
            return

        parent.user = username

        parent.errorLabel.setText('')
        parent.showWindow('collection')

    def goToLoginPage(self, parent):
        parent.errorLabel.setText('')
        parent.showWindow('login')

    def show(self, parent):
        loadUi('./QtSignup.ui', parent)
        parent.signupSubmitButton.clicked.connect(lambda : self.signup(parent))
        parent.loginLink.clicked.connect(lambda : self.goToLoginPage(parent))

signupUi = SignupUi()
