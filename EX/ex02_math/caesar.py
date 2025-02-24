"""Caesar."""


def encode(message: str, shift: int) -> str:
    """Encode a message using a Caesar cipher."""
    ascii_list = []
    crypted = []
    for character in message:
        ascii_list.append(ord(character))

    for i in ascii_list:
        if i >= 97 and i <= 122:
            i = i + shift
            if i > 122:
                crypted.append((i - 97) % 26 + 97)
            else:
                crypted.append(i)
        else:
            i = i
            crypted.append(i)

    mystring = ""
    for char in crypted:
        mystring = mystring + chr(char)
    return mystring
