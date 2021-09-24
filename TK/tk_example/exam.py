"""Example TK."""


def workday_count(days):
    if days == 6:
        return 5
    else:
        weeks = days // 7
        weekend_days = weeks * 2
        workdays = (days - weekend_days)
        return workdays



print(workday_count(4635))
print(workday_count(6))


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


def extra_end(s: str) -> str:
    if len(s) >= 2:
        return str(s[-2:] * 3)


print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))


def divisions(numbers: list) -> int:
    count = 0
    for i in numbers:
        for j in numbers:
            if i != j and i % j == 0:
                count += 1
    return count


print(divisions([3, 14, 12, 6]))


