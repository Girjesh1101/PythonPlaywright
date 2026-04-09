import allure

from eventhub.services.api.login_api_service import LoginApiService
from eventhub.test_data.factory.user_factory import UserFactory
from eventhub.utils.token_manager import TokenManager

token = TokenManager.get_token()
headers = {"Authorization": f"Bearer {token}"}
base_url = "https://api.eventhub.rahulshettyacademy.com"

@allure.step("Login to Event Hub by API")
def test_login_api():
    user = UserFactory.get_user("valid")
    service = LoginApiService(base_url)
    response = service.login(user)
    assert response.status_code == 200
    print(response.json())


@allure.step("Login with Invalid cred. to Event hub by API ")
def test_invalid_login():
    invalid_user = UserFactory.get_user("invalid")
    service = LoginApiService(base_url)
    response =  service.login(invalid_user)
    assert response.status_code == 400
    print(response.json())


def test_register_and_login():
    base_url = "https://api.eventhub.rahulshettyacademy.com"
    user = UserFactory.get_user("random")
    service = LoginApiService(base_url)
    registration_response = service.registration(user)
    assert registration_response.status_code == 201
    assert token is not None
    assert  "token" in registration_response.json()

    login_response = service.login(user)
    assert login_response.status_code == 200
    assert "token" in login_response.json()

