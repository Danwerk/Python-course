"""Lists."""


def generate_list(amount: int, data_type: str) -> list:
    """Return a list with amount elements of type data_type."""
    elem_list = []
    for i in range(amount):
        if data_type == 'list':
            elem_list.append([i])
        elif data_type == 'string':
            elem_list.append('i')
        elif data_type == 'int':
            elem_list.append(i)
        elif data_type == 'float':
            elem_list.append(float(i))
        elif data_type == 'tuple':
            elem_list.append((i, i))
        elif data_type == 'set':
            elem_list.append({i})
        elif data_type == 'dict':
            elem_list.append({i: i})
    return elem_list


def generate_combined_list(inputs: list) -> list:
    """Write a function that returns a list with the minimal possible length."""
    output_list = []
    amount_dict = {}

    for tupl in inputs:
        amount = tupl[0]
        data_type = tupl[1]
        if data_type in amount_dict:
            if amount_dict[data_type] < amount:
                amount_dict[data_type] = amount
        else:
            amount_dict[data_type] = amount

    for data_type, amount in amount_dict.items():
        output_list.extend(generate_list(amount, data_type))

    return output_list


def generate_combined_list_unique(inputs: list) -> list:
    """Write a function that returns a list with the minimal possible length."""

    return generate_combined_list(inputs)




print(generate_combined_list([(3, 'int'), (5, 'int')]))
print(generate_combined_list_unique([(3, 'int'), (5, 'int')]))  # [1, 2, 3, 4, 5]
print(generate_combined_list_unique([(2, 'int'), (2, 'float'), (1, 'int')]))
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
