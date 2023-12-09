from CollectionUi import collectionUi
from PyQt5.uic import loadUi

class LoginUi:
    def login(self, parent):
        print(parent.loginUsernameLineEdit.text())
        print(parent.loginPasswordLineEdit.text())
        parent.showWindow('collection')

    def show(self, parent):
        loadUi('./QtLogin.ui', parent)
        parent.loginSubmitButton.clicked.connect(lambda : self.login(parent))

loginUi = LoginUi()
