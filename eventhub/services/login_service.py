import allure
from eventhub.pages.login_page import LoginPage
from eventhub.utils.logger import get_logger

logger = get_logger(__name__)
class LoginService:

    def __init__(self, page):
        self.login_page= LoginPage(page)

    def login(self, user):
        logger.info(f"Logging in with email: {user.email}")
        with allure.step(f"login with email: {user.email}"):
            self.login_page.enter_username(user.email)
            self.login_page.enter_password(user.password)
            self.login_page.click_signIn()

    @allure.step("verify user logged in")
    def get_logged_in_user(self):
        return self.login_page.get_logged_in_user()