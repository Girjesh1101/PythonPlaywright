from dataclasses import dataclass
from faker import Faker

faker = Faker()

@dataclass
class AttendeeData:
    eventId:int
    attendee_full_name: str
    attendee_email: str
    attendee_phone_number: str
    attendee_quantity: int

class AttendeeBuilder:

    def __init__(self):
        self._eventId = None
        self._attendee_full_name = None
        self._attendee_email = None
        self._attendee_phone_number = None
        self._attendee_quantity = None


    def with_random_data(self):
        self._eventId = 1
        self._attendee_full_name = faker.name()
        self._attendee_email = faker.email()
        self._attendee_phone_number = "9"+faker.msisdn()[:9]
        self._attendee_quantity = faker.msisdn()[:1]
        return self

    def with_eventId(self, event_id):
        self._eventId = event_id
        return self

    def with_attendee_(self, attendee_name):
        self._attendee_full_name = attendee_name
        return self

    def with_attendee_email(self, attendee_email):
        self._attendee_email = attendee_email
        return self

    def with_attendee_phone_number(self, attendee_phone_number):
        self._attendee_phone_number = attendee_phone_number
        return self

    def with_attendee_quantity(self, attendee_quantity):
        self._attendee_quantity = attendee_quantity
        return self

    def build(self):
        return AttendeeData(self._eventId,self._attendee_full_name, self._attendee_email, self._attendee_phone_number,self._attendee_quantity)