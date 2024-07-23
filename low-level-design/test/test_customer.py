import unittest
from customer import Customer


class TestCustomer(unittest.TestCase):
    def test_customer_id(self):
        alice = Customer("Alice", "Woodlands", "878", "alice@gmail.com", "D123A")
        bob = Customer("Bob", "Yishun", "887", "bob@gmail.com", "D331B")
        self.assertNotEqual(alice.id, bob.id)
