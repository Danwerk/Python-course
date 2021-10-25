"""Test ex08 functions."""


import pytest
import solution


def test_student_study_none():
    """Test the result is not None."""
    assert solution.students_study(22, False) is not None


def test_student_evening_coffee_true():
    """Test the result even the drinking coffee is true."""
    assert solution.students_study(20, True)


def test_student_evening_coffee_false():
    """Test the result even the drinking coffee in the evening is false."""
    assert solution.students_study(20, False)


def test_student_night_coffee_true():
    """Test the result even the drinking coffee in the night is false."""
    assert solution.students_study(3, False) is not True


def test_student_night_coffee_false():
    """Test the result even the drinking coffee in the night is true."""
    assert solution.students_study(3, True) is not True


def test_student_day_coffee_true():
    """Test the result even the drinking coffee in the midday is true."""
    assert solution.students_study(6, True)


def test_student_day_coffee_false():
    """Test the result even the drinking coffee in the midday is false."""
    assert solution.students_study(6, False) is not True


def test_student_evening_edge_case_coffee_true():
    """Evening edge case, drinking the coffee is true."""
    assert solution.students_study(24, True)
    assert solution.students_study(18, True)


def test_student_evening_edge_case_coffee_false():
    """Evening edge case, drinking the coffee is false."""
    assert solution.students_study(24, False)
    assert solution.students_study(18, False)


def test_student_night_edge_case_coffee_true():
    """Night edge case, drinking the coffee is false."""
    assert solution.students_study(4, False) is not True
    assert solution.students_study(1, False) is not True


def test_student_night_edge_case_coffee_false():
    """Night edge case, drinking the coffee is true."""
    assert solution.students_study(4, True) is not True
    assert solution.students_study(1, True) is not True


def test_student_day_edge_case_coffee_true():
    """Day edge case, drinking the coffee is true."""
    assert solution.students_study(17, True)
    assert solution.students_study(5, True)


def test_student_day_edge_case_coffee_false():
    """Day edge case, drinking the coffee is false."""
    assert solution.students_study(17, False) is not True
    assert solution.students_study(5, False) is not True


def test_lottery_all_fives():
    assert solution.lottery(5, 5, 5)


def test_lottery_all_same_positive():
    assert solution.lottery(3, 3, 3)