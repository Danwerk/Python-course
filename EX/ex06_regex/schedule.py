"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_filename = 'test.txt'
    output_filename = 'after_test.txt'
    with open(input_filename) as f:  # Opens file with name of "test.txt"
        data = f.read()
        make_sence = converted_time(data)
    with open(output_filename, "w") as f:
        f.write(make_sence)


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    '''act = correct_regex_dict(input_string)
    time_width = 8
    for time in act:
        list_to_string = ' '.join(act[time])

        print(f'| {time:>{time_width}} | {list_to_string:>20} |')'''

    #return create_schedule_file(input_filename='test.txt', output_filename='after_test.txt')
    return draw_table(input_string)


def draw_table(input_string):
    for i in create_table(input_string):
        print(i)


def create_table(input_string):
    table = []
    act_schedule = []
    for i in converted_time(input_string):
        time = i[0]
        act = ', '.join(i[1])
        act_schedule.append(f'| {time:>{get_table_sizes(input_string)[0]}} | {act:<{get_table_sizes(input_string)[1]}} |')

    str_time = 'time'
    str_items = 'items'
    table_horizontal = ((get_table_sizes(input_string)[0] + get_table_sizes(input_string)[1] + 7) * '-')
    table.append(table_horizontal)
    table.append(f'| {str_time:>{get_table_sizes(input_string)[0]}} | {str_items:<{get_table_sizes(input_string)[1]}} |')
    table.append(table_horizontal)
    table.extend(act_schedule)
    table.append(table_horizontal)

    #print(f'| {time:>{get_table_sizes(input_string)[0]}} | {act:<{get_table_sizes(input_string)[1]}} |')
    return table


def get_table_sizes(input_string):
    max_len_time = 0
    max_len_act = 0
    for objects in converted_time(input_string):
        time = objects[0]
        act = ', '.join(objects[1])
        amount_time = len(time)
        amount_act = len(act)
        if amount_time > max_len_time:
            max_len_time = amount_time
        if amount_act > max_len_act:
            max_len_act = amount_act

    return max_len_time, max_len_act


def converted_time(input_string):
    conv_list = []
    for tupl in sorted_list(input_string):
        time = tupl[0]
        time = re.split(r'\D', time)
        hours = int(time[0])
        minutes = int(time[1])
        if hours > 12 and hours < 24:
            hours -= 12
            match = f'{hours}:{minutes:02} PM', tupl[1]
            conv_list.append(match)
            continue
        if 0 < hours < 12:
            hours = hours
            match = f'{hours}:{minutes:02} AM', tupl[1]
            conv_list.append(match)
            continue
        if hours == 0:
            hours = 12
            match = f'{hours}:{minutes:02} AM', tupl[1]
            conv_list.append(match)
    return conv_list


def sorted_list(input_string):
    sorted_items = sorted(correct_regex_dict(input_string).items(), key=lambda x: x[0])
    return sorted_items


def correct_regex_dict(input_string):
    dic = {}
    for tuplet in correct_regex_list(input_string):
        key = tuplet[0]
        value = tuplet[1]
        if key not in dic:
            dic[key] = [value]
        if value not in dic[key]:
            dic[key].append(value)
    return dic


def correct_regex_list(input_string: str):
    regex = re.findall(r"(\d{1,2}\D\d{1,2})\s+([A-Za-z][A-Za-z]*)", input_string)

    elem_list = []

    for match in regex:
        match = list(match)
        match[1] = match[1].lower()
        time = re.split(r'\D', match[0])
        hours = int(time[0])
        minutes = int(time[1])
        if hours < 24 and minutes < 60:
            match = f'{hours:02}:{minutes:02}', match[1]
            elem_list.append(match)
    return elem_list


print(create_schedule_string('''    A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum
     ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.
     Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.
     Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id purus diam. 24:01 Donec blandit,
     est nec semper convallis, arcu libero lacinia ex, eu placerat risus est non tellus.
    Orci varius natoque penatibus et magnis dis 0:12 parturient montes, nascetur ridiculus mus. Curabitur pretium at metus
    eget euismod. Nunc sit amet fermentum urna. Maecenas commodo ex turpis, et malesuada tellus sodales non. Fusce elementum
     eros est. Phasellus nibh magna, tincidunt eget magna nec, rhoncus lobortis dui. Sed fringilla risus a justo tincidunt,
     in tincidunt urna interdum. Morbi varius lobortis tellus, vitae accumsan justo commodo in. 12:001 Nullam eu lorem leo.
     Vestibulum in varius magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
      0:00 Aliquam ac velit sit amet nunc dictum aliquam pulvinar at enim. Nulla aliquam est quis sem laoreet, eu venenatis
      risus hendrerit. Donec ac enim lobortis, bibendum lacus quis, egestas nisi.

    08:01 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 18:19 a bibendum enim. Praesent
     dictum ante eget turpis tempor, 00:0 porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae,
     pulvinar nisl. Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. 8:8 Integer mollis nisi sed fermentum
      efficitur. Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id 18:19 purus
      diam. 18:19 Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus.

    11:0 lorem
    0:60 bad
    1:2   goodone yes
    15:0 nocomma,
     18:19 yes-minus
      21:59 nopoint.
    23-59 canuseminusthere  22,0 CommaIsAlsoOk
    5:6

'''))
