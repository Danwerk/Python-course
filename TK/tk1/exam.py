def format_time(minutes: int) -> str:
    hours = minutes // 60
    if minutes < 60:
        return f'{minutes}min'
    else:
        minutes = minutes % 60
        if minutes == 0:
            return f'{hours}h'
        else:
            return f'{hours}h {minutes}min'

print(format_time(29460))