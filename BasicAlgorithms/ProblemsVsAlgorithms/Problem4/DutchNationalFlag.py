# pylint: disable=C0103
"""
Dutch National Flag Problem
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2,
    sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # 0s pointer
    left_ptr = 0
    # 2s pointer
    right_ptr = len(input_list) - 1
    # Current pointer
    current_ptr = 0

    # Loop through the list
    while current_ptr <= right_ptr:
        # If current element is 0, swap with left pointer
        if input_list[current_ptr] == 0:
            input_list[left_ptr] = input_list[current_ptr]
            input_list[current_ptr] = input_list[left_ptr]
            # Increment left and current pointers
            left_ptr += 1
            current_ptr += 1
        # If current element is 2, swap with right pointer
        elif input_list[current_ptr] == 2:
            input_list[right_ptr] = input_list[current_ptr]
            input_list[current_ptr] = input_list[right_ptr]
            # Decrement right pointer
            right_ptr -= 1
        # If current element is 1, move to next element
        else:
            # Increment current pointer
            current_ptr += 1

    return input_list


def test_function(test_case):
    """
    Test function
    :param test_case:
    :return:
    """
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function(
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0,
     2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
)
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Added test cases
test_function([])
test_function([2, 1000, 0, 1, 2, 10000, 1, 0])
test_function([1, 1, 1, 1, 1])
