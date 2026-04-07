from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        #Locators
        self.username_input = "#email"
        self.password_input = "#password"
        self.login_btn = "#login-btn"
        self.email_label = "#user-email-display"

    def enter_username(self, username):
        self.page.fill(self.username_input,username)

    def enter_password(self, password):
        self.page.fill(self.password_input,password)

    def click_signIn(self):
        self.page.click(self.login_btn)

    def get_logged_in_user(self):
        return  self.page.locator(self.email_label).text_content()
