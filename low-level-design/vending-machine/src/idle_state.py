from vending_machine_state import VendingMachineState
import coin, note, product


class IdleState(VendingMachineState):

    def insert_coin(self, coin: "coin.Coin") -> None:
        print("Please select a product first")

    def insert_note(self, note: "note.Note") -> None:
        print("Please select a product first")

    def select_product(self, product: "product.Product") -> None:
        if self._vm.inventory.has_product(product):
            self._vm.selected_product = product
            self._vm.current_state = self._vm.ready_state
        else:
            print("Product not available")

    def dispense_product(self) -> None:
        print("Please select a product first and make payment")

    def return_change(self) -> None:
        print("No change to return")
