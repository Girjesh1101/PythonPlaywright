import allure
import pytest

from eventhub.services.api.login_api_service import LoginApiService
from eventhub.test_data.factory.user_factory import UserFactory
from eventhub.utils.logger import log_file
from eventhub.utils.token_manager import TokenManager

BASE_URL = "https://eventhub.rahulshettyacademy.com"
API_BASE_URL = "https://api.eventhub.rahulshettyacademy.com"

@pytest.fixture(scope="function")
def setup(page):
    page.goto(f"{BASE_URL}/login")
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item ,call):
    outcome =yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("setup") or item.funcargs.get("page")

        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        try:
            with open(log_file, "r") as f:
                allure.attach(
                    f.read(),
                    name="Execution Logs",
                    attachment_type=allure.attachment_type.TEXT
                )
        except FileNotFoundError:
            pass

@pytest.fixture(scope="session", autouse=True)
def auth_token():

    token = TokenManager.get_token()

    if not token:
        user = UserFactory.get_user("valid")
        service = LoginApiService(API_BASE_URL)
        response = service.login(user)
        token = response.json().get("token")
        TokenManager.set_token(token)
    return token

def get_event_id():
    event_id = TokenManager.get_event_id()
    return event_id
