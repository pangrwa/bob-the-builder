from typing import Self, Type
from threading import Lock
from inventory import Inventory
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from return_change_state import ReturnChangeState
import coin, note, product, vending_machine_state as vms


# singleton
class VendingMachine:
    _instance = None
    _lock = Lock()

    def __new__(cls: Type["Self"]):
        with cls._lock:
            if cls._instance is None:
                # handle default values
                cls._instance = super().__new__(cls)
                cls._instance._inventory = Inventory()
                cls._instance._balance = 0.0
                cls._instance._selected_product = None
                cls._instance._idle_state = IdleState(cls._instance)
                cls._instance._ready_state = ReadyState(cls._instance)
                cls._instance._dispense_state = DispenseState(cls._instance)
                cls._instance._return_change_state = ReturnChangeState(cls._instance)
                cls._instance._current_state = cls._instance._idle_state
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def insert_coin(self, coin: "coin.Coin"):
        self._current_state.insert_coin(coin)

    def insert_note(self, note: "note.Note"):
        self._current_state.insert_note(note)

    def add_coin(self, coin: "coin.Coin"):
        self._balance += coin.value

    def add_note(self, note: "note.Note"):
        self._balance += note.value

    def select_product(self, product: "product.Product"):
        self._current_state.select_product(product)

    def dispense_product(self):
        self._current_state.dispense_product()

    def return_change(self):
        self._current_state.return_change()

    @property
    def inventory(self) -> "Inventory":
        return self._inventory

    @property
    def selected_product(self) -> "product.Product":
        return self._selected_product

    @selected_product.setter
    def selected_product(self, product: "product.Product"):
        self._selected_product = product

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float):
        self._balance = amount

    @property
    def current_state(self) -> "vms.VendingMachineState":
        return self._current_state

    @current_state.setter
    def current_state(self, state: "vms.VendingMachineState"):
        self._current_state = state

    @property
    def idle_state(self) -> "vms.VendingMachineState":
        return self._idle_state

    @property
    def ready_state(self) -> "vms.VendingMachineState":
        return self._ready_state

    @property
    def dispense_state(self) -> "vms.VendingMachineState":
        return self._dispense_state

    @property
    def return_change_state(self) -> "vms.VendingMachineState":
        return self._return_change_state
