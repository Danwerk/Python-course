"""Lists."""


def generate_list(amount: int, data_type: str) -> list:
    """Return a list with amount elements of type data_type."""
    dictionary = {
        'list': [],
        'set': set(),
        'tuple': tuple,
        'dict': dict,
        'string': '',
        'float': 3.14,
        'int': 5
    }
    result_list = [dictionary[data_type]] * amount
    return result_list


def generate_combined_list(inputs: list) -> list:
    """
    Write a function that returns a list with the minimal possible length, that still satisfies the criteria below.

    Every element of 'inputs' is a tuple (int amount, string data_type).
    For each element of 'inputs', it must be true that the returned list contains at least 'amount' of elements of type 'data_type'.
    """
    '''
    for i in inputs:
        if inputs != 'int':
            return generate_list(inputs)

        min_list = (max(inputs))
        return generate_list(min_list[0], min_list[1])
'''
print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [0, 0, 0, 0, 0]
print(generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')]))  # [100, 80, 60, 40, 20]
'''
if __name__ == '__main__':
    # The given outputs are only some of possible outputs, for example for (3, 'string') in the first part an output of ["kass", "koer", "kana"] would also work.

    # Part 1
    print(generate_list(2, 'set'))  # [set(), set()]
    print(generate_list(3, 'string'))  # ["a", "kass", "a"]
    print(generate_list(1, 'list'))  # [[]]
    print(generate_list(5, 'int'))  # [1, 2, 3, 3, 3]
    print()

    # Part 2
    print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list([(3, 'int'), (5, 'int')]))  # [0, 0, 0, 0, 0]
    print(generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')]))  # [100, 80, 60, 40, 20]
    print(generate_combined_list([(2, 'list'), (3, 'string')]))  # ["a", [], "a", [], "a"]
    print(generate_combined_list([(2, 'float'), (3, 'dict')]))  # [{}, {}, {}, 3.14, 3.15]
    print()

    # Part 3
    print(generate_combined_list_unique([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique([(2, 'int'), (2, 'float'), (1, 'int')]))  # [43, 93, 4.3, 2.1]
    print()

    # Part 4
    print(generate_combined_list_unique_advanced([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
    print(generate_combined_list_unique_advanced([(2, 'list'), (3, 'string')]))  # ["a", [2], "asd", [], "abc"]
    print(
        generate_combined_list_unique_advanced([(2, 'float'), (3, 'dict')]))  # [{3: "abd"}, {"a": "a"}, {}, 3.14, 3.15]
    print()
'''
