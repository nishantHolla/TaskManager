from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.uic import loadUi
from pyqt_checkbox_list_widget.checkBoxListWidget import CheckBoxListWidget

class TaskUi:
    def addTask(self, parent):
        itemDisplay = f'{parent.taskTitleLineEdit.text()}\n{parent.taskBodyLineEdit.toPlainText()}'
        parent.taskList.addItem(itemDisplay)

    def deleteTask(self, parent):
        current_item = parent.taskList.currentItem()
        if not current_item: return
        parent.taskList.takeItem(parent.taskList.row(current_item))

    def hide(self, parent):
        parent.showWindow('collection')

    def show(self, parent):
        loadUi('./QtTask.ui', parent)
        parent.taskList = CheckBoxListWidget()
        parent.taskMainLayout.addWidget(parent.taskList)

        parent.taskAddButton.clicked.connect(lambda : self.addTask(parent))
        parent.taskDeleteButton.clicked.connect(lambda : self.deleteTask(parent))
        parent.taskBackButton.clicked.connect(lambda : self.hide(parent))

taskUi = TaskUi()
