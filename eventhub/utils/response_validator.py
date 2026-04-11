class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected):
        assert response.status_code == expected

    @staticmethod
    def validate_key_exists(response_body, key):
        assert key in response_body