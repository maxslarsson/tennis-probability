from .game import game
from .check import check_games_won, check_probability
from functools import lru_cache


@lru_cache
def set(
    games_won_a: int,
    games_won_b: int,
    p: float,
) -> float:
    """Recursively calculates the probability of player A winning at any state in a set.

    This models a set played without a tie-breaker such as in the French Open, where the player needs to win a set with at least a margin of two games.
    This function calls and uses the `game` function.

    Args:
        games_won_a:
            The number of games won for player A
        games_won_b:
            The number of games won for player B.
        p:
            The independent probability of player A winning any given *point* in a game.

    Raises:
        NegativeNumber:
            When either score is negative.
        InvalidInput:
            When the number of games won for the players is invalid - arguments `games_won_a` and `games_won_b`.
        InvalidProbability:
            When the probability is invalid - the `p` argument.

    Returns:
        The probability of player A winning the set.
    """

    check_games_won(games_won_a, games_won_b)
    check_probability(p)

    # If player A has won
    # Then the probability of player A winning is 1
    if games_won_a == 6:
        return 1

    # If player B has won
    # Then the probability of player A winning is 0
    if games_won_b == 6:
        return 0

    p_game = game(0, 0, p)

    # If the game is in the recurring state - meaning that they are tied
    if games_won_a == 4 and games_won_b == 4:
        return (p_game ** 2) / (1 - 2 * p_game + 2 * (p_game ** 2))

    # If player A has "advantage" - meaning that player A has won one game and needs to win one more to win
    if games_won_a == 5 and games_won_b == 4:
        return p_game * set(games_won_a + 1, games_won_b, p) + (1 - p_game) * set(
            games_won_a - 1, games_won_b, p
        )

    # If player A has a "disadvantage" and player B has an "advantage."
    # In other words, player B has won one game and needs to win one more to win
    if games_won_a == 4 and games_won_b == 5:
        return (1 - p_game) * set(games_won_a, games_won_b + 1, p) + p_game * set(
            games_won_a, games_won_b - 1, p
        )

    # Otherwise, it is any other state in the game
    return p_game * set(games_won_a + 1, games_won_b, p) + (1 - p_game) * set(
        games_won_a, games_won_b + 1, p
    )
