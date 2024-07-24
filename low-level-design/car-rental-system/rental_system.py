from typing import Self, Any, List, Dict
from car import Car
from customer import Customer
from reservation import Reservation
import datetime


# Singleton class, prevent inheritance
class RentalSystem(object):
    _instance: Self = None

    def __new__(cls: type[Self], *args: Any, **kwargs: Any) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self._cars: Dict[int, Car] = []
        self._reservations: Dict[int, Reservation] = []

    def add_car(self, car: Car) -> None:
        self._cars[car.id] = car

    def remove_car(self, car: Car) -> None:
        self._cars.pop(car.id)

    def _is_car_available(
        self, car: Car, start_date: datetime.date, end_date: datetime.date
    ) -> bool:
        if not car.is_available:
            return False  # car is not available
        # look through all the current reservations
        for r in self._reservations.values():
            if r.car_id == car.id:
                if start_date < r.end_date and r.start_date < end_date:
                    return False
                else:
                    return True
        return True

    def create_reservation(
        self,
        car: Car,
        customer: Customer,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> Reservation:
        if self._is_car_available(car, start_date, end_date):
            reservation: Reservation = Reservation(car, customer, start_date, end_date)
            self._reservation[reservation.id] = reservation
            return reservation
        return None

    def search_car_by_availability(
        self, start_date: datetime.date, end_date: datetime.date
    ) -> List[Car]:
        cars: List[Car] = []
        for car in self._cars.values():
            if self._is_car_available(car, start_date, end_date):
                cars.append(car)
        return car

    def search_car_by_make(self, make: str) -> List[Car]:
        cars: List[Car] = []
        for car in self._cars.values():
            if car.make == make:
                cars.append(car)
        return cars

    def search_car_by_model(self, model: str) -> List[Car]:
        cars: List[Car] = []
        for car in self._cars.values():
            if car.model == model:
                cars.append(car)
        return cars

    def search_car_by_year(self, year: str) -> List[Car]:
        cars: List[Car] = []
        for car in self._cars.values():
            if car.year == year:
                cars.append(car)
        return cars

    def search_car_by_license_plate(self, license_plate: str) -> List[Car]:
        cars: List[Car] = []
        for car in self._cars.values():
            if car.license_plate == license_plate:
                cars.append(car)
        return cars
