"""KT4."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    ret = []
    for i in str(nr):
        ret.append(int(i))
    return ret


# print(two_digits_into_list(11))  # [1, 1]
# print(two_digits_into_list(71))  # [7, 1]


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_before_and_after_last_three([1, 3, 7]) -> 8
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_before_and_after_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    pass


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    chars = set()
    ret = {}
    if s == '':
        return 0

    for i in s:
        chars.add(i)

    return max(s.count(c) for c in chars)


# print(max_block("hoopla"))  # 2
# print(max_block("abbCCCddBBBxx"))  # 3
# print(max_block(""))  # 0


def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    ret = {}
    if pairs == []:
        return ret

    for i in pairs:
        if '>' in i:
            k = i.split('>')[0]
            v = i.split('>')[-1]
            if k not in ret:
                ret[k] = [v]
            else:
                if v in ret[k]:
                    continue
                else:
                    ret[k].append(v)
        elif '<' in i:
            k = i.split('<')[-1]
            v = i.split('<')[0]
            if k not in ret:
                ret[k] = [v]
            else:
                if v in ret[k]:
                    continue
                else:
                    ret[k].append(v)

    return ret

print(create_dictionary_from_directed_string_pairs([]))  # {}
print(create_dictionary_from_directed_string_pairs(["aasdfa>basdfb", "aa>cc"]))  # {"a": ["b", "c"]}
print(create_dictionary_from_directed_string_pairs(["a>b", "a<b"]))  # {"a": ["b"], "b": ["a"]}
print(create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]))  # {"1": ["1", "2"]}
