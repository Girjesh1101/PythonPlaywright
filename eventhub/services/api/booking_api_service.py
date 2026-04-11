import json

import allure

from eventhub.utils.api_client import APIClient
from eventhub.utils.json_writer import write_json


class BookingApiServices:

    get_all_booking_list_endpoint = "/api/bookings"
    get_booking_details_by_id_endpoint = "/api/bookings/{booking_id}"
    delete_booking_by_id_endpoint = "/api/bookings/{booking_id}"
    create_booking_endpoint = "/api/bookings"

    def __init__(self, base_url):
        self.client = APIClient(base_url=base_url)

    @allure.step("call GET apin for booking list")
    def get_all_booking_list(self, params = None):

        response =  self.client.get(self.get_all_booking_list_endpoint , params=params , use_auth=True)
        response_path = write_json(response.json(), "Bookings", "get_all_booking_list_response")
        allure.attach(json.dumps(response.json(), indent=2), name="Response JSON", attachment_type=allure.attachment_type.JSON)

        return response

    @allure.step("call GET api for booking details by id")
    def get_booking_by_id(self, booking_id):
        response =self.client.get(self.get_booking_details_by_id_endpoint.format(booking_id = booking_id),use_auth=True)
        write_json(response.json(), "Bookings", "get_booking_by_id_response")
        allure.attach(json.dumps(response.json(), indent=2), name ="Response JSON", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("call DELETE api for booking by id")
    def delete_booking_by_id(self, booking_id):
        response = self.client.delete(self.delete_booking_by_id_endpoint.format(booking_id = booking_id),use_auth=True)
        write_json(response.json(), "Bookings", "delete_booking_by_id_response")
        allure.attach(json.dumps(response.json(), indent=2), name="Response JSON", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("call POST api for booking details")
    def create_booking(self, booking_data):

        booking_payload = {
            "eventId": booking_data.eventId,
            "customerName": booking_data.attendee_full_name,
            "customerEmail": booking_data.attendee_email,
            "customerPhone": booking_data.attendee_phone_number,
            "quantity": booking_data.attendee_quantity
        }

        response = self.client.post(self.create_booking_endpoint , payload=booking_payload, use_auth=True)
        request_path = write_json(booking_payload , "bookings", "create_booking_request")
        response_path = write_json(response.json(), "Bookings", "create_booking_response")
        allure.attach.file(request_path, name="Payload JSON")
        allure.attach.file(response_path, name="Response JSON")
        allure.attach(json.dumps(response.json(), indent=2), name="Response JSON", attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(response.json(), indent=2),name="Response JSON", attachment_type=allure.attachment_type.JSON)
        return response



