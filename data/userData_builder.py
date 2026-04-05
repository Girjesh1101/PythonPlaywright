from dataclasses import dataclass


@dataclass
class UserData:
    username : str
    password : str

class UserDataBuilder:
    def __init__(self):
        self.__username = None
        self.__password = None

    def set_username(self, username):
        self.__username = username
        return self

    def set_password(self, password):
        self.__password = password
        return self

    def build(self):
        if not self.__username:
            raise ValueError("Username cannot be empty")
        return UserData(self.__username, self.__password)
