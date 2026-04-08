import allure

from eventhub.utils.api_client import APIClient


class LoginApiService:

    def __init__(self, base_url):
        self.client = APIClient(base_url)

    @allure.step("Send login API request")
    def login(self, user):
        login_payload = {"email": user.email,"password": user.password,}
        response =self.client.post("/api/auth/login", login_payload)
        allure.attach(
            str(login_payload),
            name="Request payload",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(response.text,
                      name="Response payload",
                      attachment_type=allure.attachment_type.JSON)
        return response
