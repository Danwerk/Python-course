"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_filename = 'test.txt'
    output_filename = 'after_test.txt'
    with open(input_filename) as f:  # Opens file with name of "test.txt"
        data = f.read()
        make_sence = create_schedule_string(data)
    with open(output_filename, "w") as f:
        f.write(make_sence)


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    return draw_schedule_table(input_string)


def draw_schedule_table(input_string):
    """Draw schedule table."""
    if input_string == '' or correct_regex_list(input_string) == []:
        string_table = ''
        for i in draw_empty_schedule_table(input_string):
            list_table = ''.join(i) + '\n'
            string_table += list_table
        return string_table
    else:
        string_table = ''
        for i in create_table(input_string):
            list_table = ''.join(i) + '\n'
            string_table += list_table

        return string_table


def draw_empty_schedule_table(input_string):
    """Draw an empty schedule table."""
    table = []
    str_time = 'time'
    str_items = 'items'
    str_message = 'No items found'
    table_horizontal = ((18) * '-')
    table.append(table_horizontal)
    table.append(f'| {str_time:>{get_table_sizes(input_string)[0] + 1}} | {str_items:<{get_table_sizes(input_string)[1]+1}} |')
    table.append(table_horizontal)
    table.append(f'| {str_message:{get_table_sizes(input_string)[0] + get_table_sizes(input_string)[1] + 3}} |')
    table.append(table_horizontal)
    return table


def create_table(input_string):
    """Create schedule table from list."""
    table = []
    act_schedule = []
    time_size = get_table_sizes(input_string)[0]
    act_size = get_table_sizes(input_string)[1]
    for i in correct_convert_list(input_string):
        time = i[0]
        act = ', '.join(i[1])
        act_schedule.append(f'| {time:>{time_size}} | {act:<{act_size}} |')

    str_time = 'time'
    str_items = 'items'
    table_horizontal = ((time_size + act_size + 7) * '-')
    table.append(table_horizontal)
    table.append(f'| {str_time:>{time_size}} | {str_items:<{act_size}} |')
    table.append(table_horizontal)
    table.extend(act_schedule)
    table.append(table_horizontal)

    return table


def get_table_sizes(input_string):
    """Get sizes of table."""
    max_len_time = 4
    max_len_items = 5
    for objects in correct_convert_list(input_string):
        time = objects[0]
        items = ', '.join(objects[1])
        amount_time = len(time)
        amount_items = len(items)
        if amount_time > max_len_time:
            max_len_time = amount_time
        if amount_items > max_len_items:
            max_len_items = amount_items

    return max_len_time, max_len_items


def correct_convert_list(input_string):
    """Convert from 24 hours to 12 hours. It returns a list of tuples that are sorted."""
    conv_list = []
    for tupl in sorted_list(input_string):
        time = tupl[0]
        time = re.split(r'\D', time)
        hours = int(time[0])
        minutes = int(time[1])
        if 12 < hours < 24:
            hours -= 12
            match = f'{hours}:{minutes:02} PM', tupl[1]
            conv_list.append(match)
            continue
        if 0 < hours < 12:
            hours = hours
            match = f'{hours}:{minutes:02} AM', tupl[1]
            conv_list.append(match)
            continue
        if hours == 12 and minutes >= 0:
            hours = hours
            match = f'{hours}:{minutes:02} PM', tupl[1]
            conv_list.append(match)
            continue
        if hours == 0:
            hours = 12
            match = f'{hours}:{minutes:02} AM', tupl[1]
            conv_list.append(match)
    return conv_list


def sorted_list(input_string):
    """Return sorted keys, List of tuples."""
    return sorted(correct_regex_dict(input_string).items(), key=lambda x: x[0])


def correct_regex_dict(input_string):
    """Return dictionary from regex list, Time is key(string) and item is value(list)."""
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
    """Find all matches from text, using regex, Returns list of tuples."""
    regex = re.findall(r"(?<=\n|\s)(\d{1,2}\D\d{1,2})\s+([A-Za-z][A-Za-z]{0,})", input_string)

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


print(create_schedule_string('y'))
print(create_schedule_string('''ter 12:23 mingi v lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum
     ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.
     Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.
     Suspendisse sollicitudin sapien dui, vitae tem'''))
print(create_schedule_string('''start hnzlfygdm -1B18 xSRomC kejmfidlx uivyg mgbtux bncvx mrshl hnpmhc sbowlvngda nxahig 18a23   OmpMFYDWP zrlev vdhjknem vxmook ujkuaehfyb 6.32   ENkDfQQeD ifqtyocr ybyrzr yiwgkpeutw jpreso wdiiho 20?59   OMPmfYdWp pxltcum djatyjjnd mpktejy atdnu cnythzufvg ekdyj erymdknul wfpfbf fvzcgteyw cyynsgko 1?20  XSRoMC gavmbxnrst xymkcuy imrewd 24-23    vUiVdTPrbQ amsdd rjvpao uygkpkrirp 14b16    KWPgeacYx spcjelglx plrgsrmfvu ttrxcq okghzgnyix myoih ckpheejdwh sgzzbbmeky mgksnv iaxviulk uezrjtg 15=30  yorlCqcOT ymynrxuj vtcgaf gytjubr ooweudok uikpwhm tezwtwztby usxmtzhto lvvaao gijadqwfcx hlmlflqn 16?39   XSRoMc prridp lmsndin rhbcnso hgvnjuiuts cmastjl khvag tbtcyr sxjqnk dnmbammd 0?34    ompMFyDWP oniyllj ylxop dxdzyiql ugmfnob wkxplf byrlx pcaou dwyts 16-20   EnkDFQqed 13B20    hZDmDIICPW mjnfrrptc zaypth odykc oazfktj jpgnjlj nsljirlyfd olszgpifu jpgrfknxa pkqucv mrcukwau 15!41    XsrOMC xlkpugdyr kqjecxtiyr txwrjznvfv 19-44 VUivdtPRBq ijfznhcea lvpapq ifmzjooqg 0b03 oMEzZjX lambfsrk zmkxyoy itcrjqguy sxgyjujcch flfguziwjg pyhpeiui zsomzj hastcx fyygzrpfja bmgzujud 6,41  OmEzZJx wsisnuyfp jllrj yhdlmnwn ipwpz 18.43    xsROmC rjpwclkdig hgdvynaan hgfyt oeklfm ztmufax qweidnofy hiqex evbrjtp sjrfsb 16=52    yORLCqcOT gthtedyg sehmkjapj inxbpphsut gougkz vyujftwjqa rfzzuihfn fnzcvanv abpom oztufugmir 21-37 enkDFQQEd muqbmgqxul dgjsimaqpn nezklcp peyltsmob ogyeeiquld'''))
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
      diam. 18:19 Donec 12:39 djlnvo blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus.

    11:0 lorem
    0:60 bad
    1:2   goodone yes
    15:0 nocomma,
     18:19 yes-minus
      21:59 nopoint.
    23-59 canuseminusthere  22,0 CommaIsAlsoOk
    5:6

'''))
print(create_schedule_string("msubelvhht 12=00 wwguHfBZoB qxivykdl"))
