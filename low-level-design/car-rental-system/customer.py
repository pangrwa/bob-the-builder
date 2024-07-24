from itertools import count


class Customer(object):
    _counter = count(0)

    def __init__(
        self, name: str, address: str, phone: str, email: str, driver_license: str
    ):
        self._id = next(Customer._counter)
        self._name = name
        self._address = address
        self._phone = phone
        self._email = email
        self._driver_license = driver_license

    @property
    def id(self) -> int:
        return self._id
