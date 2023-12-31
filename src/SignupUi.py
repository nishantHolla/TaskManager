"""
User interface for the signup page
"""
from constants import resources_dir, layouts_dir
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from todoManager import TodoManager
import sys


class SignupUi:
    def signup(self, parent):
        """
        Signup the user with given username and password

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        username = parent.signupUsernameLineEdit.text()
        password = parent.signupPasswordLineEdit.text()
        confirmPassword = parent.signupConfirmPasswordLineEdit.text()

        if username == "":
            parent.setError("Enter a username.")
            return

        if password == "":
            parent.setError("Enter a password.")
            return

        if confirmPassword == "":
            parent.setError("Confirm your password.")
            return

        if password != confirmPassword:
            parent.setError("Passwords do not match.")
            return

        code = parent.sessionManager.new_user(username, password)
        parent.todoManager = TodoManager(
            parent.base_path / "users" / f"{username}.json"
        )
        if code == 1:
            parent.setError("Username already taken.")
            return

        parent.user = username

        parent.setError()
        parent.showWindow("collection")

    def goToLoginPage(self, parent):
        """
        Move from signup page to login page

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        parent.setError()
        parent.showWindow("login")

    def show(self, parent):
        """
        Show the signup page

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        loadUi(str(layouts_dir / 'signup.ui'), parent)

        parent.signupCloseButton.setIcon(QIcon(str(resources_dir / 'close.png')))
        parent.signupCloseButton.clicked.connect(lambda: sys.exit(0))
        parent.signupButton.clicked.connect(lambda: self.signup(parent))
        parent.signupToLoginButton.clicked.connect(lambda: self.goToLoginPage(parent))
        parent.setError()


signupUi = SignupUi()
