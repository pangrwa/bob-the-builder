from vending_machine_state import VendingMachineState
import coin, note, product


class ReadyState(VendingMachineState):

    def insert_coin(self, coin: "coin.Coin") -> None:
        self._vm.add_coin(coin)
        print(f"Coin inserted: {coin.name}")
        self._check_payment_status()

    def insert_note(self, note: "note.Note") -> None:
        self._vm.add_note(note)
        print(f"Note inserted: {note.name}")
        self._check_payment_status()

    def select_product(self, product: "product.Product") -> None:
        print("Product selected. Make payment first")

    def dispense_product(self) -> None:
        print("Product selected. Make payment first")

    def return_change(self) -> None:
        print("No change to return")

    def _check_payment_status(self):
        if self._vm.balance >= self._vm.selected_product.price:
            self._vm.current_state = self._vm.dispense_state
