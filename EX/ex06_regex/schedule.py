"""Create schedule from the given file."""
import re
from datetime import datetime

def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    return correct_regex_list(input_string)

    #for match in re.finditer(r"(\d{1,2}\D\d{1,2})\s?([A-Za-z][a-z]+)", input_string):
        #time_to_convert = match.group(1)
        #print(match.group(1) + ' ' + match.group(2))


def correct_regex_list(input_string: str):
    regex = re.findall(r"(\d{1,2}\D\d{1,2})\s+([A-Za-z][A-Za-z]+)", input_string)

    elem_list = []

    for match in regex:
        match = list(match)
        match[1] = match[1].lower()
        time = re.split(r'\D', match[0])
        hours = int(time[0])
        minutes = int(time[1])
        if hours > 12 and hours < 24:
            hours -= 12
            match = f'{hours}:{minutes:02} PM', match[1]
            elem_list.append(match)
            continue
        if 0 < hours < 12:
            hours = hours
            match = f'{hours}:{minutes:02} AM', match[1]
            elem_list.append(match)
            continue
        if hours == 0:
            hours = 12
            match = f'{hours}:{minutes:02} AM', match[1]
            elem_list.append(match)

    return elem_list


print(create_schedule_string('''A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 100 a bibendum enim. Praesent dictum
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
