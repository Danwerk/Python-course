import pytest
import solution


def test_student_study_none():
    assert solution.students_study(22, False) is not None


def test_student_evening_coffee_true():
    assert solution.students_study(20, True)


def test_student_evening_coffee_false():
    assert solution.students_study(20, False)


def test_student_night_coffee_true():
    assert solution.students_study(3, False) is not True


def test_student_night_coffee_false():
    assert solution.students_study(3, True) is not True


def test_student_day_coffee_true():
    assert solution.students_study(6, True)


def test_student_day_coffee_false():
    assert solution.students_study(6, False) is not True



def test_student_evening_edge_case_coffee_true():
    assert solution.students_study(24, True)
    assert solution.students_study(18, True)



def test_student_evening_edge_case_coffee_false():
    assert solution.students_study(24, False)


def test_student_night_edge_case_coffee_true():
    assert solution.students_study(4, False) is not True


def test_student_night_edge_case_coffee_false():
    assert solution.students_study(4, True) is not True


def test_student_day_edge_case_coffee_true():
    assert solution.students_study(17, True)


def test_student_day_edge_case_coffee_false():
    assert solution.students_study(17, False) is not True

