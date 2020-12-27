from typing import Literal

from .errors import InvalidProbability, InvalidScore

# Change from 'int' to Score
def match(score_a: int, score_b: int, p: float) -> float:
    """Recursively calculate the probability of player A winning at any state in the match.

    Args:
        score_a:
            The score for player A.
        score_b:
            The score for player B.
        p:
            The independent probability of player A winning any given point.

    Raises:
        InvalidScore:
            When the score for the players is invalid - arguments `score_a` and `score_b`.
        InvalidProbability:
            When the probability is invalid - the `p` argument.

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
        return p * match(score_a + 1, score_b, p) + (1 - p) * match(
            score_a - 1, score_b, p
        )

    # If player A has disadvantage
    # In other words, player B has an advantage
    if score_a == 2 and score_b == 3:
        return (1 - p) * match(score_a, score_b + 1, p) + p * match(
            score_a, score_b - 1, p
        )

    # Otherwise, it is any other state in the game
    return p * match(score_a + 1, score_b, p) + (1 - p) * match(score_a, score_b + 1, p)


def check_probability(p: float):
    """Checks the validity of the probability of winning any given point.

    Args:
        p:
            The independent probability of player A winning any given point.

    Raises:
        InvalidProbability:
            When the probability is invalid - the `p` argument.
    """

    # Argument p is invalid if it is less than 0.0 or greater than 1.0
    if p < 0 or p > 1:
        raise InvalidProbability(p)


def check_score(score_a: int, score_b: int):
    """Verify the validity of the player scores.

    Args:
        score_a:
            The score for player A.
        score_b:
            The score for player B.

    Raises:
        InvalidScore:
            When the score for the players is invalid - arguments `score_a` and `score_b`.
    """
    # If either score is negative, it is invalid
    if score_a < 0 or score_b < 0:
        raise InvalidScore
    # If either score is above 4, it is also an invalid score
    if score_a > 4 or score_b > 4:
        raise InvalidScore
    # A score of 3 for both players or above is invalid
    if score_a >= 3 and score_b >= 3:
        raise InvalidScore(f"Score A: {score_a!r}, Score B: {score_b!r}")
