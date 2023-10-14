# pylint: disable=C0103
"""
Rearrange Array Elements
"""


def rearrange_digits(input_list):
    """
    Rearrange array elements so as to form
    two number such that their sum is maximum.
    :param input_list:
    :return:
    """
    # Edge cases of empty list or list with one element
    if len(input_list) <= 1:
        return input_list

    # Merge sort
    def merge_sort(arr):
        """
        Merge sort
        :param arr:
        :return:
        """
        # If array is empty or has one element, return
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort left and right halves
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)

    # Merge two arrays
    def merge(left, right):
        """
        Merge two arrays
        :param left:
        :param right:
        :return:
        """
        merged = []
        left_index = 0
        right_index = 0

        # Merge left and right arrays while they are not empty
        while left_index < len(left) and right_index < len(right):
            if left[left_index] > right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Add remaining elements
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

    # Start making calls for parent function

    # Sort input list
    sorted_list = merge_sort(input_list)

    num1 = 0
    num2 = 0

    # Loop through sorted list and create two numbers
    for i, digit in enumerate(sorted_list):
        if i % 2 == 0:
            num1 = num1 * 10 + digit
        else:
            num2 = num2 * 10 + digit

    return [num1, num2]


def test_function(test_case):  # pylint: disable=W0621
    """
    Test function
    :param test_case:
    :return:
    """
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

# Added Test Case
test_function([[], []])
