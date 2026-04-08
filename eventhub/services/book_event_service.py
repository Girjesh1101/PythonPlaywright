import allure

from eventhub.pages.book_event_page import BookEventPage


class BookEventService:

    def __init__(self, page):
        self.book_event = BookEventPage(page)

    @allure.step("Fill attendee details and confirm booking")
    def book_event_confirm(self, attendee_data):
        self.book_event.enter_attendee_full_name(attendee_data.attendee_full_name)
        self.book_event.enter_attendee_email(attendee_data.attendee_email)
        self.book_event.enter_attendee_phone(attendee_data.attendee_phone_number)
        total_amount = self.book_event.get_total_label_txt()
        print(total_amount)
        self.book_event.click_on_confirm()

