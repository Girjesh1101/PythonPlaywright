import allure

from eventhub.pages.event_page import EventPage


class EventService:
    def __init__(self, page):
        self.event_page = EventPage(page)

    @allure.step("verify user select event")
    def book_event(self, event_name):
        self.event_page.click_events()
        self.event_page.verify_events_loaded()
        self.event_page.select_event(event_name)
    @allure.step("verify event page details")
    def verify_events_book_loaded(self):
        self.event_page.verify_events_loaded()
