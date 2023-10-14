# pylint: disable=C0103
"""
Max and Min in a Unsorted Array
"""
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # If the list is empty, return None
    if len(ints) == 0:
        return None

    # Initialize min and max to first element
    min_element = max_element = ints[0]

    # Iterate list and compare each element to min and max,
    # updating if necessary
    for num in ints:
        if num < min_element:
            min_element = num
        elif num > max_element:
            max_element = num

    return min_element, max_element


# Example Test Case

test_list = list(range(0, 10))  # a list containing 0 - 9
random.shuffle(test_list)

print("Pass" if ((0, 9) == get_min_max(test_list)) else "Fail")

# Test Case 2: Empty list, should return None
empty_list = []
assert None is get_min_max(empty_list)

# Test Case 3: List with a single element
single_element_list = [42]
assert (42, 42) == get_min_max(single_element_list)

# Test Case 4: List with large numbers
large_numbers_list = [1000000, 1000000000, 100, 999999]
assert (100, 1000000000) == get_min_max(large_numbers_list)

# Test Case 5: List with negative numbers
negative_numbers_list = [-5, -1, -10, -2]
assert (-10, -1) == get_min_max(negative_numbers_list)
