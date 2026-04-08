from dataclasses import dataclass
from faker import Faker

faker = Faker()

@dataclass
class AttendeeData:
    attendee_full_name: str
    attendee_email: str
    attendee_phone_number: str

class AttendeeBuilder:

    def __init__(self):
        self._attendee_full_name = None
        self._attendee_email = None
        self._attendee_phone_number = None

    def with_random_data(self):
        self._attendee_full_name = faker.name()
        self._attendee_email = faker.email()
        self._attendee_phone_number = faker.msisdn()[:10]
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

    def build(self):
        return AttendeeData(self._attendee_full_name, self._attendee_email, self._attendee_phone_number)