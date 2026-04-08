from playwright.sync_api import Page


class BookEventPage:

    def __init__(self, page:Page):
        self.page = page

        #Locators
        self.full_name_input = page.get_by_placeholder("Your full name")
        self.email_input = page.get_by_placeholder("you@email.com")
        self.phone_input = page.get_by_placeholder("+91 98765 43210")
        self.get_total_label = page.locator("div.bg-indigo-50 span[class='text-indigo-700']")
        self.confirm_booking_btn = page.get_by_role("button", name="Confirm Booking")

    def enter_attendee_full_name(self, full_name):
        self.full_name_input.fill(full_name)

    def enter_attendee_email(self, attendee_email):
        self.email_input.fill(attendee_email)

    def enter_attendee_phone(self, attendee_phone):
        self.phone_input.fill(attendee_phone)

    def get_total_label_txt(self):
        return self.get_total_label.text_content()

    def click_on_confirm(self):
        self.confirm_booking_btn.click()