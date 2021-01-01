import pytest
from tennis_probability import game, InvalidInput, InvalidProbability, NegativeNumber


def test_game():
    assert game(0, 0, 0) == 0
    assert game(0, 0, 0.50) == 0.5
    assert game(0, 0, 1) == 1

    # Test valid inputs
    assert game(0, 0, 0.51) == 0.5249850075968013
    assert game(2, 1, 0.78) == 0.9810060950060902
    assert game(3, 2, 0.13) == 0.14900103385887828

    # Test invalid inputs
    with pytest.raises(InvalidInput):
        game(10, 3, 0.2)
    with pytest.raises(InvalidInput):
        game(2, 812, 0.5)
    with pytest.raises(InvalidInput):
        game(3, 3, 0.51)
    with pytest.raises(NegativeNumber):
        game(-1, 0, 0.9)

    # Test invalid probabilities
    with pytest.raises(InvalidProbability):
        game(2, 3, 1.0001)
    with pytest.raises(InvalidProbability):
        game(1, 0, -1.001)
