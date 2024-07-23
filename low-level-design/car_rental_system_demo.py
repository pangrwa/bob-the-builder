from customer import Customer


class CarRentalSystemDemo:
    @staticmethod
    def run():
        # rental_system = CarRentalSystem()
        alice = Customer("Alice", "Woodlands", "878", "alice@gmail.com", "D123A")
        bob = Customer("Bob", "Yishun", "887", "bob@gmail.com", "D331B")
        # toyota = Car("Toyota", "Vios", "2017", "SGA100D", 70)
        # honda = Car("Honda", "Civic", "2018", "SGA200D", 80)
        # rental_system.add_car(toyota)
        # rental_system.add_car(honda)

        # rental_system.search_available_cars("2019-01-01", "2019-01-03")


if __name__ == "__main__":
    CarRentalSystemDemo.run()
