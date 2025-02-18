from dataclasses import dataclass
from ..Fruit.fruit import Fruit


@dataclass
class ShoppingCart:
    items: list[Fruit]
