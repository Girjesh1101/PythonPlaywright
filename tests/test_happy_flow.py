from pages.loginPage import LoginPage


def test_happy_flow(playwright):

    url = "https://eventhub.rahulshettyacademy.com/login"
    username = "prem@yopmail.com"
    password = "Automation@2026"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    loginObj = LoginPage(page)
    loginObj.open(url)
    loginObj.login(username , password)
    loginObj.verifyLoginSuccess(username)

