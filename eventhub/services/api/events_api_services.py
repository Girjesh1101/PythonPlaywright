import json
import allure
from eventhub.utils.api_client import APIClient
from eventhub.utils.json_writer import write_json
from eventhub.utils.token_manager import TokenManager


class EventApiService:

    get_all_events_endpoint = "/api/events"
    get_event_by_id_endpoint = "/api/events/{event_id}"
    create_event_endpoint = "/api/events"
    delete_event_endpoint = "/api/events/{event_id}"
    update_event_endpoint = "/api/events/{event_id}"

    def __init__(self, base_url):
        self.client = APIClient(base_url)

    @allure.step("Call all events API request")
    def get_all_events(self):
        response  = self.client.get(self.get_all_events_endpoint , use_auth=True)
        response_path =write_json(response.json(), "Events","get_all_event_response")
        allure.attach.file(response_path, name="Response JSON")

        return response

    @allure.step("call event by id API request")
    def get_event_by_id(self, event_id):
        response = self.client.get(self.get_event_by_id_endpoint.format(event_id = event_id), use_auth=True)
        response_path = write_json(response.json(), "Events","get_event_by_id_response")
        allure.attach(json.dumps(response.json(), indent=2), name="Response JSON" , attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("create event API request")
    def create_event(self , event_data):

        event_payload = {
            "title": event_data["title"],
            "description": event_data["description"],
            "category": event_data["category"],
            "venue": event_data["venue"],
            "city": event_data["city"],
            "eventDate": event_data["eventDate"],
            "price": event_data["price"],
            "totalSeats": event_data["totalSeats"],
            "imageUrl": event_data["imageUrl"]
        }

        response = self.client.post(endpoint=self.create_event_endpoint ,payload= event_payload  , use_auth = True)
        request_path = write_json(event_payload, "Events","create_event_payload")
        response_path = write_json(response.json(), "Events","create_event_response")
        allure.attach.file(request_path, name="Payload JSON")
        allure.attach.file(response_path, name="Response JSON")

        allure.attach(
            json.dumps(event_payload, indent=2),name="Request payload",attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            json.dumps(response.json(), indent=2),name="Response JSON",attachment_type=allure.attachment_type.JSON
        )
        event_id = response.json().get("id")
        if event_id:
            TokenManager.set_event_id(event_id)
        return response

    @allure.step("delete event API request")
    def delete_event(self, event_id):
        response = self.client.delete(endpoints=self.delete_event_endpoint.format(event_id = event_id), use_auth=True)
        allure.attach(json.dumps(response.json(), indent=2), name="Response JSON", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("update event API request")
    def update_event(self, event_data , event_id ):
        update_event_payload = {
            "title": event_data["title"],
            "description": event_data["description"],
            "category": event_data["category"],
            "venue": event_data["venue"],
            "city": event_data["city"],
            "eventDate": event_data["eventDate"],
            "price": event_data["price"],
            "totalSeats": event_data["totalSeats"],
            "imageUrl": event_data["imageUrl"]
        }

        response = self.client.update(self.update_event_endpoint.format(event_id = event_id), payload= update_event_payload, use_auth=True)

        request_path = write_json(update_event_payload ,"Events", "update_payload")
        response_path = write_json(response.json(), "Events","update_response")
        allure.attach.file(request_path, name="Payload JSON")
        allure.attach.file(response_path, name="Response JSON")
        allure.attach(json.dumps(update_event_payload, indent=2), name="Response JSON" , attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(response.json(), indent=2), name="Response JSON" , attachment_type=allure.attachment_type.JSON)

        return response



