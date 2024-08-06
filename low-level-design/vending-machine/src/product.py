class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def __eq__(self, other: "Product") -> bool:
        return self._name == other._name and self._price == other._price

    def __hash__(self) -> int:
        return hash((self._name, self._price))

    @property
    def price(self) -> float:
        return self._price
