import unittest
import datetime
from rental_system import RentalSystem
from car import Car
from customer import Customer
from reservation import Reservation


class TestRentalSystem(unittest.TestCase):

    def setUp(self):
        self.rental_system = RentalSystem()

    def test_add_car(self):
        car1 = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        car2 = Car("Honda", "Civic", "2018", "SGA200D", 80)
        self.rental_system.add_car(car1)
        self.rental_system.add_car(car2)
        self.assertEqual(len(self.rental_system._cars), 2)
        self.assertEqual(self.rental_system._cars[car1.id], car1)
        self.assertEqual(self.rental_system._cars[car2.id], car2)

    def test_remove_car(self):
        car1 = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        car2 = Car("Honda", "Civic", "2018", "SGA200D", 80)
        self.rental_system.add_car(car1)
        self.rental_system.add_car(car2)
        self.assertEqual(len(self.rental_system._cars), 2)
        self.rental_system.remove_car(car1)
        with self.assertRaises(KeyError) as cm:
            self.rental_system._cars[car1.id]
        self.assertEqual(len(self.rental_system._cars), 1)
        self.assertEqual(self.rental_system._cars[car2.id], car2)

    def test_create_reservation(self):
        car1 = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        self.rental_system.add_car(car1)
        alice = Customer("Alice", "Woodlands", "878", "alice@gmail.com", "D123A")
        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2021, 1, 3)
        reservation: Reservation = self.rental_system.create_reservation(
            car1, alice, start_date, end_date
        )
        self.assertIsNotNone(reservation)
        self.assertFalse(car1.is_available(start_date, end_date))
        self.assertEqual(self.rental_system._reservations[reservation.id], reservation)

    def test_cancel_reservation(self):
        car1 = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        self.rental_system.add_car(car1)
        alice = Customer("Alice", "Woodlands", "878", "alice@gmail.com", "D123A")
        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2021, 1, 3)
        reservation: Reservation = self.rental_system.create_reservation(
            car1, alice, start_date, end_date
        )
        self.rental_system.cancel_reservation(reservation.id)
        self.assertTrue(car1.is_available(start_date, end_date))
        with self.assertRaises(KeyError) as cm:
            self.rental_system._reservations[reservation.id]

    def test_search_car_by_availability(self):
        car1 = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        car2 = Car("Honda", "Civic", "2018", "SGA200D", 80)
        car3 = Car("Toyota", "Vios", "2017", "SGA300D", 70)
        self.rental_system.add_car(car1)
        self.rental_system.add_car(car2)
        self.rental_system.add_car(car3)

        alice = Customer("Alice", "Woodlands", "878", "alice@gmail.com", "D123A")
        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2021, 1, 3)
        reservation: Reservation = self.rental_system.create_reservation(
            car1, alice, start_date, end_date
        )

        sstart_date = datetime.date(2021, 1, 4)
        send_date = datetime.date(2021, 1, 10)
        test = self.rental_system.search_car_by_availability(sstart_date, send_date)
        x = map(lambda c: c.license_plate, test)
        self.assertEqual(
            self.rental_system.search_car_by_availability(sstart_date, send_date),
            [car1, car2, car3],
        )
