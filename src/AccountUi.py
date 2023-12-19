"""
User interface for the accounts page of the app
"""

from constants import layouts_dir, resources_dir
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import sys


class AccountUi:
    def delete_account(self, parent):
        """
        Delete currently logged in user

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        current_password = parent.accountDeletePasswordLineEdit.text()
        exit_code = parent.sessionManager.remove_user(parent.user, current_password)

        if exit_code == 3:
            parent.setError("Incorrect password")
            return

        if exit_code != 0:
            parent.setError("Something went wrong")
            return

        parent.showWindow("login")

    def change_password(self, parent):
        """
        Change the password of currently logged in user

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        current_password = parent.accountCurrentPasswordLineEdit.text()
        exit_code = parent.sessionManager.verify_password(parent.user, current_password)

        if exit_code == 3:
            parent.setError("Incorrect password")
            return

        if exit_code != 0:
            parent.setError("Something went wrong")
            return

        new_password = parent.accountNewPasswordLineEdit.text()
        new_password_confirm = parent.accountConfirmPasswordLineEdit.text()

        if new_password != new_password_confirm:
            parent.setError("Passwords do not match")
            return

        exit_code = parent.sessionManager.change_password(parent.user, new_password)
        if exit_code != 0:
            parent.setError("Something went wrong")
            return

        parent.setError()
        parent.accountCurrentPasswordLineEdit.setText("")
        parent.accountConfirmPasswordLineEdit.setText("")
        parent.accountNewPasswordLineEdit.setText("")

    def show(self, parent):
        """
        Show the accounts page

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        loadUi(str(layouts_dir / 'account.ui'), parent)

        parent.accountBackButton.setIcon(QIcon(str(resources_dir / 'back.png')))
        parent.accountBackButton.clicked.connect(
            lambda: parent.showWindow("collection")
        )
        parent.accountChangePasswordButton.clicked.connect(
            lambda: self.change_password(parent)
        )
        parent.accountDeleteButton.clicked.connect(lambda: self.delete_account(parent))
        parent.setError()


accountUi = AccountUi()
