from eventhub.pages.book_event_page import BookEventPage


class BookEventService:

    def __init__(self, page):
        self.book_event = BookEventPage(page)

    def book_event_confirm(self, full_name, email , phone):
        self.book_event.enter_attendee_full_name(full_name)
        self.book_event.enter_attendee_email(email)
        self.book_event.enter_attendee_phone(phone)
        total_amount = self.book_event.get_total_label_txt()
        print(total_amount)
        self.book_event.click_on_confirm()

