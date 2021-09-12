pos1 = 1
pos2 = 4
jump_distance1 = 2
jump_distance2 = 5
sleep1 = 3
sleep2 = 5
for time in range(1000):
    if time % sleep1 == 0:
        pos1 += jump_distance1
    if time % sleep2 == 0:
        pos2 += jump_distance2
        if pos1 == pos2:
            print(pos1)
        else:
            print('-1')
            break

