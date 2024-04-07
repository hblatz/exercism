"""Functions which helps the locomotive engineer to keep track of the train.
Working with packing, unpacking operators and multiple assignments."""

"""train_cars = (1, 7, 12, 3, 14, 8, 5)
# output [1, 7, 12, 3, 14, 8, 5]  # test """
def get_list_of_wagons(*train_cars):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    *train_cars_list, = train_cars
    return train_cars_list


def get_list_of_wagons_2(*args):
    return list(args)


"""each_wagons_id = [2, 5, 1, 7, 4, 12, 6, 3, 13] 
missing_wagons = [3, 17, 6, 15]
# expected: [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]  
# result:   [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]  # test """
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    """wagon_list_1 = [1] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]
    print("wagon_list_1 ",  wagon_list_1)  # test """

    wagon_1, wagon_2, locomotive, *rest_wagons = each_wagons_id
    *fixed_wagon_list, = locomotive, *missing_wagons, *rest_wagons, wagon_1, wagon_2
    # print("wagon_list_2 ", wagon_list_2)  # test
    
    return fixed_wagon_list


"""route_dict = {'from': 'Berlin', 'to': 'Hamburg'}
stops = {'stop_1': 'Lepzig', 'stop_2': 'Hannover', 'stop_3': 'Frankfurt'}
# expectedL: {'from': 'Berlin', 'to': 'Hamburg', 'stops': ['Lepzig', 'Hannover', 'Frankfurt']}
# actual:    {'from': 'Berlin', 'to': 'Hamburg', 'stops': ['Lepzig', 'Hannover', 'Frankfurt']}  # test """
def add_missing_stops(route_dict, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    cities = [city for city in stops.values()]
    route_dict.update({"stops": cities})
    return route_dict


def add_missing_stops_2(route, **kwargs):
    return {**route, "stops" : list(kwargs.values())}


def add_missing_stops_3(route: dict, **stops) ->dict:
    return route | {'stops': list(stops.values())}


"""route = {'from': 'Berlin', 'to': 'Hamburg'}
more_route_information = {'timeOfArrival': '12:00', 'precipitation': '10', 'temperature': '5', 'caboose': 'yes'}
# expected: {'from': 'Berlin', 'to': 'Hamburg', 'timeOfArrival': '12:00', 'precipitation': '10', 'temperature': '5', 'caboose': 'yes'}
# actual:   {'from': 'Berlin', 'to': 'Hamburg', 'timeOfArrival': '12:00', 'precipitation': '10', 'temperature': '5', 'caboose': 'yes'}  # test """
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    route.update(**more_route_information)
    return route


def extend_route_information_2(route, more_route_information):
    return {**route, **more_route_information}


def extend_route_information_3(route: dict, more_route_information: dict) -> dict:
    return route | more_route_information


"""wagon_rows = [[(2, 'red'), (4, 'red'), (8, 'red')], 
              [(5, 'blue'), (9, 'blue'), (13, 'blue')], 
              [(3, 'orange'), (7, 'orange'), (11, 'orange')]]  # list(list(tuple()))
# expected: [[(2, 'red'), (5, 'blue'), (3, 'orange')], 
#           [(4, 'red'), (9, 'blue'), (7, 'orange')], 
#           [(8, 'red'), (13, 'blue'), (11, 'orange')]]
# actual:   [[(2, 'red'), (5, 'blue'), (3, 'orange')], 
#           [(4, 'red'), (9, 'blue'), (7, 'orange')], 
#           [(8, 'red'), (13, 'blue'), (11, 'orange')]]  # test """
def fix_wagon_depot(wagon_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    [[a, b, c], [d, e, f], [g, h, i]] = wagon_rows
    wagon_columns = [[a, d, g], [b, e, h], [c, f, i]]
    return wagon_columns


def fix_wagon_depot_2(wagons_rows):
    return list(map(list, zip(*wagons_rows)))  # Note, we haven't covered MAP as yet. 

def fix_wagon_depot_3(wagons_rows):
    [*first_row], [*second_row], [*third_row] = zip(*wagons_rows)
    return [first_row, second_row, third_row]
