"""Functions to keep track and alter inventory."""


# items = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]  # test
# result >>> {'coal': 1, 'wood': 2, 'diamond': 3}
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each 
    element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.

    example:
    create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
    >>> {"coal":1, "wood":2, "diamond":3}
    """

    inventory = {}
    for inv_item in items:
        inventory[inv_item] = inventory.get(inv_item, 0) + 1
        
    return inventory

def create_inventory_2(items):
    inventory = {}
    add_items(inventory, items)
    return inventory


# inventory = {'coal': 1, 'wood': 2, 'diamond': 3}  # test
# items = ["wood", "iron", "coal", "wood"]  # test
def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for inv_item in items:
        # IF not in dictionary add item and count to dictionary
        if inventory.get(inv_item, "not in dict") == "not in dict":
            inventory[inv_item] = 1
        else:
            inventory[inv_item] = inventory.get(inv_item, 0) + 1
        
    return inventory


# inventory = {"coal":3, "diamond":1, "iron":5}  # test
# items = ["diamond", "coal", "iron", "iron", "soap"]  # test
# results >>> {"coal":2, "diamond":0, "iron":3}
def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for inv_item, inv_count in inventory.items():
        if inv_count > 0:
            cnt_item = len([item for item in items if item == inv_item])
            if cnt_item <= inv_count:
                inventory[inv_item] = inv_count - cnt_item
            else:
                inventory[inv_item] = 0
        
    # return inv_clean
    return inventory


def decrement_items_2(inventory, items):
    for inv_item in items:
        if inventory[inv_item] > 0:
            inventory[inv_item] -= 1
    return inventory


# inventory = {"coal":2, "wood":1, "diamond":2}  # test
# item = "coal"  # test
# results >>> {"wood":1, "diamond":2}
def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. 
    Current inventory if item does not match.
    """

    inventory.pop(item,"not in dictionary")

    return inventory


def remove_item_2(inventory, item):
    if item in inventory:
        del inventory[item]

    return inventory


# inventory = {"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}  # test
# result >>> [('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)] 
def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
 
    inv_clean = {inv_item: inv_count for inv_item, inv_count in inventory.items() if inv_count != 0}

    return list(inv_clean.items())


def list_inventory_2(inventory):
    output_inventory = [(inv_item, inv_count) for inv_item, inv_count in inventory.items() if inventory[inv_item] > 0]

    return output_inventory
