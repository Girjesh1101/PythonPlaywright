import allure
import pytest
from eventhub.utils.logger import log_file

BASE_URL = "https://eventhub.rahulshettyacademy.com"

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


