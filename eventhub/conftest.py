import allure
import pytest

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


