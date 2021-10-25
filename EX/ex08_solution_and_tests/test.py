import pytest
import solution


def test_student_study_none():
    assert solution.students_study(25, False) is None



def test_student_night_coffee_true():
    assert solution.students_study(20, True)


def test_student_night_coffee_false():
    assert solution.students_study(20, False)

