"""Program that creates beautiful pyramids."""


def make_pyramid(base: int, char: str) -> list:
    """
    Construct a pyramid with given base.

    Pyramid should consist of given chars, all empty spaces in the pyramid list are ' '. Pyramid height depends on base length. Lowest floor consists of base-number chars.
    Every floor has 2 chars less than the floor lower to it.
    make_pyramid(3, "A") ->
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    make_pyramid(6, 'a') ->
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    :param base: int
    :param char: str
    :return: list
    """
    empty_string = 0
    base_stage = (base, empty_string)
    tupl_to_append = [base_stage]
    next_base = base_stage

    if base % 2 != 0:  # odd num base
        while next_base[0] > 1:
            empty_string += 1
            next_base = (base - 2, empty_string)
            tupl_to_append.append(next_base)
            base -= 2

    elif base % 2 == 0:  # even num base
        while next_base[0] > 2:
            empty_string += 1
            next_base = (base - 2, empty_string)
            tupl_to_append.append(next_base)
            base -= 2

    tupl_to_append.reverse()

    lis = [' ' * tupl_to_append[i][1] + char * tupl_to_append[i][0] + ' ' * tupl_to_append[i][1] for i in
           range(len(tupl_to_append))]
    pyramid = [list(j) for j in lis]
    return pyramid


def join_pyramids(pyramid_a: list, pyramid_b: list) -> list:
    """
    Join together two pyramid lists.

    Get 2 pyramid lists as inputs. Join them together horizontally. If the the pyramid heights are not equal, add empty lines on the top until they are equal.
    join_pyramids(make_pyramid(3, "A"), make_pyramid(6, 'a')) ->
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]

    :param pyramid_a: list
    :param pyramid_b: list
    :return: list
    """
    pyramid_a_base_len = len(pyramid_a[0])
    pyramid_b_base_len = len(pyramid_b[0])
    pyramid_a.reverse()
    pyramid_b.reverse()
    if len(pyramid_a) == len(pyramid_b):
        for i in range(len(pyramid_a)):
            pyramid_a[i].extend(pyramid_b[i])
        pyramid_a.reverse()
        return pyramid_a

    elif len(pyramid_b) > len(pyramid_a):
        for i in range(len(pyramid_b)):
            if i > len(pyramid_a) - 1:
                whitespaces = list(' ' * pyramid_a_base_len)
                whitespaces.extend(pyramid_b[i])
                pyramid_a.append(whitespaces)

            else:
                pyramid_a[i].extend(pyramid_b[i])
        pyramid_a.reverse()
        return pyramid_a

    elif len(pyramid_a) > len(pyramid_b):
        for i in range(len(pyramid_a)):
            if i > len(pyramid_b) - 1:
                whitespaces = list(' ' * pyramid_b_base_len)
                whitespaces.extend(pyramid_a[i])
                pyramid_b.append(whitespaces)

            else:
                pyramid_b[i].extend(pyramid_a[i])

        pyramid_b.reverse()

        return pyramid_b


a = join_pyramids(make_pyramid(9, "A"), make_pyramid(5, "B"))
for i in a:
    print(i)


def to_string(pyramid: list) -> str:
    """
    Return pyramid list as a single string.

    Join pyramid list together into a string and return it.
    to_string(make_pyramid(3, 'A')) ->
    '''
     A
    AAA
    '''

    :param pyramid: list
    :return: str
    """
    p = ''

    for i in pyramid:
        p += ''.join(i) + '\n'
    pyramid_str = p.rstrip()
    return pyramid_str


print(to_string([
    [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
    [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
    ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
]))

if __name__ == '__main__':
    '''
    pyramid_a = make_pyramid(3, "A")
    print(pyramid_a)  # ->
    """
    [
        [' ', 'A', ' '],
        ['A', 'A', 'A']
    ]
    """

    pyramid_b = make_pyramid(6, 'a')
    print(pyramid_b)  # ->
    """
    [
        [' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'a', 'a', 'a', 'a', ' '],
        ['a', 'a', 'a', 'a', 'a', 'a']
    ]
    """
'''
    joined = join_pyramids([[' ', 'A', ' '], ['A', 'A', 'A']],
                           [[' ', ' ', 'a', 'a', ' ', ' '], [' ', 'a', 'a', 'a', 'a', ' '],
                            ['a', 'a', 'a', 'a', 'a', 'a']])
    # print(joined)  # ->
    """
    [
        [' ', ' ', ' ', ' ', ' ', 'a', 'a', ' ', ' '],
        [' ', 'A', ' ', ' ', 'a', 'a', 'a', 'a', ' '],
        ['A', 'A', 'A', 'a', 'a', 'a', 'a', 'a', 'a']
    ]
    """

    # pyramid_string = to_string(joined)
    # print(pyramid_string)  # ->
    """
         aa  
     A  aaaa 
    AAAaaaaaa
    """
