"""
This class controls the authentication of the app.
"""
import json
import argon2
import os


class SessionManager:
    def __init__(self):
        """
        Constructor of the class. Reads the users file.

        Parameters:
            None
        Return:
            None
        """
        self.users_file = "./users.json"
        self.users_data = dict()
        self.ph = argon2.PasswordHasher()

        self.read_users()

    def __del__(self):
        """
        Destructor of the class. Write the users file.

        Parameters:
            None
        Return:
            None
        """
        self.write_users()

    def debugPrint(self):
        print(self.users_data)

    def new_user(self, user_name, user_password):
        """
        Add a new users.

        Parameters:
            user_name: string => username of the new user
            user_password: string => password of the new user

        Return:
            exitCode: int => 0 if successful addition of user else non zero int
        """
        if user_name in self.users_data["users"]:
            return 1

        user = {"name": user_name, "password": self.ph.hash(user_password)}
        self.users_data["users"][user_name] = user

        with open(f"./users/{user_name}.json", "w") as file:
            file.write("[]")

        return 0

    def remove_user(self, user_name, user_password):
        """
        Remove an existing user

        Parameters:
            user_name: string => username of the user to remove
            user_password: string => password of the user to remove

        Return:
            exitCode: int => 0 if successful removal of user else non zero int
        """
        if user_name not in self.users_data["users"]:
            return 1

        if self.users_data["current_user"] != user_name:
            return 2

        try:
            self.ph.verify(
                    self.users_data["users"][user_name]["password"], user_password
                    )
        except Exception:
            return 3

        self.users_data["current_user"] = ""
        del self.users_data["users"][user_name]
        os.remove(f"./users/{user_name}.json")
        return 0

    def start_session(self, user_name, user_password):
        """
        Start a new session

        Parameters:
            user_name: string => username
            user_password: string => user password

        Return:
            exitCode: int => 0 if successful start of session else non zero int
        """
        if self.users_data["current_user"] != "":
            return 1

        if user_name not in self.users_data["users"]:
            return 2

        try:
            self.ph.verify(
                    self.users_data["users"][user_name]["password"], user_password
                    )
        except Exception:
            return 3

        self.users_data["current_user"] = user_name
        return 0

    def end_session(self):
        """
        End the current session

        Parameters:
            None

        Return:
            exitCode: int => 0 if successful end of session else non zero int
        """
        if self.users_data["current_user"] == "":
            return 1

        self.users_data["current_user"] = ""
        return 0

    def read_users(self):
        """
        Read the users file

        Parameters:
            None
        Return:
            None
        """
        with open(self.users_file, "r") as file:
            self.users_data = json.load(file)

    def write_users(self):
        """
        Writes the users file

        Parameters:
            None
        Return:
            None

        """
        data = json.dumps(self.users_data, indent=4)
        with open(self.users_file, "w") as file:
            file.write(data)
