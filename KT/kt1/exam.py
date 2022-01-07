"""KT1."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if s == '':
        return ''
    else:
        return s[0].upper() + s[1:]


def has_seven(nums):
    """
    Given a list if ints, return True if the value 7 appears.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return False
    else:
        for j in range(len(nums)):
            if nums[j] == 7:
                count += 1
                if count == 3:
                    return True
        return False


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], [], []]
    """
    ret = []
    if initial_list == []:
        return [[] for i in range(amount)]
    else:
        for i in range(amount):
            k = (len(initial_list) + factor) % len(initial_list)
            initial_list = initial_list[k::] + initial_list[:k:]
            ret.append(initial_list)
    return ret

print(list_move(["a", "b", "c"], 3, 0))  # [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']])
print(list_move(["a", "b", "c"], 3, 1))  # [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
print(list_move([1, 2, 3], 3, 2))  # [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
print(list_move([1, 2, 3], 4, 1))  # [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
print(list_move([], 4, 4))  # [[], [], []]


def parse_call_log(call_log: str) -> dict:
    """
    Parse calling logs to find out who has been calling to whom.

    There is a process, where one person calls to another,
    then this another person call yet to another person etc.
    The log consists of several those call-chains, separated by comma (,).
    One call-chain consists of 2 or more names, separated by colon (:).

    The function should return a dict where the key is a name
    and the value is all the names the key has called to.

    Each name has to be in the list only once.
    The order of the list or the keys in the dictionary are not important.

    Input:
    - consists of 0 or more "chains"
    - chains are separated by comma (,)
    - one chain consists of 2 or more names
    - name is 1 or more symbols long
    - there are no commas nor colons in the name
    - names are separated by colon (:)

    parse_call_log("") => {}
    parse_call_log("ago:kati,mati:malle") => {"ago": ["kati"], "mati": ["malle"]}
    parse_call_log("ago:kati,ago:mati,ago:kati") => {"ago": ["kati", "mati"]}
    parse_call_log("ago:kati:mati") => {"ago": ["kati"], "kati": ["mati"]}
    parse_call_log("mati:kalle,kalle:malle:mari:juri,mari:mati") =>
    {'mati': ['kalle'], 'kalle': ['malle'], 'malle': ['mari'], 'mari': ['juri', 'mati']}

    :param call_log: the whole log as string
    :return: dictionary with call information
    """
    if call_log == '':
        return {}
    call_dict = {}
    string_list = call_log.split(',')
    for names in string_list:
        names_list = names.split(':')
        names = names.split(':')
        for name in names_list:
            name = names[0]
            some_list = []
            if len(names) >= 2:
                some_list.append(names[0])
                some_list.append(names[1])
                names.remove(names[0])
                name = some_list[0]
                name1 = some_list[1]
                if name not in call_dict:
                    call_dict[name] = [name1]
                if name1 in call_dict[name]:
                    continue
                else:
                    call_dict[name].append(name1)
            else:
                continue
    return call_dict
