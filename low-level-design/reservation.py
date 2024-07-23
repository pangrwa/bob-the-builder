import datetime
from car import Car
from customer import Customer
from itertools import count


class Reservation(object):

    _counter = count(0)

    def __init__(
        self,
        car: Car,
        customer: Customer,
        start_date: datetime.date,
        end_date: datetime.date,
    ):
        self._id: int = next(Reservation._counter)
        self._car: str = car
        self._customer: str = customer
        self._start_date: str = start_date
        self._end_date: str = end_date

    @property
    def id(self) -> int:
        return self._id

    @property
    def car(self) -> Car:
        return self._car

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def start_date(self) -> datetime.date:
        return self._start_date

    @property
    def end_date(self) -> datetime.date:
        return self._end_date
