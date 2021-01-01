import pytest
from tennis_probability import set, InvalidInput, InvalidProbability


def test_set():
    # Test valid inputs
    # Don't have any to compare with - yet!
    assert set(0, 0, 0) == 0
    assert set(0, 0, 0.50) == 0.5
    assert set(0, 0, 1) == 1

    # assert round(set(2, 1, 0.78), 10) == 0.981006095
    # assert round(set(3, 2, 0.13), 10) == 0.1490010339

    # Test invalid inputs
    with pytest.raises(InvalidInput):
        set(10, 3, 0.2)
    with pytest.raises(InvalidInput):
        set(2, 812, 0.5)
    with pytest.raises(InvalidInput):
        set(5, 5, 0.51)
    with pytest.raises(InvalidInput):
        set(-1, 0, 0.9)

    # Test invalid probabilities
    with pytest.raises(InvalidProbability):
        set(2, 3, 1.0001)
    with pytest.raises(InvalidProbability):
        set(1, 0, -1.001)