from .errors import (
    InvalidProbability,
    InvalidInput,
    NegativeNumber,
)


def check_probability(p: float) -> object:
    """Checks if the probability is valid.

    Args:
        p:
            The independent probability of player A winning any given point.

    Raises:
        InvalidProbability:
            When the probability is invalid - the `p_game` argument.
    """

    # Argument p_game is invalid if it is less than 0.0 or greater than 1.0
    if p < 0 or p > 1:
        raise InvalidProbability(p)


def check_score(score_a: int, score_b: int):
    """Checks that the player scores are valid.

    Args:
        score_a:
            The score for player A.
        score_b:
            The score for player B.

    Raises:
        InvalidInput:
            When the score for the players is invalid - arguments `games_won_a` and `games_won_b`.
    """
    # If either score is negative, it is invalid
    check_not_negative(score_a, score_b)
    # If either score is above 4, it is invalid
    # This means it is PAST the number 4, which returns 1 since a player won
    if score_a > 4 or score_b > 4:
        raise InvalidInput
    # A score of 3 for both players or above is invalid
    # This is since there is a "missing" node in the diagram. There is no state at (3,3).
    if score_a >= 3 and score_b >= 3:
        raise InvalidInput


def check_games_won(games_a: int, games_b: int):
    """Checks that the number of games won is valid.

    Args:
        games_a:
            The score for player A.
        games_b:
            The score for player B.

    Raises:
        InvalidInput:
            When the score for the players is invalid - arguments `games_won_a` and `games_won_b`.
    """
    # If the number of games won for either player is negative, it is invalid
    check_not_negative(games_a, games_b)
    # If the number of games won is above 6, it is also an invalid
    # This means it is PAST the number 6, which returns 1 since a player won
    if games_a > 6 or games_b > 6:
        raise InvalidInput
    # Winning 5 or more games is invalid
    # This is since there is a "missing" node in the diagram. There is no state at (5,5).
    if games_a >= 5 and games_b >= 5:
        raise InvalidInput


def check_sets_won(sets_a: int, sets_b: int, best_out_of_n_sets: int):
    """Checks that the number of sets won is valid.

    Args:
        sets_a:
            The number of sets won for player A.
        sets_b:
            The number of sets won for player B.
        best_out_of_n_sets:
            The number of sets played. This is passed in to make sure that the number of won sets is less than the number of sets played.

    Raises:
        InvalidInput:
            When the number of sets won is invalid - arguments `sets_a` and `sets_b`.
    """
    # If the number of games won for either player is negative, it is invalid
    check_not_negative(sets_a, sets_b)

    # If the number of games won is above best_out_of_n_sets, since the "index" starts at zero, it is also an invalid
    # This means it is PAST the best_out_of_n_sets, which returns 1 since player A won
    if sets_a > best_out_of_n_sets or sets_b > best_out_of_n_sets:
        raise InvalidInput


def check_not_negative(*numbers: int):
    """Checks that all numbers passed in are **not** negative.

    Args:
        numbers:
            The numbers to check that they are not negative.

    Raises:
        NegativeNumber:
            As soon as a number is encountered that is negative in the `numbers` argument.
    """

    for num in numbers:
        if num < 0:
            raise NegativeNumber
