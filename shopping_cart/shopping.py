from .ShoppingCart.shopping_cart import ShoppingCart
from .Fruit.fruit import Fruit


def initialize_shopping_cart():
    return ShoppingCart([])


def _parse_item_list(item_list: str):
    return [item.strip() for item in item_list.split(",")]


def add_fruits_to_shopping_cart(cart_obj: ShoppingCart, item_list: str):
    items = _parse_item_list(item_list)
    for item in items:
        cart_obj.items.append(Fruit(item))


def remove_fruit_from_shopping_cart(cart_obj: ShoppingCart, rem_item: str):
    for item in cart_obj.items:
        if item.name == rem_item.strip():
            cart_obj.items.remove(item)
