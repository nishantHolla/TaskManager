from sessionManager import SessionManager
from plyer import notification
from todoManager import TodoManager
import time
from datetime import datetime

sm = SessionManager()

def send_notification(title, message):
    notification.notify(
        title=f'TaskManager reminder: {title}',
        message=message,
        app_name="TaskManager",
        timeout=10
    )


while True:
    user = sm.get_current_user()
    if user == '':
        continue

    now = datetime.now()
    tm = TodoManager(rf'C:\Users\nishant\Desktop\TM\src\database\users\{user}.json')
    db = tm.get_collections()
    for i, collection in enumerate(db):
        for j, todo in enumerate(collection['todos']):
            reminder = datetime.strptime(todo['date_reminder'], '%Y-%m-%d %H:%M:%S')
            if reminder < now and not todo['reminded']:
                send_notification(todo['title'], todo['message'])
                tm.update_todo(i, j, reminded=True)

    time.sleep(10)
