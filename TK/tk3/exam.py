"""TK 3."""

def make_ends(nums: list) -> list:
    """
    Given an array of ints, return a new array length 2 containing the first and last elements from the original array.

    The original array will be length 1 or more.

    make_ends([1, 2, 3]) → [1, 3]
    make_ends([1, 2, 3, 4]) → [1, 4]
    make_ends([7, 4, 6, 2]) → [7, 2]

    :param nums: List of integers.
    :return: List with the first and the last element from the input list.
    """
    return [nums[0], nums[-1]]


def is_sum_of_two(a: int, b: int, c: int) -> bool:
    """
    Whether one parameter is a sum of other two.

    is_sum_of_two(3, 2, 1) => True
    is_sum_of_two(3, 1, 1) => False
    is_sum_of_two(3, 2, 5) => True
    """
    if a == b + c or b == a + c or c == a + b:
        return True
    else:
        return False


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    if len(text) % 2 == 0:
        half_len = len(text) // 2
        return text[0:half_len]


def non_decreasing_list(nums: list) -> bool:
    """
    Given a list of numbers.

    If given list is a non-decreasing list, return True, otherwise False.
    Non-decreasing means every next element in the list must not be smaller than the previous one.

    non_decreasing_list([0, 1, 2, 3, 98]) => True
    non_decreasing_list([50, 49]) => False
    non_decreasing_list([12, 12]) => True

    :param nums:
    :return:
    """
    if len(nums) < 3:
        if nums[1] > nums[0] or nums[1] == nums[0]:
            return True
        else:
            return False
    for i in range(1, len(nums) - 1):
        if [i - 1] < [i] and [i + 1] > [i] or [i - 1] == [i] and [i + 1] == [i]:
            return True
        else:
            return False
print(non_decreasing_list([0, 1, 2, 3, 98]))
print(non_decreasing_list([50, 49]))
print(non_decreasing_list([12, 12]))

def mirror_ends(s: str) -> str:
    """
        Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string.

        In other words, zero or more characters at the very beginning of the given string,
        and at the very end of the string in reverse order (possibly overlapping).

        For example, the string "abXYZba" has the mirror end "ab".

        mirrorEnds("abXYZba") → "ab"
        mirrorEnds("abca") → "a"
        mirrorEnds("aba") → "aba"

        :param s: String
        :return: Mirror image string
        """
    '''
    mirror_string = ''
    for i in range(len(s)):
        if s[0] == s[-1]:
            mirror_string + 

    return s
print(mirror_ends("abXYZba"))

'''