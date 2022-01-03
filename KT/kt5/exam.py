"""KT5."""


def get_date_string(date: list) -> str:
    """
    Pretty print the date.

    You are given a list with three numbers where:
    1. First number is day number.
    2. Second number is month number.
    3. Third number is year number.

    Assume that all numbers are always in correct ranges.

    Return the pretty version of the date following the format:
    "The date is -> {day number}/{month number}/{year number}"

    If the list is empty or its length is not 3, return "The date is unknown!"

    print_date([3, 3, 2000]) -> "The date is -> 3/3/2000"
    print_date([20, 12, 5677]) -> "The date is -> 20/12/5677"
    print_date([2, 2, 3, 200]) -> "The date is unknown!"
    print_date([]) -> "The date is unknown!"

    :param date: Input list with day, month and year numbers.
    :return: Pretty version of this date.
    """
    if len(date) != 3:
        return f'The date is unknown!'
    else:
        return f'The date is -> {date[0]}/{date[1]}/{date[2]}'


# print(get_date_string([3, 3, 2000]))  # "The date is -> 3/3/2000"
# print(get_date_string([20, 12, 5677]))  # "The date is -> 20/12/5677"
# print(get_date_string([2, 2, 3, 200]))  # "The date is unknown!"
# print(get_date_string([]))  # "The date is unknown!"


def odd_sums_of_consecutive_elements(nums: list) -> list:
    """
    Return list of odd sums of consecutive elements.

    Consider all consecutive elements in the input list. Return a list of all the odd sums of consecutive elements.

    odd_sums_of_consecutive_elements([1, 2, 3, 5]) => [3, 5]
    odd_sums_of_consecutive_elements([8, 10]) => []
    odd_sums_of_consecutive_elements([9]) => []
    odd_sums_of_consecutive_elements([11, 8]) => [19]

    :param nums:
    :return:
    """
    ret = []

    for i in range(len(nums) - 1):
        sum = nums[i] + nums[i + 1]
        if sum % 2 != 0:
            ret.append(sum)
        else:
            continue
    return ret


# print(odd_sums_of_consecutive_elements([1, 2, 3, 5]))  # [3, 5]
# print(odd_sums_of_consecutive_elements([8, 10]))  # []
# print(odd_sums_of_consecutive_elements([9]))  # []
# print(odd_sums_of_consecutive_elements([11, 8]))  # [19]


def g_happy(s: str) -> bool:
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    ret = set()
    if s == 'g' or s == '':
        ret.add('unhappy')
    else:
        if len(s) == 2:
            if s[0] == 'g' and s[1] != 'g' or s[0] != 'g' and s[1] == 'g':
                ret.add('unhappy')
            elif s[0] == 'g' and s[1] == 'g':
                ret.add('happy')
        else:
            if s[0] == 'g' and s[1] != 'g':
                ret.add('unhappy')
            if s[-1] == 'g' and s[-2] != 'g':
                ret.add('unhappy')

            for i in range(1, len(s) - 1):
                if s[i] == s[i + 1] == 'g' or s[i] == s[i - 1] == 'g':
                    ret.add('happy')
                elif s[i] == 'g' and s[i + 1] != 'g':
                    ret.add('unhappy')
                elif s[i] == 'g' and s[i - 1] != 'g':
                    ret.add('unhappy')

    if 'unhappy' not in ret:
        return True
    else:
        return False


print(g_happy("xxggxx"))  # True
print(g_happy("xg"))  # False
print(g_happy("xxgggxgx"))  # False
print(g_happy("xxggyygxx"))  # False
print(g_happy("ggggggggxgg"))  # True


def merge_dictionary_paths(houses: dict, families: dict) -> dict:
    """
    Merge two dictionaries where one value indicates to another key.

    One dictionary represents houses and their families.
    The key is the house and the values are families under that house.

    The second dictionary represents family members.
    They key is the family and the values are the names.

    The order inside one house is important.
    First all the members from the first family are taken, then all the members from the second family etc.

    The same family can be under several houses.
    The same member cab be under several families.

    houses:
    {
    "Stark": ["Stark", "Tully"],
    "Lannisters": ["Lannister"],
    "Ago": ["Luberg"]
    }

    families:
    {
    "Stark": ["Eddard", "Robb"],
    "Tully": ["Catelyn"],
    "Lannister": ["Tywin"]
    }

    Result:
    {
    "Stark": ["Eddard", "Robb", "Catelyn"],
    "Lannisters": ["Tywin"]
    }

    Example:

    houses: {"h1": ["a", "b"], "h2": ["b", "c"]}
    families: {"a": ["m", "n"], "b": ["k"], "c": ["x", "y"]}

    Result:
    {
    "h1": ["m", "n", "k"], "h2": ["k", "x", "y"]
    }
    """
    # ret = {}
    # for k, v in houses.items():
    #     for i in houses[k]:
    #         if i in families:
    #             if k not in ret:
    #                 ret[k] = families[i]
    #             else:
    #                 ret[k].extend(families[i])
    # return ret
    i = 0

print(merge_dictionary_paths({"h1": ["a", "b"], "h2": ["b", "c"]}, {"a": ["m", "n"], "b": ["k"], "c": ["x", "y"]}))
# print(merge_dictionary_paths({
#     "Stark": ["Stark", "Tully"],
#     "Lannisters": ["Lannister"],
#     "Ago": ["Luberg"]
#     },
#     {
#     "Stark": ["Eddard", "Robb"],
#     "Tully": ["Catelyn"],
#     "Lannister": ["Tywin"]
#     }
# ))
