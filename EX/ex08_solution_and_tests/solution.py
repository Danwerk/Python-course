"""Some EX08 exercises."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 18 <= time <= 24 and coffee_needed is True or 18 <= time <= 24 and coffee_needed is False or 5 <= time <= 17 and coffee_needed is True:
        return True
    elif 5 <= time <= 17 and coffee_needed is False or 1 <= time <= 4 and coffee_needed is False or 1 <= time <= 4 and coffee_needed is True:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c != 5:
        return 5
    elif b != a and c != a:
        return 1
    elif b == a or c == a:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if (small_baskets * 1) + (big_baskets * 5) == ordered_amount:
        return small_baskets
    else:
        return -1


if __name__ == '__main__':
    # print(students_study(6, False))
    # print(lottery(1, 3, 3))
    print(fruit_order(3, 1, 10))
