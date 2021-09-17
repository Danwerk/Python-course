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


'''
print(find_id_code(""))
print(find_id_code("123456789123456789"))
print(find_id_code("ID code is: 49403136526"))
print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))
'''





'''
b = int(input('enter number: '))
c = f"{b:03}"

print(c)
a = f"{9:03}"

'''



'''
print(a)
for i in range(1,11):
    print(f"{i:03}")

if a < f"{10:03}":
    print('Kuressaare')
'''



'''elif a > f"{10:03}" & a < f"{20:03}":
    print('Tartu')
elif a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')
if a < f"{10:03}":
    print('Kuressaare')


[] = Kuressaare
011...020 = Tartu
021...220 = Tallinn
221...270 = Kohtla-Järve
271...370 = Tartu
371...420 = Narva
421...470 = Pärnu
471...710 = Tallinn
711...999 = undefined
'''

'''
def is_valid_gender_number(j):
    for j in range(0, 9)
        if j == 0:
            return False
    if j > 0 & j <= 6:
        return True
    if j == 7 & j == 8:
        return False

print(is_valid_gender_number(7))
'''

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
    if year % 4 == 0 and not year % 100 == 0:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    eighties = 18
    nineties = 19
    twenties = 20

    if gender_number == 1 or gender_number == 2:
        return str(eighties) + str(year_number)
    if gender_number == 3 or gender_number == 4:
        return str(nineties) + str(year_number)
    if gender_number == 5 or gender_number == 6:
        if year_number < 10:
            return str(twenties) + ('0' + str(year_number))
        else:
            return str(twenties) + str(year_number)

def get_birth_place(birth_number: int) -> str:
    d = {
        "Kuressaare": [range(0,11)],
        "Tartu": [range(11,21), range(271,371)],
        "Tallinn": [range(21,221), range(471,711)],
        "Kohtla-Järve": [range(221,271)],
        "Narva": [range(371,421)],
        "Pärnu": [range(421,471)],
        "Undefined": [range(711,1000)],
    }
    if is_valid_birth_number(birth_number) == True:
        for city in d:
            range_list = d[city]
            for city_range in range_list:
                for city_num in city_range:
                    if city_num == birth_number:
                        return city
    else:
        return 'Wrong input!'


print(get_birth_place(1003))

