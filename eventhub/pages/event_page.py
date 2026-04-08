from playwright.sync_api import Page, expect


class EventPage:
    def __init__(self, page : Page):
        self.page = page

        #Locator
        self.event_btn = page.get_by_role("button", name="Event")
        self.event_card = page.locator("[data-testid='event-card']")
        self.event_container = page.locator(".p-4")


    def click_events(self):
        self.event_btn.click()

    def verify_events_loaded(self):
        expect(self.event_card).to_have_count(3)

    def select_event(self, event_name):
        event= self.event_container.filter(has_text=event_name)
        event.get_by_role("link",name="Book Now").click()

    def verify_book_page_loaded(self, event_name):
        expect(self.page.get_by_text(event_name)).to_be_visible()

