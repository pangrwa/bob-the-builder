from __future__ import annotations
import datetime
from customer import Customer
from itertools import count


class Reservation(object):

    _counter = count(0)

    def __init__(
        self,
        car_id: str,
        customer: Customer,
        start_date: datetime.date,
        end_date: datetime.date,
    ):
        self._id: int = next(Reservation._counter)
        self._car_id: str = car_id
        self._customer: str = customer
        self._start_date: str = start_date
        self._end_date: str = end_date

    @property
    def id(self) -> int:
        return self._id

    @property
    def car_id(self) -> str:
        return self._car_id

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def start_date(self) -> datetime.date:
        return self._start_date

    @property
    def end_date(self) -> datetime.date:
        return self._end_date
