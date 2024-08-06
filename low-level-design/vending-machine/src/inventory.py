from typing import DefaultDict
from collections import defaultdict
import product


class Inventory:
    def __init__(self):
        self._products: DefaultDict["product.Product", int] = defaultdict(int)

    def add_product(self, product: "product.Product", quantity: int):
        self._products[product] += quantity

    def remove_product(self, product: "product.Product", quantity: int):
        self._products[product] -= quantity
        if self._products[product] <= 0:
            del self._products[product]

    def has_product(self, product: "product.Product") -> bool:
        return product in self._products
