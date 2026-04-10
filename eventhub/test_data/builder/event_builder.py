import datetime
from dataclasses import dataclass, asdict

from faker import Faker

faker = Faker()

@dataclass
class EventData:

    title : str
    description : str
    category : str
    venue : str
    city : str
    eventDate : str
    price : int
    totalSeats : int
    imageUrl : str = "https://example.com/banner.jpg"

class EventBuilder:
    def __init__(self):
        self._title = None
        self._description = None
        self._category = None
        self._venue = None
        self._city = None
        self._eventDate = None
        self._price = None
        self._totalSeats = None
        self._imageUrl = None

    def with_title(self, title):
        self._title = title
        return self

    def with_description(self, description):
        self._description = description
        return self

    def with_category(self, category):
        self._category = category
        return self

    def with_venue(self, venue):
        self._venue = venue
        return self

    def with_city(self, city):
        self._city = city
        return self

    def with_eventDate(self, eventDate):
        self._eventDate = eventDate
        return self

    def with_price(self, price):
        self._price = price
        return self

    def with_totalSeats(self, totalSeats):
        self._totalSeats = totalSeats
        return self

    def with_imageUrl(self, imageUrl):
        self._imageUrl = imageUrl
        return self

    def with_event_random_data(self):
        self._title = faker.catch_phrase()
        self._description = faker.text(max_nb_chars=50)
        self._category = faker.random_elements(elements=("Conference", "Music" , "Tech" , "Workshop"))
        self._venue = faker.company()
        self._city = faker.city()
        self._eventDate = str( faker.future_datetime(end_date="+7d"))
        self._price = faker.random_int(min = 500 , max = 5000)
        self._totalSeats = faker.random_int(min = 500 , max = 1000)
        return self

    def updated_event_random_data(self):
        self._title = "updated"+faker.catch_phrase()
        self._description = "updated"+faker.text(max_nb_chars=50)
        self._category = faker.random_elements(elements=("Conference", "Music", "Tech", "Workshop"))
        self._venue = "updated"+faker.company()
        self._city = faker.city()
        self._eventDate = str(faker.future_datetime(end_date="+7d"))
        self._price = faker.random_int(min=500, max=5000)
        self._totalSeats = faker.random_int(min=500, max=1000)
        return self

    def build(self):
        event =  EventData(title=self._title,
            description=self._description,
            category=self._category,
            venue=self._venue,
            city=self._city,
            eventDate=self._eventDate,
            price=self._price,
            totalSeats=self._totalSeats,
            imageUrl=self._imageUrl)
        return asdict(event)