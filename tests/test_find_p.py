from tennis_probability import find_p, InvalidProbability
from math import isclose
import pytest


accuracy = 1e-9


def test_find_p():
    assert isclose(find_p(0, accuracy), 0)
    assert isclose(find_p(0.50, accuracy), 0.5)
    assert isclose(find_p(1, accuracy), 1)

    assert isclose(find_p(0.6356544165709263, accuracy), 0.51)
    assert isclose(find_p(0.0032343475251863842, accuracy), 0.42)
    assert isclose(find_p(0.999890259155947, accuracy), 0.61)

    # Test invalid probabilities
    with pytest.raises(InvalidProbability):
        find_p(1.0001, accuracy)
    with pytest.raises(InvalidProbability):
        find_p(-1.001, accuracy)
