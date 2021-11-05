"""TK5."""


def string_edges(first: str, second: str) -> str:
    """
    Given two strings return a string which consists of the last elements of input strings.

    The strings will have length 1 or more.

    string_edges("a", "b") => "ab"
    string_edges("abc", "def") => "cf"
    """
    return first[-1] + second[-1]


def alarm_clock(day, vacation):
    """
    Return what time the alarm clock should be set.

    Given a day of the week encoded as 0=Mon, 1=Tue, ... 5=Sat, 6=Sun
    and a boolean indicating if we are on vacation,
    return a string of the form "08:00" indicating when the alarm clock should ring.

    Weekdays, the alarm should be "08:00" and on the weekend it should be "10:00".
    Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

    alarm_clock(1, False) → '08:00'
    alarm_clock(3, False) → '08:00'
    alarm_clock(6, False) → '10:00'

    :param day: Day of week.
    :param vacation: Whether it is vacation.
    :return: String when to set alarm clock.
    """
    if 0 <= day <= 4 and vacation is True:
        return '10:00'
    elif 0 <= day <= 4 and vacation is False:
        return '08:00'
    elif 5 <= day <= 6 and vacation is True:
        return 'off'
    elif 0 <= day <= 6 and vacation is False:
        return '10:00'


def combo_string(s1: str, s2: str) -> str:
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    if len(s1) < len(s2):
        return f'{s1 + s2 + s1}'
    else:
        return f'{s2 + s1 + s2}'


def min_diff(nums):
    """
    Find the smaller diff between the first and the last element.

    Diff is a distance (non-negative number) between a value of an element and a value of the element at position of original element value.
    Take diffs for both the first and the last element, return the smaller diff.

    If one index is out of range, then return the diff of other element.
    If both indices are out of range, return -1.

    min_diff([1, 2, 3, 4, 5, 3]) => 1
    min_diff([1, 3, 3, 4, 1, 4]) => 2
    min_diff([0, 1, 2, 0]) => 0
    min_diff([1, 100, 102, 2]) => 99

    min_diff([1, 2, 3]) => 1
    min_diff([79, 2, 0]) => 79
    min_diff([123, 0, 122]) => -1

    :param nums: List of integers.
    :return: Min diff
    """
    pass


def remove_in_middle(text, to_remove):
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    pass
