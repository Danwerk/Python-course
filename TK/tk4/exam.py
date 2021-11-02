"""TK 4."""


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.

    Both lists will be length 1 or more.

    common_end([1, 2, 3], [7, 3]) → True
    common_end([1, 2, 3], [7, 3, 2]) → False
    common_end([1, 2, 3], [1, 3]) → True
    :param a: List of integers.
    :param b: List of integers.
    :return: The last or the first elements are the same.
    """
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False


def near_ten(nr):
    """
    Given a non-negative number "num", return True if num is within 2 of a multiple of 10.

    near_ten(0) →  True
    near_ten(3) →  False
    near_ten(10) →  True
    near_ten(23) →  False
    near_ten(198) →  True

    :param nr: non-negative integer.
    :return: True if num is within 2 of a multiple of 10.
    """
    if (nr + 2) % 10 == 0 or (nr + 1) % 10 == 0 or (nr + 0) % 10 == 0:
        return True
    else:
        return False


def middle_chars(s: str) -> str:
    """Return two chars in the middle of string.

    The length of the string is an even number.

    middle_chars("abcd") => "bc"
    middle_chars("bc") => "bc"
    middle_chars("aabbcc") => "bb"
    middle_chars("") => ""
    """
    if s == '':
        return ''
    else:
        f_char = int((len(s) / 2) - 1)
        s_char = int((len(s) / 2))
        return s[f_char] + s[s_char]

print(middle_chars("abcdef"))

def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    pass


def max_duplicate(nums):
    """
    Return the largest element which has at least one duplicate.

    If no element has duplicate element (an element with the same value), return None.

    max_duplicate([1, 2, 3]) => None
    max_duplicate([1, 2, 2]) => 2
    max_duplicate([1, 2, 2, 1, 1]) => 2

    :param nums: List of integers
    :return: Maximum element with duplicate. None if no duplicate found.
    """
    pass
