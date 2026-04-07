from eventhub.pages.login_page import LoginPage


class LoginService:

    def __init__(self, page):
        self.login_page= LoginPage(page)

    def login(self, user):
        self.login_page.enter_username(user.email)
        self.login_page.enter_password(user.password)
        self.login_page.click_signIn()

    def get_logged_in_user(self):
        return self.login_page.get_logged_in_user()