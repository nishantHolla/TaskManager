"""
This class controls the database of the app.

DB (databasse) is a list of collection dictionaries which has a list of todo dictionaries

collection is a dictionary with the following keys
    name: string => name of the collection
    todos: list => list of todo dictionaries

Todo is a dictionary with the following keys
    title: string => title of the todo
    message: string => message of the todo
    is_completed: bool => whether the todo is completed

"""

import json
import datetime
from pathlib import Path


class TodoManager:
    def __init__(self, db_path):
        """
        Constructor of the class. Fills the DB variable with the data present in the local database

        Parameters:
            db_path: string => path of the database file from which the todos are loaded
        Return:
            None
        """

        self.db_path = Path(db_path)
        self.DB = []

        if self.read_DB() != 0:
            pass  # Throw read error

    def __del__(self):
        """
        Destructor of the class. Writes the value of DB variable into the local database

        Parameters:
            None

        Return:
            None

        """
        self.write_DB()

    def debugPrint(self):
        for collection in self.DB:
            print(collection["name"])
            for todo in collection["todos"]:
                print(f"\t{todo['title']} | {todo['message']} | {todo['is_completed']}")

    def read_DB(self):
        """
        Reads the databse present in db_path

        Parameters:
            None
        Return:
            exitCode: int => 0 if successful read else non zero int

        """
        with open(self.db_path, "r") as file:
            self.DB = json.load(file)

        return 0

    def write_DB(self):
        """
        Writes the databse present in db_path

        Parameters:
            None
        Return:
            exitCode => 0 if successful write else non zero int
        """
        data = json.dumps(self.DB, indent=4)
        with open(self.db_path, "w") as file:
            file.write(data)

        return 0

    def new_collection(self, collection_name, insertion_index=-1):
        """
        Adds a new collection to the databsae

        Parameters:
            collection_name: string => name of the collection to add
            insertioin_index: int => index at which the collection must be added. If the default value
                                     is passed (that is -1) then the collection is added to the end
        Return:
            exitCode: int => 0 if successful addition else non zero int

        """
        try:
            if any(collection["name"] == collection_name for collection in self.DB):
                print(f"Collection '{collection_name}' already exists in the database.")
                exit_code = 1
            else:
                new_collection = {"name": collection_name, "todos": []}
                if insertion_index == -1:
                    self.DB.append(new_collection)
                else:
                    self.DB.insert(insertion_index, new_collection)

            exit_code = 0
        except Exception as e:
            print(f"Error adding collection to database: {e}")
            exit_code = 1

        self.write_DB()
        return exit_code

    def get_collections(self):
        """
        Get list of collection pesent in the database at the current moment.

        Parameters:
            None

        Retrun:
            collections: list => list of all the collection in the databse
        """
        return self.DB

    def get_collection(self, collection_id):
        """
        Get a single collection

        Parameters:
            collection_id: int => index of the collection in the database

        Return:
            collection: dictionary => the collection
        """
        collection = self.DB[collection_id]
        print(collection)

    def remove_collection(self, collection_id):
        """
        Removes an existing collection from the databse

        Parameters:
            collection_id: int => index of the collection to remove

        Return:
            exitCode: int => 0 if successful removal else non zero int

        """
        if collection_id > len(self.DB):
            return 1

        del self.DB[collection_id]
        self.write_DB()
        return 0

    def remove_all_collections(self):
        self.DB = []

    def update_collection(self, collection_id, collection_name):
        """
        Update the name of a collection

        Parameters:
            collection_id: int => index of the collection which needs to be updated
            collection_name: string => new name of the collection

        Return:
            exitCode: int => 0 if successful update else non zero int
        """
        if collection_id > len(self.DB):
            return 1

        collection = self.DB[collection_id]
        collection["name"] = collection_name

        self.write_DB()
        return 0

    def new_todo(
        self,
        collection_id,
        todo_title,
        todo_message,
        todo_reminder=None,
        todo_is_completed=False,
    ):
        """
        Adds a new todo to a given collection in the databse

        Parameters:
            collection_id: int => index of the collection to which the new todo is added
            todo_title: string => title of the new todo
            todo_message: string => message of the new todo
            todo_reminder: datetime object => time to remind the todo
            todo_is_completed: bool => if the new todo is completed. By default it is false

        Return:
            exitCode: int => 0 if successful addition of todo to the collection in the database else non zero int
        """
        if collection_id > len(self.DB):
            return 1

        if todo_reminder:
            r = todo_reminder.strftime("%Y-%m-%d %H:%M:%S")
        else:
            r = None

        self.DB[collection_id]["todos"].append(
            {
                "title": todo_title,
                "message": todo_message,
                "is_completed": todo_is_completed,
                "date_reminder": r,
                "date_created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

        self.write_DB()
        return 0

    def get_todos(self, collection_id):
        """
        Get list of todos persent in the collection

        Parameters:
            collection_id: int => index of the collection from which the todos need to be returned

        Return:
            todos: list => list of todos in the given collection

        """

        if collection_id > len(self.DB):
            return None

        return self.DB[collection_id]["todos"]

    def get_todo(self, collection_id, todo_id):
        """
        Get a single todo from a given collection

        Parameters:
            collection_id: int => index of the collection from which the todo needs to be returned
            todo_id: int => index of the todo in the collection

        Return:
            todo: dictionary => the todo

        """

        if collection_id > len(self.DB):
            return None

        if todo_id > len(self.DB[collection_id]["todos"]):
            return None

        return self.DB[collection_id]["todos"][todo_id]

    def update_todo(
        self,
        collection_id,
        todo_id,
        todo_title="",
        todo_message="",
        todo_is_completed=None,
    ):
        """
        Update a todo

        Parameters:
            collection_id: int => index of the collection in the database
            todo_id: int => index of the todo in the collection
            todo_title: string => new title of the todo. If empty do not update the title
            todo_message: string => new message of the todo. If empty do not update the message
            todo_is_completed: bool => if the todo is completed or not. If None do not update the boolean
        Return:
            exitCode: int => 0 if successful update else non zero int
        """

        if collection_id > len(self.DB):
            return 1

        if todo_id > len(self.DB[collection_id]["todos"]):
            return 2

        todo = self.DB[collection_id]["todos"][todo_id]
        if todo_title:
            todo["title"] = todo_title

        if todo_message:
            todo["message"] = todo_message

        if todo_is_completed != None:
            todo["is_completed"] = todo_is_completed

        self.write_DB()
        return 0

    def remove_todo(self, collection_id, todo_id):
        """
        Removes a new todo from a given collection in the databse

        Parameters:
            collection_id: int => index of the collection from which the todo is to be removed
            todo_id: int => index of the todo in the collection which is to be removed

        Return:
            exitCode: int => 0 if successful removal of todo from the collection in the database else non zero int
        """

        if collection_id > len(self.DB):
            return 1

        if todo_id > len(self.DB[collection_id]["todos"]):
            return 2

        del self.DB[collection_id]["todos"][todo_id]
        self.write_DB()
        return 0

    def remove_all_todos(self, collection_id):
        if collection_id > len(self.DB):
            return 1

        self.DB[collection_id]["todos"] = []
        self.write_DB()
        return 0
