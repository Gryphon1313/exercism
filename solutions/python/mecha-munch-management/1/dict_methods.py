"""Functions to manage a users shopping cart items."""
from typing import Union
Ingredients = dict[str, int]
StoreDetails = list[Union[int, str, bool]]
FulfillmentCart = dict[str, StoreDetails]


def add_item(current_cart: Ingredients, items_to_add) -> Ingredients:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes) -> Ingredients:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return {item: 1 for item in notes}


def update_recipes(ideas: dict[str, Ingredients], recipe_updates: list[tuple[str, Ingredients]]) -> dict[str, Ingredients]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for recipe_name, ingredients in recipe_updates:
        ideas[recipe_name] = ingredients
    return ideas


def sort_entries(cart: Ingredients) -> Ingredients:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart: Ingredients, aisle_mapping: dict[str, StoreDetails]) -> FulfillmentCart:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}
    for item in cart:
        if item in aisle_mapping:
            fulfillment_cart[item] = [
                cart[item],
                aisle_mapping[item][0],
                aisle_mapping[item][1],
            ]
        else:
            fulfillment_cart[item] = [cart[item], None, None]
    return dict(reversed(sorted(fulfillment_cart.items())))


def update_store_inventory(fulfillment_cart: FulfillmentCart, store_inventory: FulfillmentCart) -> FulfillmentCart:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, details in fulfillment_cart.items():
        if item in store_inventory:
            store_inventory[item][0] -= details[0]
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory
