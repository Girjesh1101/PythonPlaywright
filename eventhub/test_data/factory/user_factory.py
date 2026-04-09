import allure

from eventhub.test_data.builder.user_builder import UserBuilder


class UserFactory:

    @staticmethod

    def get_user(user_type:str):
        with allure.step(f"create user :{user_type}"):

            if user_type == "valid":
                return UserBuilder().with_email("prem@yopmail.com").with_password("Automation@2026").build()

            elif user_type == "invalid":
                return UserBuilder().with_email("wrong@gmail.com").with_password("wrongpassword").build()

            elif user_type == "random":
                return UserBuilder().with_random_credentials().build()

            else:
                raise ValueError(f"Invalid user type : {user_type}")