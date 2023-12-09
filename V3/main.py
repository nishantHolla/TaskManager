from PyQt5 import QtWidgets as qtw

from LoginUi import loginUi
from CollectionUi import collectionUi
from TaskUi import taskUi

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        loginUi.show(self)
    def showWindow(self, windowName):

        if (windowName == 'login'):
            loginUi.show(self)

        elif (windowName == "collection"):
            collectionUi.show(self)

        elif (windowName == "task"):
            taskUi.show(self)



if __name__ == '__main__':
    app = qtw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
