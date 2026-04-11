import allure

from eventhub.conftest import  API_BASE_URL
from eventhub.services.api.booking_api_service import BookingApiServices
from eventhub.test_data.factory.attendee_factory import BookingFactory
from eventhub.utils.response_validator import ResponseValidator

booking_id = 14795

@allure.step("get all bookings")
def test_booking_api():

    params = {
        "eventId":1,
        "status":"confirmed",
        "page":1,
        "limit":10

    }
    service = BookingApiServices(base_url=API_BASE_URL)
    response = service.get_all_booking_list()
    print(response.json())
    assert response.status_code == 200

@allure.step("get bookings details by ID")
def test_booking_details_by_id():

    service= BookingApiServices(base_url=API_BASE_URL)
    response = service.get_booking_by_id(booking_id=booking_id)
    response_body = response.json()
    data = response_body["data"]

    assert response.status_code == 200
    assert response.json().get("data").get("id") == booking_id
    assert "data" in response_body
    assert data["id"] == booking_id
    assert data["status"] == "confirmed"
    #schema validation
    assert  isinstance(data["id"], int)
    assert isinstance( data["customerName"], str)
    assert isinstance(data["event"], dict)
    assert isinstance( data["event"]["price"], str)
    assert isinstance(data["event"]["totalSeats"],int)

    #dynamic validation
    assert data["id"] is not None
    assert data["bookingRef"] is not None
    assert data["createdAt"] is not None

    #create method
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_key_exists(response.json(),"data")


@allure.step("delete booking booking")
def test_delete_booking_booking():
    service = BookingApiServices(base_url=API_BASE_URL)
    response = service.delete_booking_by_id(booking_id=booking_id)
    response_body = response.json()
    assert response.status_code == 200
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_key_exists(response_body,"success")
    assert response_body["message"] == "Booking cancelled"
    get_response = service.get_booking_by_id(booking_id=booking_id)
    ResponseValidator.validate_status_code(get_response, 404)




def test_create_booking():

    booking_data  = BookingFactory.get_booking_data("valid")
    print("body :", booking_data)
    service = BookingApiServices(base_url=API_BASE_URL)
    response = service.create_booking(booking_data)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 201
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_key_exists(response_body,"data")
    booking_ref = response_body["data"].get("bookingRef")
    assert booking_ref is not None



