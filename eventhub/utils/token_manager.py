class TokenManager:

    _token = None

    @classmethod
    def set_token(cls, token):
        cls._token = token

    @classmethod
    def get_token(cls):
        return cls._token

    @classmethod
    def get_default_token(cls):
        return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE1NTUsImVtYWlsIjoicHJlbUB5b3BtYWlsLmNvbSIsImlhdCI6MTc3NTczMjM4MywiZXhwIjoxNzc2MzM3MTgzfQ.B5FK1yOwzeeXtp9dV91z9erxLxxpVIIudUw5RoVmru0"


