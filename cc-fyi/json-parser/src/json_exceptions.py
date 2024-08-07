class JSONException(Exception):
    pass


class JSONDFAException(JSONException):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__("JSONDFAException - " + message)


class JSONParserException(JSONException):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__("JSONParserException - " + message)
