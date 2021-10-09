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
    for match in re.finditer(r"([A-ZÕÄÖÜ])(.*?)[\.!?]{1,}", text):
        reg_list.append(match.group(0))
    return reg_list


def find_words_from_sentence(sentence: str) -> list:
    """Given a sentence, return all words in that sentence."""
    reg_list = []
    for match in re.finditer(r"[A-ZÕÄÖÜa-zõäöpü0-9]{1}([a-zõäöü0-9]{0,})", sentence):
        reg_list.append(match.group(0))
    return reg_list


def find_words_from_sentences_only(text: str) -> list:
    """Given string text, return all words in that string that are a part of a sentence in that string."""
    reg_list = []
    sentences_list = find_sentences(text)
    list_to_str = ' '.join([str(item) for item in sentences_list])
    for match in re.finditer(r"[A-ZÕÄÖÜa-zõäöpü0-9]{1}([a-zõäöü0-9]{0,})", list_to_str):
        reg_list.append(match.group(0))
    return reg_list


def find_years(text: str) -> list:
    """Given string text, return a list of all 4-digit numbers (years) in that string."""
    reg_list = []
    for match in re.finditer(r"(?<!\d)\d{4}(?!\d)", text):   # ?<! looks if there is some digit before, ?! looks if there is a digits after. If not, then prints out a four digit num
        reg_list.append(int(match.group(0)))
    return reg_list


def find_phone_numbers(text: str) -> dict:
    """Given string text, return a dictionary of all the phone numbers in that text."""
    dict = {}
    regex = re.findall(r"(\+\d{3})?\s?(\d{7,8})", text)
    for tuplet in regex:
        key = tuplet[0]
        value = tuplet[1]
        if key not in dict:
            dict[key] = [value]
        else:
            dict[key].append(value)

    return dict


if __name__ == '__main__':
    print(find_words('KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))  # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']
    print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))  # ['Apelsin', 'Õun', 'Ahven']
    print(find_sentences(
        'See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))  # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']
    print(find_words_from_sentence("Super lause ää, sorry."))  # ['Super', 'lause', 'ää', 'sorry']
    print(find_words_from_sentences_only(
        'See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))  # ['See', 'on', 'esimene', 'ä', 'lause', 'See', 'on', 'teine', 'lause', 'Aga', 'kas', 'see', 'on']
    print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))  # [1998, 7777]
    print(find_phone_numbers(
        "+372 56887364  +37256887364  +33359835647  56887364"))  # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364']}
