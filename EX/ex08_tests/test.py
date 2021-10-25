import pytest
import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_float_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "float")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_str_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_int_correct_data_types():
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, int)
