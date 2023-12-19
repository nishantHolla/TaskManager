# TaskManager
Semester 1 mini project for CS

IMPLEMENTATION DETAILS
======================

The project was implemented with modularity in mind. The frontend, backend, database are built independently
with well defined API calls from one domain to the other which allows replacement of any of them with
some other solution without disrupting other domains of the application.

On launch of the application, it follows this flow of execution:

START => reminder service and (login or sign up page) => collections page => account page or task page

FRONTEND
========

The frontend of the application is divided into 4 main parts. These are:
    1. UI handlers
    2. UI layouts
    3. Styles
    4. Resources

1. UI handlers
    These are python files that handle UI initializations and action calls to buttons and
    other interactive elements of the  UI. They also handle UI transitions from one window to the
    other. The application consists of 5 windows. They are
        a. Login layout
        b. Signup layout
        c. Collections layout
        d. Account layout
        e. Task layout

2. UI layouts
    These are QT files that define the layout of the UI. They are created using the Qt designer
    Which allow flexible layouts and ease of development. These files are managed by their
    respective UI handlers.

3. Styles
    These are css stylesheets which define the style of the UI elements of QT. These files are
    read at the time of launch of the app.

4. Resources
    This directory contains all resources used by application such as images and fonts.

BACKEND
=======

The backend of the application is divided into 3 main parts called managers. These are:
    1. reminderManager
    2. sessionManager
    3. todoManager

1. reminderManager
    ReminderManager manages all the notification reminders of the application. It runs as a
    background process and check for pending reminders every 10 seconds. It is initialized on statup
    of the system. Uses plyer to integrate system independent notification service.

2. sessionManager
    sessionManager manages all the authentication required for the app. It interacts with users.json
    database and handles user creation, user deletion, user login, user logout. It is initialized by
    the application on launch. Uses argon2 to store and verify password hashes.

3. todoManager
    todoManager manages all the task related actions of the user. It handles task creation, task deletion,
    collection creation, collection deletion It is initialized by sessionManager on successful login.

DATABASE
========

Currently the application uses a json file to store all data of the users. This is fine for light
weight usage of the applications with few than 100 users. But once the userbase of the application
grows, switching to a dedicated database service such as SQL is preferred.

The application has a users.json file which stores all the usernames and their hashed passwords.
Each user gets their own json file to store their collections and tasks in a file called <username>.json.
Due to this users with same usernames are not allowed in the application and this validation is done
during the signup of new user.

The user data is stored as a list of collections which are dictionary containing the name of the
collection and a list of tasks present in the given collection.

Each task is a dictionary which stores the title, message, reminder time, addition time and state
of the task.

FUTURE WORK
===========

1. Replace the current json database with a more robust solution like MongoDB or SQL.
2. Implement forgot password action.
3. Implement multi device notification service.

REFERENCES
==========

1. PESU academy notes.
2. Open source software such as pyqt-checkbox-list-widget
3. Module documentation of argon2 and player
