import datetime

import allure

from eventhub.test_data.builder.event_builder import EventBuilder


class EventFactory:

    @staticmethod
    def get_event(event_type:str):
        with (allure.step(f"create event by : {event_type} ")):
            if event_type == "valid":
                return (EventBuilder()
                        .with_title("DJ Summit 2027")
                        .with_description("this will be automation description")
                        .with_category("Music")
                        .with_venue("Mumbai Point")
                        .with_city("Mumbai")
                        .with_eventDate("2026-06-15T09:00:00.000Z")
                        .with_price(1000)
                        .with_totalSeats(500)
                        .with_imageUrl("https://example.com/banner.jpg")
                        .build())
            elif event_type == "invalid":
                return (EventBuilder()
                        .with_title("invalid title ")
                        .with_description("invalid description")
                        .with_category("invalid category")
                        .with_venue("invalid")
                        .with_eventDate("2026-06-15T09:00:00.000Z")
                        .with_price(0)
                        .with_totalSeats(0)
                        .with_imageUrl("https://example.com/banner.jpg")
                        .build())
            elif event_type == "random":
                return EventBuilder().with_event_random_data().build()
            elif event_type == "update":
                return EventBuilder().updated_event_random_data().build()
            else:
                raise ValueError("invalid event type")





