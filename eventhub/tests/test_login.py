import time
import allure

from eventhub.services.book_event_service import BookEventService
from eventhub.services.event_service import EventService
from eventhub.services.login_service import LoginService
from eventhub.test_data.builder.attendee_builder import AttendeeBuilder
from eventhub.test_data.builder.user_builder import UserBuilder



@allure.title("Verify user can book event")
@allure.description("Login with valid credential and verify user email")
def test_login(setup):
    page = setup

    user = UserBuilder().with_email("prem@yopmail.com").with_password("Automation@2026").build()
    attendee_data = AttendeeBuilder().with_random_data().build()
    login_service = LoginService(page)
    login_service.login(user)
    actual_email = login_service.get_logged_in_user()
    assert  actual_email == user.email

    event_service = EventService(page)
    event_service.book_event("World Tech Summit")
    event_service.verify_events_book_loaded()

    book_event_service =BookEventService(page)
    book_event_service.book_event_confirm(attendee_data)


    time.sleep(5)


#Page_layer - done
#service_layer - done
#test_layer - done
# builder_design - done
# factory_design - pending
# api_design - started
# allure_reporting - pending
# logger - pending
# create and store data in json