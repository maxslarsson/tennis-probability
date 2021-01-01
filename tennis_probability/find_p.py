from .check import check_probability
from .match import match


def find_p(probability: float, accuracy_threshold: float) -> float:
    """This functions finds the p value from the probability of winning a game.

    This p value is later used for all other functions to calculate the probability of winning. This is calculated using
    binary search. This assumes that the probability passed in is the probability of winning the entire match, with 0
    points played.

    Args:
        probability:
            The probability of player A winning the entire match.
        accuracy_threshold:
            The threshold of when to stop looking for the p value. Looks for the p value while `high - low > accuracy_threshold.`
            For example, a threshold of 0.001 would make sure that three first three digits of the p value is correct,
            meaning that if the p value is 0.51, it would get 0.510 and then an arbitrary amount of follow up numbers.
            After running this once with a threshold of 0.001 and a p value of 0.51, the function returned 0.51025390625.

    Raises:
        InvalidProbability:
            When the probability is invalid.

    Returns:
        A p value that is withing `accuracy_threshold` of the real midpoint. If the search stops due to the threshold being reached,
        the mid is returned. In other words, the average of the high and low of the binary search is returned.
    """
    # Verifies that the probability is valid
    check_probability(probability)

    # When p is 0, the probability of winning is also 0
    # Therefore the lowest in binary search to start is 0
    low = 0
    # When p is 1, the probability of winning is also 1
    # Therefore the highest in binary search to start is 1
    high = 1
    # The midpoint is going to be halfway in between, starting at 0.5 since the low is 0 and the high is 1
    mid = 0.5

    while high - low > accuracy_threshold:
        # These two checks take a while and the probability of it being *exactly* low or high is extremely low.
        # It *can* more efficient to just run binary search. The `match` function is run three times, but if these
        # two checks are removed it would nly be run once per iteration.

        if probability == match(0, 0, low):
            return low
        elif probability == match(0, 0, high):
            return high

        prob_mid = match(0, 0, mid)

        # If probability is greater, ignore left half
        if prob_mid < probability:
            low = mid

        # If probability is smaller, ignore right half
        elif prob_mid > probability:
            high = mid

        # If it is neither gretar than or less than mid, it IS mid
        # This means our target probability is mid, so return it
        else:
            return mid

        # Recalculate mid at the end of the function
        mid = (high + low) / 2

    # If accuracy_threshold is reached return the middle point in between the high and the low
    return mid
