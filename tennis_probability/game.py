from .check import check_score, check_probability


def game(score_a: int, score_b: int, p: float) -> float:
    """Recursively calculates the probability of player A winning at any state in a game.

    Args:
        score_a:
            The score for player A.
        score_b:
            The score for player B.
        p:
            The independent probability of player A winning any given *point* in a game.

    Raises:
        NegativeNumber:
            When either score is negative.
        InvalidScore:
            When the score for the players is invalid - arguments `games_won_a` and `games_won_b`.
        InvalidProbability:
            When the probability is invalid - the `p_game` argument.

    Returns:
        The probability of player A winning the game.
    """

    check_score(score_a, score_b)
    check_probability(p)

    # If player A has won
    # Then the probability of player A winning is 1
    if score_a == 4:
        return 1

    # If player B has won
    # Then the probability of player A winning is 0
    if score_b == 4:
        return 0

    # If the game is in deuce
    if score_a == 2 and score_b == 2:
        return (p ** 2) / (1 - 2 * p + 2 * (p ** 2))

    # If player A has advantage
    if score_a == 3 and score_b == 2:
        return p * game(score_a + 1, score_b, p) + (1 - p) * game(
            score_a - 1, score_b, p
        )

    # If player A has disadvantage
    # In other words, player B has an advantage
    if score_a == 2 and score_b == 3:
        return (1 - p) * game(score_a, score_b + 1, p) + p * game(
            score_a, score_b - 1, p
        )

    # Otherwise, it is any other state in the game
    return p * game(score_a + 1, score_b, p) + (1 - p) * game(score_a, score_b + 1, p)
