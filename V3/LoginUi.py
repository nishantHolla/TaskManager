from PyQt5.uic import loadUi
from todoManager import TodoManager

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
        loadUi('./QtLogin.ui', parent)
        parent.loginSubmitButton.clicked.connect(lambda : self.login(parent))
        parent.signupLink.clicked.connect(lambda : self.goToSignupPage(parent))

loginUi = LoginUi()
