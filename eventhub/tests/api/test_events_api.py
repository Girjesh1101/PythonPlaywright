from http.client import responses

import allure
from faker.proxy import Faker

from eventhub.services.api.events_api_services import EventApiService
from eventhub.test_data.factory.event_factory import EventFactory
from eventhub.utils.token_manager import TokenManager

base_url = "https://api.eventhub.rahulshettyacademy.com"
created_event_id  = None

faker = Faker()

@allure.step("GET all events")
def test_get_all_events():

     print("token : ", TokenManager.get_token())
     service = EventApiService(base_url)
     response =  service.get_all_events()
     assert response.status_code == 200
     print(response.json())

@allure.step("get event by id")
def test_get_event_by_id():
      service = EventApiService(base_url)
      response = service.get_event_by_id("1")

      print(response.json())
      assert response.status_code == 200
      assert response.json().get("data").get("id") == 1

def test_create_event():

    print("Future date :", faker.future_datetime(end_date="+7d"))
    service = EventApiService(base_url)

    event_data = EventFactory.get_event("random")
    service = EventApiService(base_url)
    response = service.create_event(event_data)
    print(response.json())
    assert response.status_code == 201
    created_event_id = response.json().get("data").get("id")
    print("Print Event : ",created_event_id)

    get_event_response = service.get_event_by_id(created_event_id)
    assert response.status_code == 201
    assert get_event_response.json().get("data").get("id") == created_event_id


def test_update_event():

    updated_data = EventFactory.get_event("update")
    print("update Print Event : ",updated_data)
    service = EventApiService(base_url)

    service = EventApiService(base_url)
    response = service.update_event(event_id=created_event_id ,event_data=updated_data)
    print(response.json())
    assert response.status_code == 200
    get_event_response = service.get_event_by_id(created_event_id)
    print(get_event_response.json())
    assert get_event_response.status_code == 200


@allure.step("delete event by id")
def test_delete_event():
    service  =EventApiService(base_url)
    response = service.delete_event(event_id=created_event_id)
    print(response.json())
    assert response.status_code == 200
    get_event_response = service.get_event_by_id(created_event_id)
    assert get_event_response.status_code == 404







# def test_list_of_events(playwright: Playwright):
#     request_context = playwright.request.new_context(base_url=base_url)
#     response =request_context.get("api/events",
#                         params={
#                             "page":1,
#                             "limit":12
#                         },
#                         headers={"Authorization": f"Bearer {token}"})
#     assert  response.ok
#     print(response.json())
#
# def test_event_by_id(playwright: Playwright):
#
#     event_id = 2
#     request_context = playwright.request.new_context(base_url=base_url)
#     response =request_context.get(f"api/events/{event_id}",
#                         headers={"Authorization": f"Bearer {token}"})
#     assert  response.ok
#     print(response.json())
#
#
# def test_create_event(playwright: Playwright):
#     request_context = playwright.request.new_context(base_url=base_url)
#     response = request_context.post(f"api/events",)