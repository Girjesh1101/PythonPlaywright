from dataclasses import dataclass

from faker import Faker

faker = Faker()
@dataclass
class UserData:
    email :str
    password : str

class UserBuilder:
    def __init__(self):
        self._email = "Prem@yopmail.com" #default value
        self._password = "Automation@2026"

    def with_email(self, email):
        self._email = email
        return self

    def with_password(self, password):
        self._password = password
        return self

    def with_random_credentials(self):
        self._email = faker.email()
        self._password = faker.password(length=10)
        return self

    def build(self):
        return UserData(self._email, self._password)