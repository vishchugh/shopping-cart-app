from shopping_cart import shopping  # noqa: F403
from argparse import ArgumentParser    

if __name__ == '__main__':
    basket = shopping.initialize_shopping_cart()
    
    parser = ArgumentParser()
    parser.add_argument("--fav_fruits", help="Add Fruits to your Shopping Cart", required=True, type=str)
    args = parser.parse_args()

    shopping.add_fruits_to_shopping_cart(basket, args.fav_fruits)
    print(basket)

    shopping.remove_fruit_from_shopping_cart(basket, "banana ")
    print(basket)
