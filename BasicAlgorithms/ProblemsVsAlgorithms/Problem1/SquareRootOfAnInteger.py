# pylint: disable=C0103
"""
Square Root of an Integer
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # If number is 0 or 1, return that number
    if number in (0, 1):
        return number

    # Binary search
    start, end = 0, number

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        if mid * mid < number:
            start = mid + 1
        else:
            end = mid - 1

    return end


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (-1 == sqrt(-1)) else "Fail")
