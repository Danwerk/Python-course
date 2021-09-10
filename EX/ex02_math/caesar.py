def encode(message: str, shift: int) -> str:
    ascii_list = []
    crypted = []
    for character in message:
        ascii_list.append(ord(character))

    for i in ascii_list:
        if i >= 97 and i <= 122:
            i = i + shift
            if i > 122:
                crypted.append((i + shift - 97) % 26 + 97)
            else:
                crypted.append(i)
        else:
            i = i
            crypted.append(i)

    mystring = ""
    for char in crypted:
        mystring = mystring + chr(char)
    return mystring


print(encode("hmm... wh4t, oh what?!QWERTYUIOPÜÕASDFGHJKLÖÄZXCVBNM;:?‽", 4))
print(encode("hmm... wh4t, oh what?!?‽", 4))
print(encode("helkkki asdf 2", 100))
