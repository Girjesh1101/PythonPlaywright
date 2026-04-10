import json

import allure

from eventhub.utils.api_client import APIClient
from eventhub.utils.json_writer import write_json
from eventhub.utils.token_manager import TokenManager


class LoginApiService:

    login_endpoint = "/api/auth/login"
    registration_endpoint= "/api/auth/register"

    def __init__(self, base_url):
        self.client = APIClient(base_url)

    @allure.step("Send login API request")
    def login(self, user):
        login_payload = {"email": user.email,"password": user.password,}
        response =self.client.post(self.login_endpoint, login_payload)

        request_path = write_json(login_payload, "login", "request")
        response_path = write_json(response.json(),"login", "response")

        allure.attach.file(request_path,name="Request JSON")
        allure.attach.file(response_path,name="Response JSON")
        allure.attach(
            json.dumps(login_payload, indent=2),
            name="Request payload",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(json.dumps(response.json(), indent=2),
                      name="Response payload",
                      attachment_type=allure.attachment_type.JSON)

        token = response.json().get("token")
        if token:
            TokenManager.set_token(token)

        return response

    @allure.step("Register new user API request")
    def registration(self, user):

        registration_payload = {"email": user.email,"password": user.password}
        response = self.client.post(self.registration_endpoint ,registration_payload )

        request_path = write_json(registration_payload,"registration", "request")
        response_path = write_json(response.json(),"registration", "response")

        allure.attach.file(request_path,name="Request JSON")
        allure.attach.file(response_path, name="Response JSON")
        allure.attach(
            json.dumps(registration_payload, indent=2),
            name="Request payload",
            attachment_type=allure.attachment_type.JSON
        )

        allure.attach(
            json.dumps(response.json(), indent=2),
            name="Response payload",
            attachment_type=allure.attachment_type.JSON
        )

        token= response.json().get("token")
        if token:
            TokenManager.set_token(token)
        return  response