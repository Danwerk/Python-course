import pytest
import solution


def test_part1_zero():
    input_amount = 0
    res = solution.generate_list(input_amount, "int")
    expected_len = 0
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


def test_part1_int_correct_data_types():
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, int)


def test_part2_get_max():
    input_amount = 5
    res = solution.generate_combined_list([(3, 'int'), (5, 'int'), (4, 'int')])
    assert len(res) == input_amount
