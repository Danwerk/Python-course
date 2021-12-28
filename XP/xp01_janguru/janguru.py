"""Janguru."""

'''
def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus."""
    for time in range(100000):
        if time % sleep1 == 0:
            pos1 += jump_distance1
        if time % sleep2 == 0:
            pos2 += jump_distance2
        if pos1 == pos2:
            return pos1
    return -1
'''


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus."""
    if pos1 and pos2 >= 1000000:
        for time in range(1000000, 1000000000):
            if time % sleep1 == 0:
                pos1 += jump_distance1
            if time % sleep2 == 0:
                pos2 += jump_distance2
            if pos1 == pos2:
                return pos1
        return -1
    else:
        for time in range(100000):
            if time % sleep1 == 0:
                pos1 += jump_distance1
            if time % sleep2 == 0:
                pos2 += jump_distance2
            if pos1 == pos2:
                return pos1
        return -1


if __name__ == "__main__":
    print(meet_me(1, 2, 1, 2, 1, 1))  # => 3
    print(meet_me(1, 2, 3, 4, 5, 5))  # => -1
    print(meet_me(10, 7, 7, 5, 8, 6))  # => 45
    print(meet_me(100, 7, 4, 300, 8, 6))  # => 940
    print(meet_me(1, 7, 1, 15, 5, 1))  #  => 50
    print(meet_me(0, 1, 1, 1, 1, 1))  # => -1
    print(meet_me(1, 2, 1, 1, 3, 1))  # => -1