def generate_list(amount: int, data_type: str) -> list:
    if data_type == 'list':
        return list([[]]) * amount
    elif data_type == 'set':
        return list([set()]) * amount
    elif data_type == 'tuple':
        return list([tuple]) * amount
    elif data_type == 'dict':
        return list([{}]) * amount
    elif data_type == 'string':
        word = 'hehe'
        return list([word]) * amount
    elif data_type == 'float':
        float_num = 3.14
        return list([float_num]) * amount
    elif data_type == 'int':
        int_num = 5
        return list([int_num]) * amount


print(generate_list(2, 'set'))  # [set(), set()]
print(generate_list(2, 'list'))
print(generate_list(2, 'tuple'))
print(generate_list(2, 'dict'))
print(generate_list(2, 'string'))
print(generate_list(2, 'float'))
print(generate_list(2, 'int'))

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