def ects(ects, weeks):
    """Implement a function to know how many hours are needed per week."""
    if weeks <= 0:
        print('impossible')
    else:
        hours_per_week = (ects * 26) / weeks
        print(hours_per_week)
