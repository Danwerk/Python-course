import pytest
import solution


def test_student_study_none():
    res = solution.students_study(0, False)
    assert res is None
