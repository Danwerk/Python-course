def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.

    :param text: string
    :return: string
    """

    nums_from_string = []
    for i in text:
        if i.isdigit():
            nums_from_string.append(i)
    str_number = "".join(nums_from_string) #converts list numbers to a string

    if len(str_number) < 11:
        return 'Not enough numbers!'
    elif len(str_number) > 11:
        return 'Too many numbers!'
    else:
        return str_number


print(find_id_code(""))
print(find_id_code("123456789123456789"))
print(find_id_code("ID code is: 49403136526"))
print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))
