import pytest
from tennis_probability import set, InvalidInput, InvalidProbability, NegativeNumber


def test_set():
    assert set(0, 0, 0) == 0
    assert set(0, 0, 0.50) == 0.5
    assert set(0, 0, 1) == 1

    # Test valid inputs
    assert set(5, 3, 0.13) == 0.008146509339015371
    assert set(2, 2, 0.37) == 0.024086243446167555
    assert set(4, 1, 0.91) == 0.9999999999999992

    # Test invalid inputs
    with pytest.raises(InvalidInput):
        set(10, 3, 0.2)
    with pytest.raises(InvalidInput):
        set(2, 812, 0.5)
    with pytest.raises(InvalidInput):
        set(5, 5, 0.51)
    with pytest.raises(NegativeNumber):
        set(-1, 0, 0.9)

    # Test invalid probabilities
    with pytest.raises(InvalidProbability):
        set(2, 3, 1.0001)
    with pytest.raises(InvalidProbability):
        set(1, 0, -1.001)
