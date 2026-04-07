import time

from eventhub.services.login_service import LoginService
from eventhub.config.configtest import setup
from eventhub.test_data.user_builder import UserBuilder


def test_login(setup):

    user = UserBuilder().with_email("prem@yopmail.com").with_password("Automation@2026").build()

    login_service = LoginService(setup)
    login_service.login(user)
    actual_email = login_service.get_logged_in_user()
    assert  actual_email == user.email
    time.sleep(5)

