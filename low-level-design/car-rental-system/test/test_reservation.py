import unittest
from reservation import Reservation
from car import Car
from customer import Customer


class TestReservation(unittest.TestCase):

    def test_reservation(self):
        car = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        alice = Customer("Alice", "Woodlands", "878", "alice@gmail.com", "D123A")
        r1 = Reservation(car.id, alice, "2019-01-01", "2019-01-03")
        self.assertEqual(r1.car_id, car.id)
        self.assertEqual(r1.customer, alice)
        self.assertEqual(r1.start_date, "2019-01-01")
        self.assertEqual(r1.end_date, "2019-01-03")
