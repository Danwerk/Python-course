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


print(find_id_code(""))
print(find_id_code("123456789123456789"))
print(find_id_code("ID code is: 49403136526"))
print(find_id_code("efs4  9   #4aw0h 3r 1a36g5j2!!6-"))
