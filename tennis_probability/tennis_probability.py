from .errors import InvalidProbability, InvalidScore, InvalidGamesWon


def game(score_a: int, score_b: int, p: float) -> float:
    """Recursively calculates the probability of player A winning at any state in a game.

    Args:
        score_a:
            The score for player A.
        score_b:
            The score for player B.
        p:
            The independent probability of player A winning any given point.

    Raises:
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


def set(
    games_won_a: int,
    games_won_b: int,
    p: float,
    score_a: int = 0,
    score_b: int = 0,
) -> float:
    """Recursively calculates the probability of player A winning at any state in a set.

    This models a set played without a tie-breaker such as in the French Open, where the player needs to win a set with at least a margin of two games.

    Args:
        games_won_a:
            The number of games won for player A
        games_won_b:
            The number of games won for player B.
        p:
            The independent probability of player A winning any given point.
        score_a:
            The score for player A for the current game.
        score_b:
            The score for player B for the current game.

    Raises:
        InvalidScore:
            When the starting score for the players is invalid - arguments `starting_score_a` and `games_b`.
        InvalidProbability:
            When the probability is invalid - the `p` argument.

    Returns:
        The probability of player A winning the set.
    """

    check_games(games_won_a, games_won_b)
    check_score(score_a, score_b)
    check_probability(p)

    # If player A has won
    # Then the probability of player A winning is 1
    if games_won_a == 6:
        return 1

    # If player B has won
    # Then the probability of player A winning is 0
    if games_won_b == 6:
        return 0

    p_game = game(score_a, score_b, p)

    # If the game is in the recurring state - meaning that they are tied
    if games_won_a == 4 and games_won_b == 4:
        return (p_game ** 2) / (1 - 2 * p_game + 2 * (p_game ** 2))

    # If player A has "advantage" - meaning that player A has won one game and needs to win one more to win
    if games_won_a == 5 and games_won_b == 4:
        return p_game * set(games_won_a + 1, games_won_b, p) + (1 - p_game) * game(
            games_won_a - 1, games_won_b, p
        )

    # If player A has a "disadvantage." In other words, player B has an "advantage"
    # In other words, player B has won one game and needs to win one more to win
    if games_won_a == 4 and games_won_b == 5:
        return (1 - p_game) * game(games_won_a, games_won_b + 1, p) + p_game * game(
            games_won_a, games_won_b - 1, p
        )

    # Otherwise, it is any other state in the game
    return p_game * game(games_won_a + 1, games_won_b, p) + (1 - p_game) * game(
        games_won_a, games_won_b + 1, p
    )


def check_probability(p: float):
    """Checks the validity of the probability of winning any given point.

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
    """Verify the validity of the player scores.

    Args:
        score_a:
            The score for player A.
        score_b:
            The score for player B.

    Raises:
        InvalidScore:
            When the score for the players is invalid - arguments `games_won_a` and `games_won_b`.
    """
    # If either score is negative, it is invalid
    if score_a < 0 or score_b < 0:
        raise InvalidScore
    # If either score is above 4, it is also an invalid score
    if score_a > 4 or score_b > 4:
        raise InvalidScore
    # A score of 3 for both players or above is invalid
    if score_a >= 3 and score_b >= 3:
        raise InvalidScore


def check_games(games_a: int, games_b: int):
    """Verify the validity of the number of games won.

    Args:
        games_a:
            The score for player A.
        games_b:
            The score for player B.

    Raises:
        InvalidGamesWon:
            When the score for the players is invalid - arguments `games_won_a` and `games_won_b`.
    """
    # If either score is negative, it is invalid
    if games_a < 0 or games_b < 0:
        raise InvalidGamesWon
    # If either score is above 4, it is also an invalid score
    if games_a > 4 or games_b > 4:
        raise InvalidGamesWon
    # A score of 3 for both players or above is invalid
    if games_a >= 3 and games_b >= 3:
        raise InvalidGamesWon
