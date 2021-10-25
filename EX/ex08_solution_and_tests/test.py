import pytest
import solution


def test_student_study_none():
    assert solution.students_study(22, False) is not None


def test_student_night_coffee_true():
    assert solution.students_study(20, True)


def test_student_night_coffee_false():
    assert solution.students_study(20, False)

'''
def test_student_evening_coffee_true():
    assert solution.students_study(20, False)


def test_student_evening_coffee_false():
    assert solution.students_study(20, False)

'''
def test_student_day_coffee_true():
    assert solution.students_study(6, True)


def test_student_day_coffee_false():
    assert solution.students_study(6, True)

