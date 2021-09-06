def ects(ects, weeks):
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours. If it's not possible in
    time then return a string "Impossible!".

    Examples:
    1. ects(30, 12) == 65
    2. ects(1, 1) == 26
    3. ects(1, 0) == "Impossible!"
    """

    if weeks <= 0:
        print('impossible')
    else:
        hours_per_week = (ects * 26) / weeks
        print(hours_per_week)


