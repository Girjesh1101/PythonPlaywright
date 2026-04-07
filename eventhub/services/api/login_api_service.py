from multiprocessing.resource_tracker import register

from eventhub.utils.api_client import APIClient


class LoginApiService:

    def __init__(self, base_url):
        self.client = APIClient(base_url)

    def login(self, user):
        login_payload = {"email": user.email,"password": user.password,}
        response =self.client.post("/api/auth/login", login_payload)
        return response
