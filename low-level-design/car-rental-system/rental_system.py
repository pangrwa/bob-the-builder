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
        self._cars: Dict[int, Car] = {}
        self._reservations: Dict[int, Reservation] = {}

    @staticmethod
    def get_instance() -> Self:
        if RentalSystem._instance is None:
            RentalSystem()
        return RentalSystem._instance

    def add_car(self, car: Car) -> None:
        self._cars[car.id] = car

    def remove_car(self, car: Car) -> None:
        self._cars.pop(car.id)

    def create_reservation(
        self,
        car: Car,
        customer: Customer,
        start_date: datetime.date,
        end_date: datetime.date,
    ) -> Reservation:
        if car.id in self._cars and car.is_available(start_date, end_date):
            reservation: Reservation = Reservation(
                car.id, customer, start_date, end_date
            )
            self._reservations[reservation.id] = reservation
            car.add_reservation(reservation)
            return reservation
        return None

    def cancel_reservation(self, reservation_id: str) -> None:
        reservation: Reservation = self._reservations.pop(reservation_id, None)
        self._cars[reservation.car_id].remove_reservation(reservation_id)
        # if reservation is not found, ideally throw an exception

    def search_car_by_availability(
        self, start_date: datetime.date, end_date: datetime.date
    ) -> List[Car]:
        cars: List[Car] = []
        for car in self._cars.values():
            if car.is_available(start_date, end_date):
                cars.append(car)
        return cars

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
