class TokenManager:

    _token = None
    _event_id = None

    @classmethod
    def get_token(cls):
        return cls._token

    @classmethod
    def set_token(cls, token):
        cls._token = token

    @classmethod
    def get_token(cls):
        return cls._token

    @classmethod
    def set_event_id(cls, event_id):
        cls._event_id = event_id

    @classmethod
    def get_event_id(cls):
        return cls._event_id
