from playwright.sync_api import Page, expect


class LoginPage():

    #Locator
    PLACEHOLDER_LOGIN = "you@email.com"
    PASSWORD = "#password"
    EMAIL_DISPLAY = "#user-email-display"


    def __init__(self, page : Page):
        self.page = page

    def login(self , username , password):
        self.page.get_by_placeholder(self.PLACEHOLDER_LOGIN).fill(username)
        self.page.locator(self.PASSWORD).fill(password)
        self.page.get_by_role("button",name="Sign In").click()

    def verifyLoginSuccess(self, username):
        expect(self.page.locator(self.EMAIL_DISPLAY)).to_have_text(username)