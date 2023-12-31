"""
User interface for the task page
"""
from PyQt5.QtCore import Qt
from constants import layouts_dir, resources_dir
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from pyqt_checkbox_list_widget.checkBoxListWidget import CheckBoxListWidget
from datetime import datetime


class TaskUi:
    def formatTask(self, title, body, addedOn):
        """
        Format the given ttitle, body and time for display on the task list.

        Parameters:
            title: string => title of the task
            body : string => body of the task
            addedOn : string => time of the task addition

        Return:
            format: string => The formatted string of the task
        """
        return f"{title}\n{body}\nAdded on: {addedOn}"

    def addTask(self, parent):
        """
        Add task to the task list of currently logged in user

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        taskTitle = parent.taskTitleLineEdit.text()
        taskBody = parent.taskBodyLineEdit.toPlainText()

        if taskTitle == "":
            parent.setError('Task ttile is empty. Add a task title.')
            return

        if taskBody == "":
            parent.setError('Task body is empty. Add a task body.')
            return

        time = parent.taskReminderTime.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        parent.todoManager.new_todo(parent.collectionIndex, taskTitle, taskBody, time)
        parent.taskList.addItem(
            self.formatTask(
                taskTitle, taskBody, datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )

        parent.taskTitleLineEdit.setText("")
        parent.taskBodyLineEdit.setPlainText("")
        parent.setError()

    def deleteTask(self, parent):
        """
        Delete the selected task of the currently logged in user.

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        current_item = parent.taskList.currentItem()
        if not current_item:
            parent.setError('Select a task to delete it.')
            return

        item_row = parent.taskList.row(current_item)

        parent.todoManager.remove_todo(parent.collectionIndex, item_row)
        parent.taskList.takeItem(item_row)
        parent.setError()

    def deleteAllTask(self, parent):
        """
        Delete all tasks from the currently logged in user.

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        parent.todoManager.remove_all_todos(parent.collectionIndex)
        parent.taskList.clear()

    def setTask(self, parent, index, state):
        parent.todoManager.update_todo(parent.collectionIndex, index, todo_is_completed = state == 2)


    def show(self, parent):
        """
        Show the task page

        Parameters:
            parent: QtWindow => main window

        Return:
            None
        """
        loadUi(str(layouts_dir / 'todos.ui'), parent)
        parent.taskList = CheckBoxListWidget()
        parent.taskLayout.addWidget(parent.taskList)
        parent.taskList.setStyleSheet(
            "background: transparent; border: 2px solid black; border-radius: 20px;"
        )

        parent.taskAddButton.clicked.connect(lambda: self.addTask(parent))
        parent.taskDeleteButton.clicked.connect(lambda: self.deleteTask(parent))
        parent.taskDeleteAllButton.clicked.connect(lambda: self.deleteAllTask(parent))
        parent.taskBackButton.setIcon(QIcon(str(resources_dir / 'back.png')))
        parent.taskBackButton.clicked.connect(lambda: parent.showWindow("collection"))
        parent.taskReminderTime.setDateTime(QDateTime.currentDateTime().addSecs(300))

        parent.taskList.checkedSignal.connect(lambda x, y: self.setTask(parent, x, y))
        tasks = parent.todoManager.get_todos(parent.collectionIndex)
        for task in tasks:
            parent.taskList.addItem(
                self.formatTask(task["title"], task["message"], task["date_created"])
            )

        for i, todo in enumerate(parent.todoManager.get_todos(parent.collectionIndex)):
            if todo['is_completed']:
                parent.taskList.parent
                parent.taskList.item(i).setCheckState(Qt.Checked)


taskUi = TaskUi()
