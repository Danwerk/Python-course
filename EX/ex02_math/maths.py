"""maths."""
def ects(ects, weeks):
    """Implement a function to know how many hours are needed per week if each ECTS is 26 hours."""
    if weeks <= 0:
        return 'Impossible!'
    else:
        hours_per_week = (ects * 26) / weeks
        return hours_per_week
    pass


def average(a, b, c, d):
    """

    Implement a function that has 4 numeric parameters.

    Each parameter must be multiplied by number of its position
    in the function (x, y, z = 1, 2, 3). Calculate and return the average.
    Examples:
    1. average(0, 0, 0, 4) === 4
    2. average(1, 2, 3, 4) == 7.5
    3. average(5, 0, 5, 1) == 6
    """
    average = ((a * 1) + (b * 2) + (c * 3) + (d * 4)) / 4
    return average
    pass


def clock(d, h, m, s):
    """
    Implement a function that has 4 numeric parameters.

    The values are: days, hours, minutes, seconds. Calculate how many
    minutes are in total and return the value.
    Examples:
    1. clock(1, 24, 60, 60) === 2941
    3. clock(0, 0, 0, 60) == 1
    3. clock(0, 0, 1, 60) == 2
    """
    minutes = (d * 24 * 60) + (h * 60) + (m) + (s / 60)
    return minutes
    pass
