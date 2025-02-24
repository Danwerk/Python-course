"""Test EX04."""
import solution


def test_part1_zero():
    """Test correct length of empty list."""
    input_amount = 0
    res = solution.generate_list(input_amount, "int")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_big_input():
    """Test correct length if big input is given."""
    input_amount = 100000000
    res = solution.generate_list(input_amount, "int")
    expected_len = 100000000
    assert len(res) == expected_len


def test_part1_int_correct_len():
    """Test correct length of list if data type is int."""
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_float_correct_len():
    """Test correct length of list if data type is float."""
    input_amount = 5
    res = solution.generate_list(input_amount, "float")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_str_correct_len():
    """Test correct length of list if data type is string."""
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_tuple_correct_len():
    """Test correct length of list if data type is tuple."""
    input_amount = 5
    res = solution.generate_list(input_amount, "tuple")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_dict_correct_len():
    """Test correct length of list if data type is dict."""
    input_amount = 5
    res = solution.generate_list(input_amount, "dict")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_set_correct_len():
    """Test correct length of list if data type is set."""
    input_amount = 5
    res = solution.generate_list(input_amount, "set")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_list_correct_len():
    """Test correct length of list if data type is list."""
    input_amount = 5
    res = solution.generate_list(input_amount, "list")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_correct_int_data_types():
    """Test correct int data types."""
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, int)


def test_part2_get_max_int():
    """Test combined list with data type of int."""
    input_amount = 5
    res = solution.generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')])
    assert len(res) == input_amount


def test_part2_get_max_string():
    """Test combined list with data type of string."""
    input_amount = 5
    res = solution.generate_combined_list([(3, 'string'), (5, 'string'), (4, 'string')])
    assert len(res) == input_amount


def test_part2_get_max_float():
    """Test combined list with data type of string."""
    input_amount = 5
    res = solution.generate_combined_list([(3, 'float'), (5, 'float'), (4, 'float')])
    assert len(res) == input_amount


def test_part2_bigger_numbers():
    """Test combined list with bigger numbers."""
    input_amount = 10000
    res = solution.generate_combined_list([(3, 'int'), (10000, 'int'), (4, 'int')])
    assert len(res) == input_amount


def test_part2_empty_list():
    """Test combined list returns empty list."""
    input_amount = 0
    res = solution.generate_combined_list([(0, 'int'), (0, 'int'), (0, 'int')])
    assert len(res) == input_amount


def test_part2_correct_types_list():
    """Test combined list returns correct data types."""
    res = solution.generate_combined_list([(1, 'string'), (2, 'string'), (3, 'string')])
    for element in res:
        assert isinstance(element, str)


def test_part3_empty_list():
    """Test combined list unique returns empty list."""
    input_amount = 0
    res = solution.generate_combined_list_unique([(0, 'string'), (0, 'string'), (0, 'string')])
    assert len(res) == input_amount


def test_part3_list_too_big():
    """Test combined list unique contains big amount of some datatype."""
    input_amount = 10000
    res = solution.generate_combined_list_unique([(2, 'string'), (3, 'string'), (10000, 'string')])
    assert len(res) == input_amount


def test_part3_correct_types_list():
    """Test combined list unique correct data types."""
    res = solution.generate_combined_list_unique([(5, 'int'), (6, 'string'), (7, 'string')])
    for element in res:
        assert isinstance(element, str) or isinstance(element, int)


def test_part3_smaller_numbers():
    """Test combined list unique small numbers."""
    input_amount = 5
    res = solution.generate_combined_list_unique([(5, 'string'), (2, 'string'), (3, 'string')])
    assert len(res) == input_amount


def test_part3_unique_ints():
    """Test combined list unique contains unique ints."""
    res = solution.generate_combined_list_unique([(5, 'int'), (2, 'int'), (3, 'int')])
    for i in range(len(res) - 1):
        assert res[i] != res[i + 1]


def test_part3_unique_floats():
    """Test combined list unique contains unique floats."""
    res = solution.generate_combined_list_unique([(5, 'float'), (2, 'float'), (3, 'float')])
    for i in range(len(res) - 1):
        assert res[i] != res[i + 1]


def test_part3_unique_string():
    """Test combined list unique contains unique strings."""
    res = solution.generate_combined_list_unique([(5, 'string'), (2, 'string'), (3, 'string')])
    for i in range(len(res) - 1):
        assert res[i] != res[i + 1]
