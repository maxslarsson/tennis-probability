from .check import check_sets_won, check_probability, check_not_negative
from math import ceil
from .set import set


def match(
    sets_won_a: int, sets_won_b: int, p: float, best_out_of_n_sets: int = 5
) -> float:
    """Recursively calculates the probability of player A winning at any state in a match.

    This function calls and uses both the `set` and `game` function.

    Args:
        sets_won_a:
            The score for player A.
        sets_won_b:
            The score for player B.
        p:
            The independent probability of player A winning any given point.
        best_out_of_n_sets:
            The number of sets played. Typically, this would be 5 sets for mens, and 3 sets for womens. The default is 5,
            since that is the number of sets played for mens.

    Raises:
        NegativeNumber:
            When either the score is negative or the num_of_sets_played.
        InvalidSetsWon:
            When the score for the players is invalid - arguments `games_won_a` and `games_won_b`.
        InvalidProbability:
            When the probability is invalid - the `p_game` argument.

    Returns:
        The probability of player A winning the match.
    """

    # Check if negative first so I can then use it to check that the number of sets won is valid
    check_not_negative(best_out_of_n_sets)
    check_sets_won(sets_won_a, sets_won_b, best_out_of_n_sets)
    check_probability(p)

    # For example if,
    winning = ceil(best_out_of_n_sets / 2)

    # If player A has won
    # Then the probability of player A winning is 1
    if sets_won_a == winning:
        return 1

    # If player B has won
    # Then the probability of player A winning is 0
    if sets_won_b == winning:
        return 0

    p_set = set(0, 0, p)

    # Otherwise, it is any other state in the game
    return p_set * match(sets_won_a + 1, sets_won_b, p, best_out_of_n_sets) + (
        1 - p_set
    ) * match(sets_won_a, sets_won_b + 1, p, best_out_of_n_sets)
