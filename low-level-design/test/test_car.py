import unittest
from car import Car


class TestCar(unittest.TestCase):
    def test_car(self):
        car = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Vios")
        self.assertEqual(car.year, "2017")
        self.assertEqual(car.license_plate, "SGA100D")
        self.assertEqual(car.daily_rate, 70)

    def test_car_id(self):
        car1 = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        car2 = Car("Honda", "Civic", "2018", "SGA200D", 80)
        self.assertNotEqual(car1.id, car2.id)


if __name__ == "__main__":
    unittest.main()
