"""KT2."""


def switch_lasts_and_firsts(s: str) -> str:
    """
    Move last two characters to the beginning of string and first two characters to the end of string.

    When string length is smaller than 4, return reversed string.

    switch_lasts_and_firsts("ambulance") => "cebulanam"
    switch_lasts_and_firsts("firetruck") => "ckretrufi"
    switch_lasts_and_firsts("car") => "rac"

    :param s:
    :return: modified string
    """
    if len(s) >= 4:
        return s[-2::] + s[2:-2] + s[0:2]
    elif len(s) < 4:
        return s[::-1]


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    s = ''
    text_length = len(text)
    if leave_count > 0:
        for i in range(0, text_length, leave_count):
            if text == '':
                break
            else:
                text = text.replace(text[0:leave_count], '', 1)
                s += text[:take_count]
                text = text.replace(text[0:take_count], '', 1)
    elif leave_count == 0:
        while text != '':
            s += text[:take_count]
            text = text.replace(text[0:take_count], '', 1)
    return s


print(take_partial("a,d", 1, 1))
print(take_partial("abcdef", 2, 3))  # "cde"
print(take_partial("abcdef", 0, 1))
print(take_partial("abcdef", 1, 0))


def min_diff(nums):
    """
    Find the smallest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1
    min_diff([1, 9, 17]) => 8
    min_diff([100, 90]) => 10
    min_diff([1, 100, 1000, 1]) => 0

    :param nums: list of ints, at least 2 elements.
    :return: min diff between 2 numbers.
    """
    ret = []
    duplicate_list = sorted(nums, reverse=True)
    for i in range(len(nums) - 1):
        minimum = duplicate_list[i] - duplicate_list[i + 1]
        ret.append(minimum)
    return min(ret)


def get_symbols_by_occurrences(text: str) -> dict:
    """
    Return dict where key is the occurrence count and value is a list of corresponding symbols.

    The order of the counts and the symbols is not important.

    get_symbols_by_occurrences("hello") => {1: ['e', 'o', 'h'], 2: ['l']}
    get_symbols_by_occurrences("abcaba") => {2: ['b'], 1: ['c'], 3: ['a']}
    """
    dict = {}
    for w in text:
        count = 1
        if w not in dict:
            dict[w] = count
        else:
            dict[w] = dict[w] + 1
    new_dict = {}
    for i in dict.items():
        key = i[1]
        value = i[0]
        if key not in new_dict:
            new_dict[key] = [value]

        else:
            new_dict[key].append(value)
    return new_dict


print(get_symbols_by_occurrences("abcaba"))
