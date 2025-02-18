from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    quantity: float = 1
    unit_price: int = 10
