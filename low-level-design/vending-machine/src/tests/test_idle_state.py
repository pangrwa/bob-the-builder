import unittest
from unittest.mock import Mock, patch
from inventory import Inventory
from product import Product
from idle_state import IdleState
from io import StringIO


class TestIdleState(unittest.TestCase):
    def setUp(self):
        inventory = Inventory()
        inventory.add_product(Product("Coke", 1.25), 2)
        inventory.add_product(Product("Pepsi", 1.50), 1)
        self.vending_machine = Mock()
        self.vending_machine.inventory = inventory
        self.vending_machine.idle_state = IdleState(self.vending_machine)

    def tearDown(self) -> None:
        del self.vending_machine

    @patch("sys.stdout", new_callable=StringIO)
    def test_insert_coin(self, mock_stdout):
        self.vending_machine.idle_state.insert_coin(Mock())
        self.assertEqual(
            mock_stdout.getvalue().strip(), "Please select a product first"
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_insert_note(self, mock_stdout):
        self.vending_machine.idle_state.insert_note(Mock())
        self.assertEqual(
            mock_stdout.getvalue().strip(), "Please select a product first"
        )

    def test_select_exists_product(self):
        self.vending_machine.idle_state.select_product(Product("Coke", 1.25))
        self.assertEqual(self.vending_machine.selected_product._name, "Coke")

    @patch("sys.stdout", new_callable=StringIO)
    def test_select_non_exists_product(self, mock_stdout):
        self.vending_machine.idle_state.select_product(Product("Fanta", 1.25))
        self.assertEqual(mock_stdout.getvalue().strip(), "Product not available")
