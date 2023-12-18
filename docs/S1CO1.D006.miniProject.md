
# Objectives

- Create task
- Read task
- Update task
- Delete task
- Remind task
- Group task
- Mark completed task
- Calendar

- Reorder tasks (low priority)

# Teams

- GUI
    - PyQt6
    - subprocess
    - plyer

- Core
    - os
    - sys
    - json
    - random
    - threads

# Backend

- Database class
    - newCollection method -> collection name
    - newTodo method -> collection index, todo title, todo message
    - deleteCollection method -> collection index
    - deleteTodo method -> collection index, todo index
    - startReminderService method
    - stopReminderService method
    - writeDatabase method
    - readDatabase method
    - changeTodoTitle -> collection index, todo index, new title
    - changeTodoMessage -> collection index, todo index, new message

    - Collection class
    - Todo class
