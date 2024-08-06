import unittest
from unittest.mock import patch, Mock
from io import StringIO
from inventory import Inventory
from product import Product
from ready_state import ReadyState
from coin import Coin
from note import Note


class TestReadyState(unittest.TestCase):

    def setUp(self):
        self.vending_machine = Mock()
        self.vending_machine.balance = 0
        self.vending_machine.ready_state = ReadyState(self.vending_machine)

    def tearDown(self) -> None:
        del self.vending_machine

    @patch("sys.stdout", new_callable=StringIO)
    def test_select_product(self, mock_stdout) -> None:
        self.vending_machine.ready_state.select_product(Product("Coke", 1.25))
        self.assertEqual(
            mock_stdout.getvalue().strip(), "Product selected. Make payment first"
        )

    def test_insert_coin(self) -> None:
        self.vending_machine.ready_state.insert_coin(Coin.DIME)
        self.assertEqual(self.vending_machine.balance, 0.1)

    def test_insert_note(self) -> None:
        self.vending_machine.ready_state.insert_note(Note.ONE)
        self.assertEqual(self.vending_machine.balance, 1)
