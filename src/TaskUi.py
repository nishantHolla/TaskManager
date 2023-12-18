from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.uic import loadUi
from pyqt_checkbox_list_widget.checkBoxListWidget import CheckBoxListWidget
from datetime import datetime

class TaskUi:
    def formatTask(self, title, body, addedOn):
        return f'{title}\n{body}\nAdded on: {addedOn}'

    def addTask(self, parent):
        taskTitle = parent.taskTitleLineEdit.text()
        taskBody = parent.taskBodyLineEdit.toPlainText()

        time = parent.taskReminderTime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        parent.todoManager.new_todo(parent.collectionIndex, taskTitle, taskBody, time)
        parent.taskList.addItem(self.formatTask(taskTitle, taskBody, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        parent.taskTitleLineEdit.setText('')
        parent.taskBodyLineEdit.setPlainText('')

    def deleteTask(self, parent):
        current_item = parent.taskList.currentItem()
        if not current_item: return

        item_row = parent.taskList.row(current_item)

        parent.todoManager.remove_todo(parent.collectionIndex, item_row)
        parent.taskList.takeItem(item_row)

    def deleteAllTask(self, parent):
        parent.todoManager.remove_all_todos(parent.collectionIndex)
        parent.taskList.clear()

    def hide(self, parent):
        parent.showWindow('collection')

    def show(self, parent):
        loadUi('./layouts/todos.ui', parent)
        parent.taskList = CheckBoxListWidget()
        parent.taskLayout.addWidget(parent.taskList)
        parent.taskList.setStyleSheet('background: transparent; border: 2px solid black')

        parent.taskAddButton.clicked.connect(lambda : self.addTask(parent))
        parent.taskDeleteButton.clicked.connect(lambda : self.deleteTask(parent))
        parent.taskDeleteAllButton.clicked.connect(lambda : self.deleteAllTask(parent))
        parent.taskBackButton.setIcon(QIcon('./resources/back.png'))
        parent.taskBackButton.clicked.connect(lambda : self.hide(parent))
        parent.taskReminderTime.setDateTime(QDateTime.currentDateTime().addSecs(300))

        tasks = parent.todoManager.get_todos(parent.collectionIndex)
        for task in tasks:
            parent.taskList.addItem(self.formatTask(task['title'], task['message'], task['date_created']))


taskUi = TaskUi()
