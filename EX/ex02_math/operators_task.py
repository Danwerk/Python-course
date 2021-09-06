"""Operators."""


def add(x, y):
    """Add x to y."""
    return x + y
    pass


def sub(x, y):
    """Subtract y from x."""
    return x - y
    pass


def multiply(x, y):
    """Multiply x by y."""
    return x * y
    pass


def div(x, y):
    """Divide x by y."""
    return x / y
    pass


def modulus(x, y):
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y
    pass


def floor_div(x, y):
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return x // y
    pass


def exponent(x, y):
    """Calculate x where y is an exponent."""
    return x ** y
    pass


def first_greater_or_equal(x, y):
    """If x is greater or equal than y then return True. If not then return False."""
    if x >= y:
        return True
    else:
        return False
    pass


def second_less_or_equal(x, y):
    """If y is less or equal than x then return True. If not then return False."""
    if y <= x:
        return True
    else:
        return False
    pass


def x_is_y(x, y):
    """If x same as y then return True. If not then return False."""
    if x == y:
        return True
    else:
        return False
    pass


def x_is_not_y(x, y):
    """If x is not same as y then return True. If not then return False."""
    if x != y:
        return True
    else:
        return False
    pass


def if_else(a, b, c, d):
    """Create a program that has 4 numeric parameters."""
    result1 = a * b
    result2 = c / d
    if result1 > result2:
        return result1
    elif result1 < result2:
        return result2
    else:
        return 0
    pass


def surface(length, width):
    """Add the missing parameters to calculate the surface. Calculate and return the value of surface."""
    return length * width
    pass


def volume(length, width, height):
    """Add the missing parameters to calculate the volume. Calculate and return the value of volume."""
    return length * width * height
    pass


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2))  # 2
    print(volume(5, 5, 5))  # 125
