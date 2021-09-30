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


def lucky_guess(n: int) -> bool:
    lucky_nums = [1, 3, 7]
    str_num = str(n)
    if n in lucky_nums:
        return True
    elif n >= -6 and n <= 121 and n % 13 == 0:
        return True
    elif n < 0 and '5' not in str(n) and '6' not in str(n):
        return True
    else:
        False


#print(lucky_guess(7))
#print(lucky_guess(26))
#print(lucky_guess(-35))


def sum_of_a_beach(s: str) -> int:
    low_case = s.lower()
    count = 0
    beach_list = ['sand', 'water', 'fish', 'sun']
    for beach_elem in beach_list:
        beach_elem_len = len(beach_elem)
        for i in range(len(s)):
            if low_case[i:i + beach_elem_len] == beach_elem:
                count += 1
    return count


print(sum_of_a_beach("WAtErSlIde"))


