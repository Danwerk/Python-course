def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Calculate the meeting position of 2 jangurus.
    @:param pos1: position of first janguru
    @:param jump_distance1: jump distance of first janguru
    @:param sleep1: sleep time of first janguru
    @:param pos2: position of second janguru
    @:param jump_distance2: jump distance of second janguru
    @:param sleep2: sleep time of second janguru

    @:return positions where jangurus first meet
    """

    for time in range(1000):
        if time % sleep1 == 0:
            pos1 += jump_distance1
        if time % sleep2 == 0:
            pos2 += jump_distance2
        if pos1 == pos2:
            return pos1
    return -1



print(meet_me(10, 7, 7, 5, 8, 6))  # => 45


