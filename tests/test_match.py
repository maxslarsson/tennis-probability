import pytest
from tennis_probability import match, InvalidInput, InvalidProbability, NegativeNumber


def test_match():
    assert match(0, 0, 0) == 0
    assert match(0, 0, 0.50) == 0.5
    assert match(0, 0, 1) == 1

    # Test valid inputs
    assert match(2, 1, 0.91) == 1.0
    assert match(1, 0, 0.38) == 0.0012392424927120083
    assert match(2, 2, 0.51) == 0.573396584031171

    # Test invalid inputs
    with pytest.raises(InvalidInput):
        match(10, 3, 0.2)
    with pytest.raises(InvalidInput):
        match(2, 812, 0.5)
    with pytest.raises(InvalidInput):
        match(5, 5, 0.51)
    with pytest.raises(NegativeNumber):
        match(-1, 0, 0.9)

    # Test invalid probabilities
    with pytest.raises(InvalidProbability):
        match(2, 3, 1.0001)
    with pytest.raises(InvalidProbability):
        match(1, 0, -1.001)
