"""Eksam 6 (2022-01-21)."""


def segment_number(first_number, last_number):
    """
    Segment number.

    Return list of numbers where only numbers between first_number
    and last_number (both inclusive) which divide by 5 but do not divide by 3
    are used.

    #1

    :param first_number: the lowest possible candidate
    :param last_number: the highest possible candidate
    :return: list of numbers
    """
    ret = []
    for i in range(first_number, last_number + 1):
        if i % 3 != 0 and i % 5 == 0:
            ret.append(i)
    return ret


# print(segment_number(1, 11))  # [5, 10]
# print(segment_number(1, 4))  # []
# print(segment_number(-20, 20))  # [-20, -10, -5, 5, 10, 20]


def add_or_subtract(numbers):
    """
    Add or subtract.

    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    #2

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    subtract = False
    sum = 0
    for i in numbers:
        if i != 0 and subtract == False:
            sum += i
        elif i != 0 and subtract == True:
            sum -= i
        elif i == 0 and subtract == False:
            subtract = True
        elif i == 0 and subtract == True:
            subtract = False
    return sum


# print(add_or_subtract([1, 2, 0, 3]))  # 0
# print(add_or_subtract([0, 1, 2]))  # -3
# print(add_or_subtract([1, 2, 0, 2, 0, 4]))  # 5


def should_get_up_early(is_weekday, really_tired, first_class_is_programming) -> bool:
    """
    Should get up early.

    Decide if you should get up early enough for first class.

    You should only even consider getting up early if it is a weekday, on weekends you should never get up early.
    If it is a weekday you should typically get up early, unless you are really tired.
    But if it is a weekday and you are really tired but the first class is a programming class you should still get up
    early ignoring you being tired.

    #3

    :param is_weekday: is it a weekday or not, boolean
    :param really_tired: are you really tired, boolean
    :param first_class_is_programming: is the first class a programming class, boolean
    :return: True if you should get up early, otherwise False
    """
    if not is_weekday:
        return False
    elif is_weekday and really_tired and first_class_is_programming:
        return True
    elif is_weekday and really_tired and not first_class_is_programming:
        return False
    elif is_weekday and not really_tired:
        return True


# print(should_get_up_early(True, True, True))  # True
# print(should_get_up_early(False, True, False))  # False


def pear_fear(pears, people):
    """
    Pear fear.

    Every 3rd person fears pears, so they won't get any.
    How many pears will each get?
    Everyone who is not afraid of pears gets equal number of pears.
    Only whole pears will be used, so some pears may remain.

    #4

    :param pears:
    :param people:
    :return:
    """
    """Sisendiks on pirnide arv ja inimeste arv.Mitu pirni iga üks saab kui need võrdselt jagada?On teada, et 
    iga kolmandal inimesel on hirm pirnide ees, neile ära pirne jaga.Ainult terveid pirne jagatakse, nii, 
    et mõned pirnid võivad üle jääda."""
    if pears == 0 or people == 0:
        return 0
    amnt_of_people_dont_get_pears = people // 3
    amnt_of_people_who_get_pears = people - amnt_of_people_dont_get_pears

    return pears // amnt_of_people_who_get_pears


# print(pear_fear(10, 3))  # 5
# print(pear_fear(10, 5))  # 2
# print(pear_fear(0, 3))  # 0
# print(pear_fear(17, 2))  # 8
# print(pear_fear(21, 10))  # 3


def string_between_string(word1, word2):
    """
    Insert reversed word2 to the center of word1.

    word1 length is always even.

    #5

    :param word1: Initial word. String.
    :param word2: Word to reverse and insert. String.
    :return: New word as string.
    """
    reversed_s2 = word2[::-1]
    half_s1 = len(word1) // 2
    return word1[0:half_s1] + reversed_s2 + word1[half_s1:]


# print(string_between_string("ho", "lle"))  # "hello"
# print(string_between_string("", "yas"))  # "say"
# print(string_between_string("smrt", "a"))  # "smart"
# print(string_between_string("w  d", " ro "))  # "w  or  d"
# print(string_between_string(".,", ",."))  # "..,,"


def get_padded_string(string1, string2):
    """
    Pad the longer of two strings with the shorter one on both sides.

    If both strings are the same length, consider string1 as the longer one.
    For example when string1 is "pizza" and string2 is "bbq", this should return "bbqpizzabbq".

    #6

    :param string1: String one
    :param string2:  String two
    :return: Padded string
    """
    """Sisendiks on kaks sõne: string1 ja string2. 
    Lisa nendest kahest pikemale nii ette kui tahalühem. Kui sõned on sama pikkusega, siis arvesta string1-e 
    kui pikemat."""

    if len(string1) == len(string2):
        longest = string1
        shortest = string2
    else:
        longest = max(s for s in [string1, string2])
        shortest = min(s for s in [string1, string2])
    return shortest + longest + shortest


# print(get_padded_string("pizza", "bbq"))  # "bbqpizzabbq"
# print(get_padded_string("dog", "cat"))  # "catdogcat"
# print(get_padded_string("geoff", "giraffe"))  # "geoffgiraffegeoff"


def remove_duplicate(number_list):
    """
    Remove duplicates.

    Go though given list and remove all
    occurrences of two or more of the same
    numbers appearing after one another.
    Remove all but one of the duplicates.

    #7

    :param number_list: input list
    :return: new list
    """
    """Sisendiks on arvude järjend.Tagasta järjend, kus kohe pärast mingit arvu olevad tema kordused on eemaldatud."""
    instances = []
    result = []

    for i in range(0, len(number_list) - 1):
        instance = number_list[0]

    return result


print(remove_duplicate([1, 1, 2, 2, 3, 3]))  # [1, 2, 3]
print(remove_duplicate([1, 2, 3]))  # [1, 2, 3]
print(remove_duplicate([1, 1, 1, 1, 1, 2, 1, 1, 3]))  # [1, 2, 1, 3]


def who_called(calls, name):
    """
    Who called.

    You are given a dictionary of calls and a name.
    Determine who called that name.
    The key of the dictionary is the caller, the value is to whom the caller called.
    If nobody called the person, return -1.

    #8

    :param calls: dictionary of all the calls
    :param name: name of the receiver
    :return: name of the caller
    """
    if calls == {}:
        return -1
    for person in calls:
        if calls[person] == name:
            return person
    return -1


# print(who_called({}, "Nathan"))  # -1
# print(who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Alex"))  # "James"
# print(who_called({"Alex": "James", "Jeff": "Bill", "James": "Alex", "Daniel": "Matt"}, "Olaf"))  # -1


def remove_lowest_digit(number):
    """
    Remove lowest digit.

    Given a non-negative integer, remove the first occurrence
    of the lowest digit and return a new number.

    123 => 23
    223 => 23
    232 => 32
    1 => 0
    :param number: non-negative integer
    :return: non-negative integer
    """
    lowest = min(n for n in str(number))
    if len(str(number)) == 1:
        return 0
    else:
        return int(str(number).replace(lowest, '', 1))


# print(remove_lowest_digit(123))  # 23
# print(remove_lowest_digit(100))  # 10
# print(remove_lowest_digit(7))  # 0
# print(remove_lowest_digit(171))  # 71


def show_highest_grade(grade1, grade2):
    """
    Show highest grade.

    Print "Highest grade: GRADE"
    where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"

    #10

    :param grade1:
    :param grade2:
    :return:
    """
    highest_grade = max(grade1, grade2)
    print(f'Highest grade: {highest_grade}')
    return None


# print(show_highest_grade(10, 14))


def transactions(transaction_string):
    """
    The result of transactions.

    Given a string of transactions between bank accounts
    return the amount of money on accounts A, B anc C.

    The transaction is in the following format:
    X,Y,Z
    where
    X is the account (A, B or C) the money is transferred from
    Y is the account (A, B or C) the money is transferred to
    Z is the amount transferred.

    For example:
    "A,B,100"
    The amount in account A is lowered by 100,
    the amount in account B is raised by 100.

    The transaction can take place if the starting
    account has enough money.
    Initially, every account has 100 units of money.

    Account C is credit account, meaning from
    that account the transactions can be executed even
    if there is no money left, the balance goes below 0.

    "C,A,101"
    as the first transaction yields in
    [201, 100, -1]

    "A,B,100" => [0, 200, 100]
    "A,B,10 B,C,10" => [90, 100, 110]

    "A,B,200 C,A,200" => [300, 100, -100]
    (the first transaction is cancelled)

    If the first account is 0 (zero), then
    the money is just transferred to the second account
    (like payment into the account).

    "0,A,100" => [200, 100, 100]
    "0,A,110 A,B,120" => [90, 220, 100]

    The input is always correct:
     - space separated transactions
     - transaction is in the format X,Y,Z
     - X is either '0', 'A', 'B' or 'C'
     - Y is either 'A', 'B' or 'C'
     - Z is non-negative integer

     #11

    :param transaction_string: string with transactions
    :return: list of ints (length 3)
    """
    pass


def recursive_sum(list_of_numbers):
    """
    Recursive sum.

    Write a function that finds the sum of numbers in the given list recursively.
    Assume that the list always exists and can be empty or contain only numbers.

    #12

    @param list_of_numbers: list of integers.
    @return: sum of numbers in list
    """
    if len(list_of_numbers) == 0:
        return 0
    else:
        return list_of_numbers[0] + recursive_sum(list_of_numbers[1:])


# print(recursive_sum([]))  # 0
# print(recursive_sum([1, 2, 3]))  # 6
# print(recursive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55


class Stargate:
    """
    Class Stargate.

    Stargate is a device that creates a wormhole between it and another stargate that can be used to travel between two
    stargates almost instantly. Stargate can dial (connect) to another stargate and a stargate can be connected to
    (dialed to) by another stargate. Each stargate can only have one active connection. A stargate can be only connected
    to if it is currently disconnected. When a stargate connects to a stargate it means that the destination stargate is
    also connected to the stargate that initiated the connection (the one who dialed). When one of the stargates that is
    connected disconnects, the other disconnects also. To dial out (initiate the connection it needs to have a Dial Home
    Device (DHD). Think of the DHD of like a controller. If it doesn't have one, it can oly be dialed to by another
    stargate (it can't dial out) and it can't initiate a disconnect (remains connected until the other stargate
    initiates the disconnect).
    """

    def __init__(self, planet_name: str, has_dial_home_device: bool):
        """
        Construct a new stargate.

        :param planet_name: The name of the planet the stargate is on. String
        :param has_dial_home_device: Does the stargate have a Dial Home Device. Boolean
        """
        self.planet_name = planet_name
        self.has_dial_home_device = has_dial_home_device

    def get_planet_name(self):
        """
        Get planet name.

        :return: The name of the planet the stargate is on. String
        """
        return self.planet_name

    def is_connected(self):
        """
        Whether is connected.

        :return: Is the stargate currently connected or not. Boolean
        """
        pass

    def get_connected_stargate(self):
        """
        Get connected stargate.

        :return: The stargate this stargate is connected to. None if not connected. Stargate or None
        """
        pass

    def get_connected_planet_name(self):
        """
        Get connected planet name.

        :return: The name of the planet that the stargate that this stargate is connected to is on. None if not connected. String or None
        """
        pass

    def dial(self, destination):
        """
        Dial.

        Dial out to another stargate. This can only succeed if these criteria are met:
        * this stargate is not connected
        * this stargate has a Dial Home Device
        * the destination is an instance of the Stargate class
        * the destination stargate is currently not connected
        * this stargate is not trying to connect to itself

        :param destination: The stargate that this stargate should connect to. Stargate
        :return: Did the two stargates connect successfully. Boolean
        """
        pass

    def disconnect(self):
        """
        Disconnect.

        Disconnect this stargate and the stargate that this stargate is connected to if this stargate is currently
        connected.
        """
        pass


class Student:
    """Student class."""

    def __init__(self, curriculum):
        """
        Constructor.

        :param curriculum: the students curriculum.
        """
        self.curriculum = curriculum

    def add_subject_to_curriculum(self, subject):
        """
        Add the given subject to the students curriculum.

        If the subject is already in the curriculum, rewrite the EAPs.

        :param subject: the subject to be added to the curriculum.
        :param eap: how many EAPs the subject is worth.
        """
        pass

    def add_grade(self, subject, grade):
        """
        Add grade.

        Add the grade for the subject to students record if the subject is in the students curriculum.
        If the student already has a grade for said subject, rewrite it.
        The grade must be an integer between 0-5 (both included).

        :param subject: the subject for which the students has been given a grade.
        :param grade: the grade the student received. Must be between 0-5 (both included).
        """
        pass

    def get_subject_grade(self, subject):
        """
        Get subject grade.

        Return the grade the student has received for the given subject.
        If the student has not received a grade for the subject yet return None.
        :param subject: the subject which grade to return.
        :return: the received grade or None.
        """
        pass

    def get_average_grade(self):
        """
        Calculate the average of all grades on the students record.

        If a student has failed a subject (the grade is 0), don't count it.
        :return: the average grade with two decimal places.
        """
        pass

    def get_eaps(self):
        """
        Get EAP-s.

        Calculate, how many EAPs does the student currently have for passed subjects.
        A subject is passed when the student has received a grade greater than 0 for it.
        :return: the nr of EAPs.
        """
        pass

    def get_curriculum(self):
        """
        Get the students curriculum.

        :return: a Curriculum object.
        """
        return self.curriculum


class Subject:
    """Subject class."""

    def __init__(self, name, eaps):
        """
        Constructor.

        :param name: name of the subject.
        :param eaps: how many EAPs the subject is worth.
        """
        self.name = name
        self.eaps = eaps

    def get_eaps(self):
        """
        Return how many EAPs the subject is worth.

        :return: nr of EAPs
        """
        return self.eaps


class Curriculum:
    """Curriculum class."""

    def __init__(self):
        """Constructor."""
        self.curriculum = []

    def get_subject(self, name):
        """
        Get a subject from the curriculum by name.

        :param name: name of the subject.
        :return: subject object.
        """
        for n in self.curriculum:
            if n == name:
                return n

    def add_subject(self, subject):
        """
        Add the subject to curriculum.

        :param subject: the subject to be added.
        """
        pass

    def get_all_subjects(self):
        """
        Get all subjects.

        :return: al list of all the subjects in the curriculum.
        """
        return self.curriculum

    def add_subject_grade(self, subject, grade):
        """
        Add subject grade.

        Add the grade for the subject to students record if the subject is in the students curriculum.
        If the student already has a grade for said subject, rewrite it.
        The grade must be an integer between 0-5 (both included).

        :param subject: the subject for which the students has been given a grade.
        :param grade: the grade the student received. Must be between 0-5 (both included).
        """
        pass

    def get_grades(self):
        """
        Return a dictionary where keys are subjects and values are grades.

        The dictionary must include all subjects in teh curriculum, including those the student has not received a grade for yet.
        :return: dictionary.
        """
        pass


if __name__ == '__main__':
    # assert transactions("A,B,100") == [0, 200, 100]
    # assert transactions("C,A,200") == [300, 100, -100]
    # assert transactions("") == [100, 100, 100]
    # assert transactions("0,A,1000") == [1100, 100, 100]
    # assert transactions("A,B,10 B,C,10 0,A,20") == [110, 100, 110]
    #
    # OOP1 - stargate

    # sg1 = Stargate("Earth", True)
    # sg2 = Stargate("Another planet", False)
    # assert sg1.dial(sg2) is True
    # assert sg1.get_connected_planet_name() == "Another planet"
    # sg2.disconnect()
    # assert sg2.get_connected_planet_name() == "Earth"
    # sg1.disconnect()
    # assert sg2.get_connected_planet_name() is None
    # assert sg2.dial(sg1) is False
    #
    # OOP2 - student
    student = Student(Curriculum())

    subj1 = Subject("lineaar", 6)
    subj2 = Subject("matanaal", 5)
    subj3 = Subject("java", 4)

    student.get_curriculum().add_subject(subj1)
    student.get_curriculum().add_subject(subj2)
    student.get_curriculum().add_subject(subj3)

    student.add_grade(subj1, 3)
    student.add_grade(subj2, 5)


    assert student.get_subject_grade(subj3) is None
    # assert student.get_eaps() == 11
    assert student.get_subject_grade(subj2) == 5
    assert student.get_average_grade() == 4

    student.add_grade(subj2, 3)

    assert student.get_subject_grade(subj2) == 3
    assert student.get_average_grade() == 3

    assert student.get_curriculum().get_subject("java") == subj3
