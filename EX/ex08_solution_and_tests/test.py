import pytest
import solution


def test_student_study_none():
    res = solution.students_study(0, False)
    assert res is None


def test_student_night_coffee_true():
    assert solution.students_study(20, True)



def test_student_night_coffee_false():
    res = solution.students_study(20, False)
    assert res is True
