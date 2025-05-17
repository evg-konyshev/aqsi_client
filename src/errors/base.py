class BaseStrMessageError(Exception):

    def __init__(self, message: str, *_, **__):
        self.message = message


class BaseDictMessageError(Exception):

    def __init__(self, message: dict, *_, **__):
        self.message = message


class BaseRequestError(BaseDictMessageError):

    def __init__(self, status_code: int, text: str, *_, **__):
        self.message = {"status_code": status_code, "text": text}
