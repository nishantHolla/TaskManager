"""
User interface for the login page
"""
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from todoManager import TodoManager
import sys


class LoginUi:
    def login(self, parent):
        """
        Login the user with given username and password

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        username = parent.loginUsernameLineEdit.text()
        password = parent.loginPasswordLineEdit.text()

        if username == "":
            parent.setError("Enter a username.")
            return

        if password == "":
            parent.setError("Enter a password.")
            return

        code = parent.sessionManager.start_session(username, password)
        if code == 2:
            parent.setError("User not found.")
            return

        if code == 3:
            parent.setError("Incorrect password.")
            return

        if code != 0:
            print(code)
            parent.setError("Something went wrong.")
            return

        parent.user = username
        parent.todoManager = TodoManager(
            parent.base_path / "users" / f"{username}.json"
        )
        parent.setError()
        parent.showWindow("collection")

    def goToSignupPage(self, parent):
        """
        Move from login page to signup page

        Parameters:
            parent: QtWIndow => main window

        Return:
            None
        """
        parent.setError()
        parent.showWindow("signup")

    def show(self, parent):
        '''
        Show the login page

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        '''
        loadUi("./layouts/login.ui", parent)

        parent.loginCloseButton.setIcon(QIcon("./resources/close.png"))
        parent.loginCloseButton.clicked.connect(lambda: sys.exit(0))
        parent.loginButton.clicked.connect(lambda: self.login(parent))
        parent.loginToSignupButton.clicked.connect(lambda: self.goToSignupPage(parent))
        parent.setError()


loginUi = LoginUi()
