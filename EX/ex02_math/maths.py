def ects(ects, weeks):
    if weeks <= 0:
        print('impossible')
    else:
        hours_per_week = (ects * 26) / weeks
        print(hours_per_week)
    pass
