import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response =requests.post(f"{url}", json=payload)
        return response