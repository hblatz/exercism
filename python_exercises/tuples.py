"""Functions to help Azara and Rui locate pirate treasure.

Azara's List
Treasure, Coordinates
Amethyst Octopus, 1F
Angry Monkey Figurine, 5B
Antique Glass Fishnet Float, 3D
Brass Spyglass. 4B
Carved Wooden Elephant, 8C
Crystal Crab, 6A
Glass Starfish, 6D
Model Ship in Large Bottle, 8A
Pirate Flag, 7F
Robot Parrot, 1C
Scrimshawed Whale Tooth, 2A
Silver Seahorse, 4E
Vintage Pirate Hat, 7E

Rui's List
Location Name, Coordinates, Quadrant
Seaside Cottages, ("1", "C"), Blue
Aqua Lagoon (Island of Mystery), ("1", "F"), Yellow
Deserted Docks, ("2", "A"), Blue
Spiky Rocks, ("3", "D"), Yellow
Abandoned Lighthouse, ("4", "B"), Blue
Hidden Spring (Island of Mystery), ("4", "E"), Yellow
Stormy Breakwater, ("5", "B"), Purple
Old Schooner, ("6", "A"), Purple
Tangled Seaweed Patch, ("6", "D"), Orange
Quiet Inlet (Island of Mystery), ("7", "E"), Orange
Windswept Hilltop (Island of Mystery), ("7", "F"), Orange
Harbor Managers Office, ("8", "A"), Purple
Foggy Seacave, ("8", "C"), Purple
"""

# record = ["Amethyst Octopus", "1F"]  # test
def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[-1]

# coordinate = "2A"  # test
def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    return tuple(list(coordinate))
    # return list(reversed(list(coordinate)))  # everses coordinate element's order
    # list(reversed(list(x))) is not obvious to me. I guess the 'reversed()' does not return a list from a list.


    # azara_record = ('Brass Spyglass', '1C')  # test
    # rui_record = ('Seaside Cottages', ('1', 'C'), 'blue')  # test
def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    # print(convert_coordinate(get_coordinate(azara_record)))  # test
    # print(rui_record[1])  # test
    return convert_coordinate(get_coordinate(azara_record)) == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    
    return 'not a match'


# combined_record_group = (('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))  # test


def clean_up(combined_record_group):
    """    
    Clean up combined record group into a multi-line string of single records,
    so that there's only one set of coordinates per record, and separated by newlines, '\n'.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    Output:
    ('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n
    ('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n
    ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n
    """

    combo_recs = [(rec[0], rec[2], rec[3], rec[4]) for rec in combined_record_group]

    output_str = ''
    for rec in combo_recs:
        output_str = output_str + str(tuple(rec)) + '\n'
    
    return output_str
