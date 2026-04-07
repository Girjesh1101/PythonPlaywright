from eventhub.services.api.login_api_service import LoginApiService

from eventhub.test_data.user_builder import UserBuilder


def test_login_api():
    user = UserBuilder().with_email("Prem@yopmail.com").with_password("Automation@2026").build()
    base_url = "https://api.eventhub.rahulshettyacademy.com"
    service = LoginApiService(base_url)
    response = service.login(user)
    assert response.status_code == 200
    print(response.json())



