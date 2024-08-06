import unittest
from vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):

    def test_singleton(self):
        a = VendingMachine()
        b = VendingMachine()
        self.assertIs(a, b)
