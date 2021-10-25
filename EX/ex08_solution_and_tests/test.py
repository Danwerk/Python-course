import pytest
import solution


def test_student_study_none():
    input_amount = None
    res = solution.students_study(0, False)
    assert res == input_amount


def test_student_night_coffee_true():
    assert solution.students_study(20, True)


def test_student_night_coffee_false():
    assert solution.students_study(20, False)

