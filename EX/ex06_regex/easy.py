"""Regex, yay!"""
import re


def find_words(text: str) -> list:
    """Given string text, return all the words in that string."""
    reg_list = []
    for match in re.finditer(r"[A-ZÕÄÖÜ]{1}[a-zõäöü]{1,}", text):
        reg_list.append(match.group(0))
    return reg_list


def find_words_with_vowels(text: str) -> list:
    """Given string text, return all the words in that string that start with a vowel."""
    reg_list = []
    for match in re.finditer(r"[AEIOUÕÄÖÜ]{1}[a-zõäöü]{1,}", text):
        reg_list.append(match.group(0))
    return reg_list


def find_sentences(text: str) -> list:
    """Given string text, return all sentences in that string."""
    reg_list = []
    for match in re.finditer(r"([A-ZÕÄÖÜ])(.*?)[\.!?]{1}", text):
        reg_list.append(match.group(0))
    return reg_list


def find_words_from_sentence(sentence: str) -> list:
    """Given a sentence, return all words in that sentence."""
    reg_list = []
    for match in re.finditer(r"[A-ZÕÄÖÜa-zõäöpü0-9]{1}([a-zõäöü0-9]{0,})", sentence):
        reg_list.append(match.group(0))
    return reg_list


def find_words_from_sentences_only(text: str) -> list:
    """
    Given string text, return all words in that string that are a part of a sentence in that string.

    A sentence is defined in function find_sentences().
    A word is defined in function find_words_from_sentence().

    :param text: given string to find words from
    :return: list of words found in sentences from given string
    """
    pass


def find_years(text: str) -> list:
    """
    Given string text, return a list of all 4-digit numbers (years) in that string.

    Only 4-digit numbers are considered years here.
    If there is a 5-digit number then that is not considered a year,
    nor will it give two years. So you can not split them up.

    Years must be found using regex.

    Hint: use lookbehind and lookahead to check what comes before and after the numbers.

    :param text: given string to find years from
    :return: list of years (integers) found in given string
    """
    pass


def find_phone_numbers(text: str) -> dict:
    """
    Given string text, return a dictionary of all the phone numbers in that text.

    Phone number might be preceded by area code. Are code is a combination of plus sign and three numbers.
    The phone number itself is a combination of 7-8 numbers.
    The phone number might be separated from the area code with a whitespace, but not necessarily.

    The function must return a dictionary where keys are the area codes
    and values are lists of the phone numbers with the corresponding area number.
    If a phone number does not have an area code given, its area code would be empty string,
    so in dictionary it would be like that: {"": ["56332456"]}.

    Phone numbers must be found using regex.

    :param text: given string to find phone numbers from
    :return: dict containing the numbers
    """
    pass


if __name__ == '__main__':
#    print(find_words(
 #       'KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))  # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']

    print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))  # ['Apelsin', 'Õun', 'Ahven']
    print(find_sentences(
        'See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))  # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']
    print(find_words_from_sentence("Super lause ää, ö, Ö sorry."))  # ['Super', 'lause', 'ää', 'sorry']
    print(find_words_from_sentences_only(
        'See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))  # ['See', 'on', 'esimene', 'ä', 'lause', 'See', 'on', 'teine', 'lause', 'Aga', 'kas', 'see', 'on']
    print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))  # [1998, 7777]
    print(find_phone_numbers(
        "+372 56887364  +37256887364  +33359835647  56887364"))  # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364']}
