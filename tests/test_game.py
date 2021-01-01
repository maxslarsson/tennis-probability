import pytest
from tennis_probability import game, InvalidInput, InvalidProbability


def test_game():
    # Test valid inputs
    assert round(game(0, 0, 0.51), 10) == 0.5249850076
    assert round(game(2, 1, 0.78), 10) == 0.981006095
    assert round(game(3, 2, 0.13), 10) == 0.1490010339

    # Test invalid inputs
    with pytest.raises(InvalidInput):
        game(10, 3, 0.2)
    with pytest.raises(InvalidInput):
        game(2, 812, 0.5)
    with pytest.raises(InvalidInput):
        game(3, 3, 0.51)
    with pytest.raises(InvalidInput):
        game(-1, 0, 0.9)

    # Test invalid probabilities
    with pytest.raises(InvalidProbability):
        game(2, 3, 1.0001)
    with pytest.raises(InvalidProbability):
        game(1, 0, -1.001)
