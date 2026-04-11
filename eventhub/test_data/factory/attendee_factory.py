import allure

from eventhub.test_data.builder.attendee_builder import AttendeeBuilder


class BookingFactory():

    @staticmethod
    def get_booking_data(booking_type : str):
        with allure.step(f"create booking data from type {booking_type}") :
            if booking_type == "valid":
                return AttendeeBuilder().with_random_data().build()
            elif booking_type == "invalid":
                return AttendeeBuilder().with_attendee_("").with_attendee_email("").with_attendee_phone_number().with_eventId().build()
            else:
                raise ValueError("invalid booking type")
