"""Example TK."""


def workday_count(days):
    weeks = days // 7
    weekend_days = weeks * 2
    workdays = days - weekend_days
    return workdays


def sorta_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21

    """
    sum_of_nums = a + b
    if 10 <= sum_of_nums <= 19:
        return 20
    else:
        return sum_of_nums


print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))






