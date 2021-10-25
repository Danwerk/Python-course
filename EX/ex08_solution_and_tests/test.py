"""Test ex08 functions."""


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
    """Test given all fives."""
    input_value = 10
    res = solution.lottery(5, 5, 5)
    assert res == input_value


def test_lottery_all_same_positive():
    """Test given all same positive numbers, not fives."""
    input_value = 5
    res = solution.lottery(3, 3, 3)
    assert res == input_value


def test_lottery_all_same_negative():
    """Test given all negative numbers."""
    input_value = 5
    res = solution.lottery(-3, -3, -3)
    assert input_value == res


def test_lottery_all_same_zero():
    """Test given numbers are same zeros."""
    input_value = 5
    res = solution.lottery(0, 0, 0)
    assert input_value == res


def test_lottery_a_b_same_c_diff():
    """Test a and b are same c is different."""
    input_value = 0
    res = solution.lottery(2, 2, 3)
    assert input_value == res


def test_lottery_a_c_same_b_diff():
    """Test a and c are same b is different."""
    input_value = 0
    res = solution.lottery(2, 3, 2)
    assert input_value == res


def test_lottery_b_c_same_a_diff():
    """Test b and c are same a is different."""
    input_value = 1
    res = solution.lottery(2, 3, 3)
    assert input_value == res


def test_lottery_all_diff():
    """Test all given numbers are different."""
    input_value = 1
    res = solution.lottery(1, 2, 3)
    assert input_value == res


def test_fruit_all_zero():
    """Test all given numbers are zeros."""
    input_value = 0
    res = solution.fruit_order(0, 0, 0)
    assert input_value == res


def test_fruit_zero_amount_zero_small():
    """Test given order_amount is zero and small_basket is zero."""
    input_value = 0
    res = solution.fruit_order(0, 2, 0)
    assert input_value == res


def test_fruit_zero_amount_zero_big():
    """Test given order_amount is zero and big_basket is zero."""
    input_value = 0
    res = solution.fruit_order(2, 0, 0)
    assert input_value == res


def test_fruit_zero_amount_others_not_zero():
    """Test given order_amount others are not zero."""
    input_value = 0
    res = solution.fruit_order(2, 3, 0)
    assert input_value == res


def test_fruit_only_big_exact_match():
    """Test given big_basket exact match."""
    input_value = 0
    res = solution.fruit_order(0, 2, 10)
    assert input_value == res


def test_fruit_only_big_not_enough():
    """Test given big_basket not enough."""
    input_value = -1
    res = solution.fruit_order(0, 2, 11)
    assert input_value == res


def test_fruit_only_big_more_than_required_match():
    """Test given big_basket more than required match."""
    input_value = 0
    res = solution.fruit_order(0, 4, 10)
    assert input_value == res


def test_fruit_only_small_exact_match():
    """Test given small_basket exact match."""
    input_value = 5
    res = solution.fruit_order(5, 0, 5)
    assert input_value == res


def test_fruit_only_small_not_enough():
    """Test given small_basket not enough."""
    input_value = -1
    res = solution.fruit_order(4, 0, 5)
    assert input_value == res


def test_fruit_only_small_more_than_required():
    """Test given small_basket not enough."""
    input_value = 5
    res = solution.fruit_order(14, 0, 5)
    assert input_value == res


