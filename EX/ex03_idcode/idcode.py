"""Idcode."""


def find_id_code(text: str) -> str:
    """Find ID-code from given text."""
    nums_from_text = []
    for i in text:
        if i.isdigit():
            nums_from_text.append(i)
    str_number = "".join(nums_from_text)  # converts list numbers to a string

    if len(str_number) < 11:
        return 'Not enough numbers!'
    elif len(str_number) > 11:
        return 'Too many numbers!'
    else:
        return str_number

def is_valid_gender_number(i):
    if i == 0 or i >= 7:
        return False
    elif i > 0 and i < 7:
        return True


def get_gender(gender: str):
    first_num_male = [1, 3, 5]
    first_num_female = [2, 4, 6]
    if gender in first_num_male:
        return 'male'
    if gender in first_num_female:
        return 'female'

def is_valid_year_number(year_number: int) -> bool:
    if year_number >= 0 and year_number < 100:
        return True
    else:
         return False


def is_valid_month_number(month_number: int) -> bool:
    if month_number > 0 and month_number < 13:
        return True
    else:
        return False



def is_valid_birth_number(birth_number: int) ->bool:
    if birth_number > 0 and birth_number < 1000:
        return True
    else:
        return False

def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and not year % 100 == 0:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    eighties = 18
    nineties = 19
    twenties = 20
    if len(str(year_number)) > 2:
        return 'woops'
    else:

        if gender_number == 1 or gender_number == 2:
            return eighties * 100 + year_number

        if gender_number == 3 or gender_number == 4:
            return nineties * 100 + year_number

        if gender_number == 5 or gender_number == 6:
            return twenties * 100 + year_number


def get_birth_place(birth_number: int) -> str:
    dict = {
        "Kuressaare": [range(0,11)],
        "Tartu": [range(11,21), range(271,371)],
        "Tallinn": [range(21,221), range(471,711)],
        "Kohtla-Järve": [range(221,271)],
        "Narva": [range(371,421)],
        "Pärnu": [range(421,471)],
        "undefined": [range(711,1000)],
    }
    if is_valid_birth_number(birth_number) == True:
        for city in dict:
            range_list = dict[city]
            for city_range in range_list:
                for city_num in city_range:
                    if city_num == birth_number:
                        return city
    else:
        return 'Wrong input!'


print(get_birth_place(711))



def is_valid_control_number(id_code: str):
    first_step = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    second_step = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    id_code_list = list(map(int, id_code))
    id_code_list.pop()

    summary = sum(x * y for x, y in zip(first_step, id_code_list))
    summary = summary % 11

    if summary < 10:
        if str(summary) == id_code[-1]:
            return True
        else:
            return False

    if summary >= 10:
        summary2 = sum(x * y for x, y in zip(second_step, id_code_list))
        summary2 = summary2 % 11
        if summary2 < 10:
            if str(summary2) == id_code[-1]:
                return True
            else:
                return False
        if summary2 >= 10:
            return summary == 0

