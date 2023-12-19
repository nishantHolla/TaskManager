#!../env/Scripts/pythonw.exe
from constants import database_dir
import threading
import time
from sessionManager import SessionManager
from plyer import notification
from todoManager import TodoManager
import time
from datetime import datetime
from pathlib import Path
import os

database_path = database_dir / 'users'

sm = SessionManager()

def send_notification(title, message):
    notification.notify(
        title=f'TaskManager reminder: {title}',
        message=message,
        app_name="TaskManager",
        timeout=10
    )

def check():
    sm.read_users()
    user = sm.get_current_user()
    if user == '':
        return

    now = datetime.now()
    print(user)
    user_path = database_path / f'{user}.json'
    tm = TodoManager(str(user_path))
    db = tm.get_collections()
    for i, collection in enumerate(db):
        for j, todo in enumerate(collection['todos']):
            reminder = datetime.strptime(todo['date_reminder'], '%Y-%m-%d %H:%M:%S')
            if reminder < now and not todo['reminded']:
                send_notification(todo['title'], todo['message'])
                tm.update_todo(i, j, reminded=True)



def run_function_periodically(interval):
    while True:
        check()
        time.sleep(interval)

interval_seconds = 10

background_thread = threading.Thread(target=run_function_periodically, args=(interval_seconds,), daemon=True)
background_thread.start()

while True:
    time.sleep(1)
