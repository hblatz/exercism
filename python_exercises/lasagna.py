"""lasagna bake time"""
EXPECTED_BAKE_TIME: int = 40
TIME_PER_LAYER: int = 2
elapsed_bake_time: int = 30
number_of_layers: int = 2


def bake_time_remaining(time=elapsed_bake_time, expected=EXPECTED_BAKE_TIME):
    """Calculate the bake time that remains:
    time remaining = expected cook time - elapsed time """
    return expected - time


def preparation_time_in_minutes(layers=number_of_layers):
    """Use a constant, 2, * a variable, layers,
    to calculate preparation time in minutes
    prep = layers * 2 """
    return layers * TIME_PER_LAYER


def elapsed_time_in_minutes(layers=number_of_layers, time=elapsed_bake_time):
    """Elapsed time = prep time + elapsed bake time, where 
    prep = layers * 2 """
    return layers * 2 + time
