from http.client import responses

import allure
import requests

from eventhub.utils.token_manager import TokenManager


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Calling POST api" )
    def post(self, endpoint, payload, use_auth = False):
        url = f"{self.base_url}{endpoint}"
        headers = {}
        if use_auth:
            token = TokenManager.get_token()
            headers["Authorization"] = f"Bearer {token}"
        response =requests.post(f"{url}", headers= headers, data=payload)

        return response

    @allure.step("Calling GET api")
    def get(self , endpoint , params = None , use_auth = False ):
        url  =f"{self.base_url}{endpoint}"
        headers = {}

        if use_auth:
            token = TokenManager.get_token()
            headers["Authorization"] = f"Bearer {token}"
        response =requests.get(url,headers=headers, params=params)
        return response

    @allure.step("Calling DELETE api")
    def delete(self, endpoints, use_auth = False):
        url =f"{self.base_url}{endpoints}"
        headers = {}
        if use_auth:
            token = TokenManager.get_token()
            headers["Authorization"] = f"Bearer {token}"
        response = requests.delete(url, headers=headers)
        return response

    @allure.step("Calling PUT api")
    def update(self, endpoint, payload, use_auth=False):
        url = f"{self.base_url}{endpoint}"
        headers = {}
        if use_auth:
            token = TokenManager.get_token()
            headers["Authorization"] = f"Bearer {token}"
        response = requests.put(f"{url}", headers=headers, data=payload)

        return response