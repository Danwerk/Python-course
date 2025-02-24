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
    big_baskets_needed = ordered_amount // 5
    small_baskets_needed = ordered_amount - (big_baskets_needed * 5)
    if big_baskets >= big_baskets_needed and small_baskets >= small_baskets_needed:
        return ordered_amount - (big_baskets_needed * 5)

    if big_baskets < big_baskets_needed:
        if small_baskets >= ordered_amount - (big_baskets * 5):
            return ordered_amount - (big_baskets * 5)
        else:
            return -1
    else:
        return -1


if __name__ == '__main__':
    print(fruit_order(6, 1, 11))
    print(fruit_order(1, 2, 6))  # 1
    print(fruit_order(2, 1, 6))  # 1
    print(fruit_order(4, 0, 4))  # 4
    print(fruit_order(4, 0, 5))  # -1
    print(fruit_order(100, 2, 101))  # 37
