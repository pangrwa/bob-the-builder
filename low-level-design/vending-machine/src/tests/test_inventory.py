import unittest
from inventory import Inventory


class TestInventory(unittest.TestCase):

    def setUp(self) -> None:
        self.inventory = Inventory()

    def tearDown(self) -> None:
        del self.inventory

    def test_add_product(self):
        self.inventory.add_product("Coke", 2)
        self.inventory.add_product("Coke", 1)
        self.assertEqual(self.inventory._products["Coke"], 3)

    def test_remove_existing_product(self):
        self.inventory.add_product("Coke", 2)
        self.inventory.remove_product("Coke", 1)
        self.assertEqual(self.inventory._products["Coke"], 1)
        self.inventory.remove_product("Coke", 1)
        self.assertFalse("Coke" in self.inventory._products)
