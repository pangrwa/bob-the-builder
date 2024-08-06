from abc import ABC, abstractmethod
from coin import Coin
from note import Note
from product import Product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import vending_machine


class VendingMachineState(ABC):

    def __init__(self, vm: "vending_machine.VendingMachine") -> None:
        self._vm = vm

    @abstractmethod
    def insert_coin(self, coin: Coin) -> None:
        pass

    @abstractmethod
    def insert_note(self, note: Note) -> None:
        pass

    @abstractmethod
    def select_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def dispense_product(self) -> None:
        pass

    @abstractmethod
    def return_change(self) -> None:
        pass
