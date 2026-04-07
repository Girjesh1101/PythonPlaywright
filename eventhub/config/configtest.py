import pytest
from pytest_playwright.pytest_playwright import browser

from eventhub.utils.playwright_factory import PlaywrightFactory

@pytest.fixture(scope="function")
def setup():
    url = "https://eventhub.rahulshettyacademy.com/login"
    factory = PlaywrightFactory()
    page , browser , playwright = factory.launch_browser()

    page.goto(url)
    yield  page
    browser.close()
    playwright.stop()


