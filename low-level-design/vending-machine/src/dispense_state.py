from vending_machine_state import VendingMachineState
import coin, note, product


class DispenseState(VendingMachineState):

    def insert_coin(self, coin: "coin.Coin") -> None:
        print("Payment ended. Please collect product")

    def insert_note(self, note: "note.Note") -> None:
        print("Payment ended. Please collect product")

    def select_product(self, product: "product.Product") -> None:
        print("Product already selected. Please collect product")

    def dispense_product(self) -> None:
        product = self._vm.selected_product
        self._vm.inventory.remove_product(product, 1)
        print(f"Product dispensed: {product._name}")
        self._vm.current_state = self._vm.return_change_state

    def return_change(self) -> None:
        print("Please collect product first")
