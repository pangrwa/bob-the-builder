from vending_machine_state import VendingMachineState
import coin, note, product


class ReturnChangeState(VendingMachineState):
    def insert_coin(self, coin: "coin.Coin") -> None:
        print("Please collect change first")

    def insert_note(self, note: "note.Note") -> None:
        print("Please collect change first")

    def select_product(self, product: "product.Product") -> None:
        print("Please collect change first")

    def dispense_product(self) -> None:
        print("Product dispensed. Collect change")

    def return_change(self) -> None:
        change = self._vm.balance - self._vm.selected_product.price
        if change > 0:
            print(f"Change returned: {change}")
            self._vm.balance = 0
        else:
            print("No change to return")
        self._vm.selected_product = None
        self._vm.current_state = self._vm.idle_state
