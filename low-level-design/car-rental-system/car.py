from itertools import count


class Car(object):
    _counter = count(0)

    def __init__(
        self, make: str, model: str, year: str, license_plate: str, daily_rate: float
    ):
        self._id: int = next(Car._counter)
        self._make: str = make
        self._model: str = model
        self._year: str = year
        self._license_plate: str = license_plate
        self._daily_rate: str = daily_rate

    @property
    def id(self) -> int:
        return self._id

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> str:
        return self._year

    @property
    def license_plate(self) -> str:
        return self._license_plate

    @property
    def daily_rate(self) -> float:
        return self._daily_rate
