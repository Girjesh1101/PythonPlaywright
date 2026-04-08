import time

from eventhub.services.book_event_service import BookEventService
from eventhub.services.event_service import EventService
from eventhub.services.login_service import LoginService
from eventhub.config.configtest import setup
from eventhub.test_data.user_builder import UserBuilder


def test_login(setup):

    user = UserBuilder().with_email("prem@yopmail.com").with_password("Automation@2026").build()

    login_service = LoginService(setup)
    login_service.login(user)
    actual_email = login_service.get_logged_in_user()
    assert  actual_email == user.email

    event_service = EventService(setup)
    event_service.book_event("World Tech Summit")
    event_service.verify_events_book_loaded()

    book_event_service =BookEventService(setup)
    book_event_service.book_event_confirm("Prem","simple@gmail.com","9876543210")


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