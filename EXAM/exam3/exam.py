"""Exam 3 (2022-01-12)."""
import math


def count_camel_case_words(text: str) -> int:
    """
    Count the words in the text.

    The text uses camel case. There are no spaces between words.
    Each new word starts with a capital letter.
    The first word can start with a small or a capital letter.

    count_camel_case_words("hello") => 1
    count_camel_case_words("") => 0
    count_camel_case_words("helloWorld") => 2
    count_camel_case_words("HelloWorld") => 2
    count_camel_case_words("aBC") => 3
    count_camel_case_words("ABC") => 3
    count_camel_case_words("a") => 1
    count_camel_case_words("What") => 1
    """
    count = 0
    if text == '':
        return 0
    if text[0] == text[0].lower():
        count += 1
    elif text[0] == text[0].upper():
        count += 1
    for i in text[1:]:
        if i.isupper():
            count += 1
    return count


# print(count_camel_case_words("hello"))  # 1
# print(count_camel_case_words(""))  # 0
# print(count_camel_case_words("helloWorld"))  # 2
# print(count_camel_case_words("HelloWorld"))  # 2
# print(count_camel_case_words("aBC"))  # 3
# print(count_camel_case_words("ABC"))  # 3
# print(count_camel_case_words("a"))  # 1
# print(count_camel_case_words("What"))  # 1


def odd_index_sum(nums: list) -> int:
    """
    Find sum of elements with odd indices.

    odd_index_sum([1, 2, 3]) => 2
    odd_index_sum([]) => 0
    odd_index_sum([1]) => 0
    odd_index_sum([2, 3]) => 3
    odd_index_sum([0, -1, -4, -3]) => -4
    """
    summ = 0
    if nums == []:
        return 0
    for i in range(1, len(nums), 2):
        summ += nums[i]
    return summ


# print(odd_index_sum([1, 2, 3]))  # 2
# print(odd_index_sum([]))  # 0
# print(odd_index_sum([1]))  # 0
# print(odd_index_sum([2, 3]))  # 3
# print(odd_index_sum([0, -1, -4, -3]))  # -4


def encode_string_with_hex_key(input_str: str, key: str) -> str:
    """
    Encode string using key.

    :param input_str - string to encode. Non-alphabetic characters are left as is.
    Caps are encoded into caps.
    :param key - hex key in which n-th number tells how much should n-th char in input_str be shifted.
    Works as round buffer, eg. if z is reached start from a again.
    The input_str and key are always the same length.

    encode_string("a", "1") -> "b"
    encode_string("z", "1") -> "a"
    encode_string("abc", "101") -> "bbd"
    encode_string("z.z.z", "fffff") -> "o.o.o"

    :return Encoded string
    """
    ascii_list = []
    crypted = []
    for character in input_str:
        ascii_list.append(ord(character))

    for i in range(len(ascii_list)):
        n = ascii_list[i]
        if ascii_list[i] >= 97 and ascii_list[i] <= 122:
            n = ascii_list[i] + int(key[i], base=16)
            if n > 122:
                crypted.append((n - 97) % 26 + 97)
            else:
                crypted.append(n)
        else:
            n = n
            crypted.append(n)

    mystring = ""
    for char in crypted:
        mystring = mystring + chr(char)
    return mystring


# print(encode_string_with_hex_key("a", "1"))  # "b"
# print(encode_string_with_hex_key("z", "1"))  # "a"
# print(encode_string_with_hex_key("abc", "101"))  # "bbd"
# print(encode_string_with_hex_key("z.z.z", "fffff"))  # "o.o.o"


def who_gets_gingerbread(students: dict, total_gingerbreads: int) -> dict:
    """
    How many gingerbread students get.

    Given a dictionary of students with their average score and amount of gingerbreads that shows
    how many gingerbreads elves are about to share between students. However, elves have some conditions how to
    they are sharing gingerbreads - students with average score with or below 2.0 don't get any and should not appear in
    result dictionary and student with the highest average starts getting gingerbreads first.

    Return the dictionary of students with amount of gingerbreads they got from elves.

    Examples:
    students = {
        'Mart': 4.0,
        'Kristi': 4.5,
        'Kevin': 3.2,
        'Markus': 2.0
    }
    total_gingerbreads = 11

    The order of the students: Kristi, Mart, Kevin. Markus is left out due to the average grade 2.0.

    result =>
    {
        'Kristi': 4
        'Mart': 4
        'Kevin': 3
    }

    :param students: dict of students with their aberage score
    :param total_gingerbreads: number of gingerbreads that elves have
    :return: dict of students with amount of gingerbreads they got
    """
    ret = {}
    avg_grade = 0
    names_to_remove = []
    avg_grade = sum(students.values()) / len(students)
    for i in students:
        if students[i] < avg_grade:
            pass
    avg_grade = avg_grade / len(students)

    sorted_students = sorted(students, key=lambda x: -students[x])

    for s in range(total_gingerbreads):
        gingerbreads = 1
        ret[s] = gingerbreads

    return ret


# print(who_gets_gingerbread({'Mart': 4.0, 'Kristi': 4.5, 'Kevin': 3.2, 'Markus': 2.0}, 11))


def fuel_calculator(fuel: int) -> int:
    """
    Find needed amount of fuel for a given mass.

    Amount of fuel needed = mass divided by three, rounded down, subtract two
    + fuel needed for the fuel itself
    + fuel needed for the fuel's fuel + etc.

    Negative fuel rounds to zero.

    Examples:
    fuel_calculator(10) -> 1 + 0 = 1
    fuel_calculator(151) -> 48 + 14 + 2 + 0 = 64
    """
    s = math.floor(fuel / 3) - 2
    if s < 0:
        return 0
    else:
        return s + fuel_calculator(s)


def make_table(n: int) -> str:
    r"""
    Given an odd integer n, return a n*n table like shown in the examples.

    The given n is more or equal to 7.

    Example 1:
    n=15
    result:

    \#####/|\#####/
    #\###/#|#\###/#
    ##\#/##|##\#/##
    ###X###|###X###
    ##/#\##|##/#\##
    #/###\#|#/###\#
    /#####\|/#####\
    -------+-------
    \#####/|\#####/
    #\###/#|#\###/#
    ##\#/##|##\#/##
    ###X###|###X###
    ##/#\##|##/#\##
    #/###\#|#/###\#
    /#####\|/#####\

    Example 2:
    n=7
    result:

    \#/|\#/
    #X#|#X#
    /#\|/#\
    ---+---
    \#/|\#/
    #X#|#X#
    /#\|/#\

    Example 3:
    n=9
    result:

    \##/|\##/
    #\/#|#\/#
    #/\#|#/\#
    /##\|/##\
    ----+----
    \##/|\##/
    #\/#|#\/#
    #/\#|#/\#
    /##\|/##\

    """
    pass


class Student:
    """Represent student model."""

    def __init__(self, name: str, gpa: float, age: int):
        """
        Class constructor.

        Each student has name and gpa (Grade Point Average).

        :param name: student's name
        :param gpa: student's gpa
        :param age: student's age
        """
        self.age = age
        self.gpa = gpa
        self.name = name

    def __repr__(self):
        return self.name


class University:
    """Represent university model."""

    def __init__(self, name: str, gpa_required: float):
        """
        Class constructor.

        Each university has name and gpa_required.

        University should also have a database to keep and track all students.
        :param name: university name
        :param gpa_required: university required gpa
        """
        self.name = name
        self.gpa_required = gpa_required
        self.students = []

    def __repr__(self):
        return self.students

    def can_enroll_student(self, student: Student) -> bool:
        """
        Check if student can be enrolled to university.

        Student can be successfully enrolled if:
            * he/she has required gpa (>=)
            * he/she is not already enrolled to this university
            * he/she is at least 16 years old
            * additionally, if student's name characters length is
            exactly 13 -> student can be added to university despite gpa (though still should not be
            already present in university and be younger)
        If the student cannot be enrolled, returns False. Otherwise returns True.

        :return: bool
        """

        if student.gpa >= self.gpa_required and student not in self.students and student.age >= 16:
            return True
        if len(student.name) == 13:
            return True
        else:
            return False

    # tudengi enda gpa ei ole ülikooli gpa_required väärtusest väiksem
    # tudengit ei ole juba ülikoolis olemas.
    # tudeng on vähemalt 16 aastat vana
    # kui aga tudengi nime pikkus (tähtede arv) on täpselt 13, siis tudeng saab ülikooli astuda vaatamata tema gpa väärtusele (ehk saab ka madalama keskmise hindega sisse).
    # Funktsioon tagastab True, kui tudengit saab ülikooli lisada, ja False vastasel juhul.

    def enroll_student(self, student: Student):
        """
        Enroll new student to university if possible.

        Before enrolling, you have to check whether student can be enrolled.

        :param student: Student
        Function does not return anything
        """
        if self.can_enroll_student(student) is True:
            self.students.append(student)

    def can_unenroll_student(self, student: Student) -> bool:
        """
        Check if student can leave from university.

        Student can be successfully leave if he/she actually studies in this university.

        Returns True, if the student can be unenrolled, False otherwise.

        :return: bool
        """
        if student in self.students:
            return True
        else:
            return False

    def unenroll_student(self, student: Student):
        """
        Unenroll student from University if possible.

        Before unenrolling, you have to make sure the student can be unenrolled.
        Function does not return anything
        """
        if self.can_unenroll_student(student) is True:
            self.students.remove(student)

    def get_students(self) -> list:
        """
        Return a list of all students in current university.

        :return: list of Student objects
        """
        return self.students

    def get_student_highest_gpa(self) -> list:
        """
        Return a list of students (student) with the highest gpa.

        :return: list of Student objects
        """
        ret = []
        if self.students is not []:
            student_max = max(student.gpa for student in self.students)
        else:
            return []
        for s in self.students:
            if s.gpa == student_max:
                ret.append(s)
        return ret


class Accessory:
    """Accessory."""

    def __init__(self, name: str, value: int):
        """Constructor."""
        self.name = name
        self.value = value

    def __repr__(self):
        """
        String representation of accessory.

        Returns string in form "{name}, value : {value}."
        """
        return f"{self.name}, value : {self.value}."


class Car:
    """Car."""

    def __init__(self, name: str, color: str):
        """Constructor."""
        self.name = name
        self.color = color
        self.fuel = 100
        self.accessories = []

    def add_accessory(self, accessory: Accessory):
        """Add accessory to the car."""
        self.accessories.append(accessory)
        print("a")

    def get_value(self) -> int:
        """
        Get the value of the car.

        Regular car base price is 9500, for premium car its 42 500.
        All the values of accessories are summed up.
        """
        price = 0
        if self.accessories is []:
            return price

    def get_fuel_left(self):
        """Return how much fuel is left in percentage."""
        return self.fuel

    def get_accessories_by_value(self):
        """Return accessories sorted by value (descending i.e. higher to lower)."""
        return sorted(self.accessories, key=lambda x: x.value)

    def __repr__(self):
        """
        String representation of the car.

        Should return "This {color} {name} contains {accessory_amount} accessories and has {fuel}% fuel left."
        """
        return f'This {self.color} {self.name} contains ... accessories and gas {self.fuel}% fuel left.'


class Customer:
    """Customer."""

    def __init__(self, name: str, wish: str):
        """
        Constructor.

        The wish consists of two words.
        The first word is either "Cheap" or "Expensive".
        In case of "Cheap", the customer wants to get the car with the lowest value.
        In case of "Expensive", the customer wants to get the car with the highest value.
        The second word is the color. Customer does not want a car with another color.
        For premium customer a car with the given color is searched for from the premium cars.
        If there is no such car with the wished color, the cheapest car is taken from the premium cars.

        For example: "Cheap Red", "Expensive Yellow".
        """
        self.name = name
        self.wish = wish
        self.cars = []
        self.type = None

    def get_garage(self):
        """
        Return all the cars of the customer sorted by the value (ascending i.e. from lower to higher).

        Both regular and premium cars are kept in garage.
        """
        return sorted(self.cars, key= lambda x: x.price)

    def make_premium(self):
        """Make customer a premium customer, premium cars can be sold to the customer now."""

    def drive_with_car(self, driving_style: str):
        """
        Go for a drive.

        A car with the highest fuel percentage should be taken.
        If several cars have the same percentage, use the most expensive one.

        If the driving_style is "Rally", the customer takes the cheapest car instead.
        Regular driving takes 15 percentage points of fuel, "Rally" takes 35 percentage points (85% - 35% => 50%).
        If the fuel gets to zero during the drive, the car is left behind (it is no longer part of garage).
        """


class Dealership:
    """Dealership."""

    def __init__(self, name: str):
        """Constructor."""
        self.name = name
        self.cars = []
        self.premium = []
        self.regular = []

    def add_car(self, car: Car):
        """Car is added to dealership."""
        self.cars.append(car)

    def get_all_regular_cars(self):
        """Return all the regular cars sorted by value (ascending, lower to higher)."""
        self.regular = [i for i in self.cars]
        return sorted(self.regular, key=lambda x: x.get_value())

    def make_car_premium(self, car: Car):
        """Make a car premium, which can can be sold only to premium customers."""
        self.premium.append(car)
        self.regular.remove(car)

    def get_all_premium_cars(self):
        """Return all the premium cars sorted by value (ascending, lower to higher)."""
        return sorted(self.premium, key=lambda x: x.price)

    def sell_car_to_customer(self, customer: Customer):
        """
        Sell a car to customer depending on his/her wishes.

        After selling, the car is removed from the dealership and moved into customer's garage.
        In the given exercise, there is always a matching car.
        """


if __name__ == '__main__':
    # assert count_camel_case_words("") == 0
    # assert count_camel_case_words("helloWorld") == 2
    # assert count_camel_case_words("ABC") == 3
    #
    # assert odd_index_sum([]) == 0
    # assert odd_index_sum([1]) == 0
    # assert odd_index_sum([1, 2]) == 2
    # assert odd_index_sum([1, 2, 4, 3]) == 5
    #
    # assert encode_string_with_hex_key("hello", "01234") == "hfnos"
    # assert encode_string_with_hex_key("a", "f") == "p"
    #
    # assert who_gets_gingerbread(
    #     {
    #         'Mart': 4.0,
    #         'Kristi': 4.5,
    #         'Kevin': 3.2,
    #     },
    #     11
    # ) == {
    #            "Kristi": 4,
    #            "Mart": 4,
    #            "Kevin": 3
    #        }
    #
    # assert fuel_calculator(151) == 64
    #
    # print(make_table(9))
    r"""
\##/|\##/
#\/#|#\/#
#/\#|#/\#
/##\|/##\
----+----
\##/|\##/
#\/#|#\/#
#/\#|#/\#
/##\|/##\
    """
    # table = make_table(9).split("\n")
    # assert table[0] == r"\##/|\##/"
    # assert table[4] == r"----+----"
    # assert table[6] == r"#\/#|#\/#"
    # assert table[8] == "/##\\|/##\\"
    # assert table[-1] != "\n"  # no new-line in the end
    #
    # table = make_table(7)
    # assert table[8:15] == "#X#|#X#"

    # university

    # university = University("taltech", 60)
    # student = Student("Bob", 61, 18)
    # print(university.can_enroll_student(student))  # True
    # print(university.can_unenroll_student(student))  # False; student is not yet in university
    #
    # university.enroll_student(student)
    # print(university.get_students())  # [student]
    # print(university.get_student_highest_gpa())  # [student]; since this student is the only one
    #
    # print(university.can_unenroll_student(student))  # True
    # university.unenroll_student(student)
    # print(university.get_students())  # []

    # dealership

    blue_car = Car("Audi R4", "blue")
    green_car = Car("Ford", "green")
    wheel = Accessory("Sport wheel", 100)
    blue_car.add_accessory(wheel)
    car_dealer = Dealership("Ago Carfriend")
    car_dealer.add_car(blue_car)
    car_dealer.add_car(green_car)

    print(car_dealer.get_all_regular_cars())
    # [This green Ford contains 0 accessories and has 100% fuel left.,
    # This blue Audi R4 contains 1 accessories and has 100% fuel left.]
    print(car_dealer.get_all_premium_cars())  # []

    customer = Customer("Ago", "Cheap green")
    car_dealer.sell_car_to_customer(customer)
    print(customer.get_garage())  # [This green Ford contains 0 accessories and has 100% fuel left.]
    customer.drive_with_car("Rally")
    print(customer.get_garage())  # [This green Ford contains 0 accessories and has 65% fuel left.]
    customer.drive_with_car("Rally")
    customer.drive_with_car("Rally")
    print(customer.get_garage())  # []]

    car_dealer.make_car_premium(blue_car)
    print(car_dealer.get_all_premium_cars())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]

    customer_premium = Customer("Ago", "Expensive black")
    customer_premium.make_premium()
    car_dealer.sell_car_to_customer(customer_premium)
    print(customer_premium.get_garage())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]
