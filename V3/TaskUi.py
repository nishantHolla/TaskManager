from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.uic import loadUi
from pyqt_checkbox_list_widget.checkBoxListWidget import CheckBoxListWidget

class TaskUi:
    def formatTask(self, title, body):
        return f'{title}\n{body}'

    def addTask(self, parent):
        taskTitle = parent.taskTitleLineEdit.text()
        taskBody = parent.taskBodyLineEdit.toPlainText()

        parent.todoManager.new_todo(parent.collectionIndex, taskTitle, taskBody)
        parent.taskList.addItem(self.formatTask(taskTitle, taskBody))

    def deleteTask(self, parent):
        current_item = parent.taskList.currentItem()
        if not current_item: return

        item_row = parent.taskList.row(current_item)

        parent.todoManager.remove_todo(parent.collectionIndex, item_row)
        parent.taskList.takeItem(item_row)

    def hide(self, parent):
        parent.showWindow('collection')

    def show(self, parent):
        loadUi('./QtTask.ui', parent)
        parent.taskList = CheckBoxListWidget()
        parent.taskMainLayout.addWidget(parent.taskList)

        parent.taskAddButton.clicked.connect(lambda : self.addTask(parent))
        parent.taskDeleteButton.clicked.connect(lambda : self.deleteTask(parent))
        parent.taskBackButton.clicked.connect(lambda : self.hide(parent))

        tasks = parent.todoManager.get_todos(parent.collectionIndex)
        for task in tasks:
            parent.taskList.addItem(self.formatTask(task['title'], task['message']))


taskUi = TaskUi()
