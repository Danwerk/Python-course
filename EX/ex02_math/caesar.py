"""Caesar."""


def encode(message: str, shift: int) -> str:
    """
       Encode a message using a Caesar cipher.

       Presume the message is already lowercase.
       For each letter of the message, shift it forward in the alphabet by shift amount.
       If the character isn't a letter, keep it the same.

       For example, shift = 3 then a => d, b => e, z => c (see explanation below)

       Shift:    0 1 2 3
       Alphabet:       A B C D E F G H I J
       Result:   A B C D E F G H I J

       Examples:
       1. encode('i like turtles', 6) == 'o roqk zaxzrky'
       2. encode('example', 1) == 'fybnqmf'
       3. encode('the quick brown fox jumps over the lazy dog.', 7) == 'aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.'

       :param message: message to be encoded
       :param shift: shift for encoding
       :return: encoded message
       """
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


print(encode("hmm... wh4t, oh what?!QWERTYUIOPÜÕASDFGHJKLÖÄZXCVBNM;:?‽", 4))
print(encode("hmm... wh4t, oh what?!?‽", 4))
print(encode("helkkki asdf 2", 100))
