"""Idcode."""


def find_id_code(text: str) -> str:
    """Find ID-code from given text."""
    nums_from_text = []
    for i in text:
        if i.isdigit():
            nums_from_text.append(i)
    str_number = "".join(nums_from_text)  # converts list of numbers to a string

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


def get_gender(gender: int):
    if gender % 2 == 0:
        return 'female'
    else:
        return 'male'


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""

    if year_number >= 0 and year_number < 100:
        return True
    else:
         return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
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

    if gender_number == 1 or gender_number == 2:
        return eighties * 100 + year_number

    if gender_number == 3 or gender_number == 4:
        return nineties * 100 + year_number

    if gender_number == 5 or gender_number == 6:
        return twenties * 100 + year_number


def get_birth_place(birth_number: int) -> str:
    dict = {
        "Kuressaare": [range(0, 11)],
        "Tartu": [range(11, 21), range(271, 371)],
        "Tallinn": [range(21, 221), range(471, 711)],
        "Kohtla-Järve": [range(221, 271)],
        "Narva": [range(371, 421)],
        "Pärnu": [range(421, 471)],
        "undefined": [range(711, 1000)],
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


def is_valid_control_number(id_code: str):
    first_step = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    second_step = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    id_code_list = list(map(int, id_code))
    id_code_list.pop()  # removes last digit from id_code_list

    sum_of_idcode = sum(x * y for x, y in zip(first_step, id_code_list))
    sum_of_idcode = sum_of_idcode % 11

    if sum_of_idcode < 10:
        if str(sum_of_idcode) == id_code[-1]:
            return True
        else:
            return False


    if sum_of_idcode >= 10:
        sum_of_idcode_2 = sum(x * y for x, y in zip(second_step, id_code_list))
        sum_of_idcode_2 = sum_of_idcode_2 % 11
        if sum_of_idcode_2 == 10:
            sum_of_idcode_2 = 0
        if sum_of_idcode_2 < 10:
            if str(sum_of_idcode_2) == id_code[-1]:
                return True
            else:
                return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    month_of_thirty_days = [4, 6, 9, 11]
    month_of_thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
    depends_on_leap = [2]
    if month_number in month_of_thirty_days:
        if day_number > 1 and day_number <= 30:
            return True
        else:
            return False
    elif month_number in month_of_thirty_one_days:
            if day_number >= 1 and day_number <= 31:
                return True
            else:
                return False
    elif month_number in depends_on_leap:
        if is_leap_year(get_full_year(gender_number, year_number)) == True:
            if day_number > 1 and day_number <= 29:
                return True
            elif day_number > 1 and day_number <= 28:
                return False
            else:
                return False
        elif not is_leap_year(get_full_year(gender_number, year_number)):
            if day_number > 1 and day_number <= 29:
                return False
            elif day_number > 1 and day_number <= 28:
                return True
            else:
                return False


def is_id_valid(id_code: str) -> bool:
    if len(find_id_code(id_code)) < 11 or len(find_id_code(id_code)) > 11:
        return False
    else:
        if is_valid_gender_number(int(id_code[0])) == False:
            return False
        else:
            if is_valid_year_number(int(id_code[1:3])) == False:
                return False
            else:
                if is_valid_month_number(int(id_code[3:5])) == False:
                    return False
                else:
                    if is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])) == False:
                        return False
                    else:
                        if is_valid_birth_number(int(id_code[7:10])) == False:
                            return False
                        else:
                            if is_valid_control_number(id_code[0:11]) == False:
                                return False
                            else:
                                return True


def get_data_from_id(id_code: str) -> str:
    id_code = find_id_code(id_code)
    if is_id_valid(id_code) == True:
        return f"This is a {get_gender(int(id_code[0]))} born on {int(id_code[5:7])}.{(id_code[3:5])}.{get_full_year(int(id_code[0]), int(id_code[1:3]))} in {get_birth_place(int(id_code[7:10]))}."
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print(is_valid_control_number("60102031670"))  # -> False, it must be 6
    print(is_id_valid('60102nm31670'))
    '''
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))  # -> "49403136526"

    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    '''
    print("\nFull message:")
    print(get_data_from_id("aspoiejrtd498082asdf7024gd4"))
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True

