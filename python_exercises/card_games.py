"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    hand_count: int = len(hand)
    hand_total: int = 0
    for card in hand:
        hand_total = hand_total + int(card)

    return hand_total / hand_count


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values )
    OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # get average from card_average() function for comparisons
    true_average = card_average(hand)

    # find central number(s) as proxy for average
    # calculate first + last / 2 as proxy for average
    # compare: if F+L/2 = Avg OR Mid = Avg then TRUE
    first_and_last = (hand[0] + hand[-1])/2
    middle_card = hand[int(round(len(hand)/2))]
    # return true_average == first_and_last or true_average == middle_card
    return true_average in (first_and_last, middle_card)


def average_even_is_average_odd(hand):
    """Return if the (avg of even indexed card values) == (avg of odd indexed cards).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    hand_odds = hand[0::2]
    hand_evens = hand[1::2]

    return card_average(hand_odds) == card_average(hand_evens)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand = hand[:-1]
        hand.append(22)

    return hand
