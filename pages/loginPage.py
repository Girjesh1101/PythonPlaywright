from playwright.sync_api import Page, expect

from data.userData_builder import UserData
from pages.basePage import BasePage


class LoginPage(BasePage):

    #Locator
    PLACEHOLDER_LOGIN = "you@email.com"
    PASSWORD = "#password"
    EMAIL_DISPLAY = "#user-email-display"


    def __init__(self, page : Page):
        super().__init__(page)
        self.page = page

    def login(self , user_data : UserData):
        self.page.get_by_placeholder(self.PLACEHOLDER_LOGIN).fill(user_data.username)
        self.page.locator(self.PASSWORD).fill(user_data.password)
        self.page.get_by_role("button",name="Sign In").click()

    def verifyLoginSuccess(self, user_data : UserData):
        expect(self.page.locator(self.EMAIL_DISPLAY)).to_have_text(user_data.username)