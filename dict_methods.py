"""Functions to manage a users shopping cart items."""


# 1
"""current_cart = {'Banana': 3, 'Apple': 2, 'Orange': 1}  # test 1
items_to_add = ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')  # test 1
# results >>> {'Banana': 4, 'Apple': 5, 'Orange': 2}  # test 1 """
"""current_cart = {'Banana': 3, 'Apple': 2, 'Orange': 1}   # test 2
items_to_add = ['Banana', 'Orange', 'Blueberries', 'Banana']   # test 2
# results >>> {'Banana': 5, 'Apple': 2, 'Orange': 2, 'Blueberries': 1}  # test 2 """
def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for new_item in items_to_add:
        if new_item in current_cart:
            current_cart[new_item] = current_cart[new_item] + 1
        else:
            current_cart.update({new_item: 1})

    return current_cart


# 2
"""notes = ('Banana','Apple', 'Orange')  # test 1  # test 1
# results >>> {'Banana': 1, 'Apple': 1, 'Orange': 1}  # test 1 """
"""notes = ['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']  # test 2
# results >>> {'Blueberries' : 1, 'Pear' : 1, 'Orange' : 1, 'Banana' : 1, 'Apple' : 1}  # test 2 """
def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = dict.fromkeys(list(notes), 1)

    return cart


# 3
"""ideas = {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1}, 
         'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}
recipe_updates = (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)

# {'Banana Bread' : {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3},
# 'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}} """
"""ideas = {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1}, 
          'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
          'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}}
recipe_updates = [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
                  ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
                  ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})]

# {'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
# 'Raspberry Pie': {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2},
# 'Pasta Primavera': {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1},
# 'Blueberry Crumble': {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3}} """
def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


# 4
"""4 test inputs: [{'Banana': 4, 'Apple': 2, 'Orange': 1, 'Pear': 12},
        {'Apple': 3, 'Orange': 5, 'Banana': 1, 'Avocado': 2},
        {'Orange': 3, 'Banana': 2, 'Apple': 1},
        {'Apple': 2, 'Raspberry': 2, 'Blueberries': 5, 'Broccoli' : 2, 'Kiwi': 1, 'Melon': 4}]  # test set 1 - 4

4 test outputs: [{'Apple': 2, 'Banana': 4, 'Orange': 1, 'Pear': 12},
{'Apple': 3, 'Avocado': 2, 'Banana': 1, 'Orange': 5},
{'Apple': 1, 'Banana': 2, 'Orange': 3},
{'Apple' : 2, 'Blueberries': 5, 'Broccoli': 2, 'Kiwi': 1, 'Melon': 4, 'Raspberry': 2}] # test set 1 - 4 """
# cart = {'Banana': 4, 'Apple': 2, 'Orange': 1, 'Pear': 12}  # test 1
def sort_entries(cart):
    return dict(sorted(cart.items()))


# 5
""" cart = {'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}  # test 1
aisle_mapping = {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 
                 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}  # test 1
# results >>> {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 
#               'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]} # test 1 """
def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store. """

    # build a new cart with pairs [food, [count, aisle, fridge]] 
    """ probably, can be done directly with dictionaries. I figured out how to do it with lists."""
    new_cart_list = []
    for (food, count) in cart.items():
        new_cart_list = new_cart_list + [[food, [count] + list(aisle_mapping.get(food))]]
    
    # build new dictionary from the new list
    new_cart_dict = {}
    for item in new_cart_list:
        food_item, food_properties = item
        new_cart_dict[food_item] = food_properties
 
    # return a reversed sorted dictionary
    rev_sort_cart = sorted(new_cart_dict.items(), reverse = True)

    return rev_sort_cart


fullfillment_cart = {'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 
                     'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}
store_inventory = {'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 
                   'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}
# result >>> {'Banana': [12, 'Aisle 5', False], 'Apple': [10, 'Aisle 4', False], 
#           'Orange': ['Out of Stock', 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True]}  # test """
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    pass
