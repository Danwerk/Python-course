"""Janguru."""


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


