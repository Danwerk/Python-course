"""Files."""

import csv
from datetime import datetime


def is_int(value):
    return value.isdigit()


def is_date(value):
    format = "%d.%m.%Y"
    try:
        datetime.strptime(value, format)
        return True
    except ValueError:
        return False

'''
csv_list = []
with open('csv_town.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        csv_list.append(row)
if len(csv_list) == 0:
    print(list({}))
else:

    types_dict = {}
    header = csv_list[0]
    # print(header)
    for row in csv_list[1:]:
        for i, value in enumerate(row):
            if value == '-':
                if header[i] not in types_dict:
                    types_dict[header[i]] = ['-']
                else:
                    types_dict[header[i]].append('-')
                continue
            if is_date(value):
                if header[i] not in types_dict:
                    types_dict[header[i]] = ['date']
                    continue
                else:
                    types_dict[header[i]].append('date')
                    continue

            if not is_date(value) and not is_int(value):
                if header[i] not in types_dict:
                    types_dict[header[i]] = ['str']
                    continue
                else:
                    types_dict[header[i]].append('str')
                    continue


            if is_int(value):
                if header[i] not in types_dict:
                    types_dict[header[i]] = ['int']
                else:
                    types_dict[header[i]].append('int')
                continue
            else:
                if header[i] not in types_dict:
                    types_dict[header[i]] = ['str']
                else:
                    types_dict[header[i]].append('str')
    #print(types_dict)


    # get final right type and write into dictionary
    for key in types_dict:
        val = types_dict[key]
        if 'str' in val:
            types_dict[key] = 'str'
            continue
        if 'int' in val and 'str' not in val and 'date' not in val:
            types_dict[key] = 'int'
        if 'date' in val and 'str' not in val and 'int' not in val:
            types_dict[key] = 'date'
        if '-' in val:
            continue
    #print(types_dict)




    final_list = []
    for row in csv_list[1:]:
        final_dict = {}
        for i, value in enumerate(row):
            if value == '-':
                final_dict[header[i]] = None
                continue
            if types_dict[header[i]] == 'str':
                final_dict[header[i]] = str(value)
                continue
            if types_dict[header[i]] == 'int':
                final_dict[header[i]] = int(value)
                continue
            if types_dict[header[i]] == 'date':
                final_dict[header[i]] = datetime.strptime(value, '%d.%m.%Y').date()
        final_list.append(final_dict)

    print(final_list)



'''

























'''
csv_list = []
with open('csv_town.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        csv_list.append(row)
print(csv_list)
list_of_dicts = []
lists = csv_list
if lists:
    header_list = lists[0]
    lists.remove(header_list)
    for content_list in lists:
        dic = {}
        for i in range(len(header_list)):
            key = header_list[i]
            value = content_list[i]
            dic[key] = value
        list_of_dicts.append(dic)
    #print(list_of_dicts)

'''




def read_file_contents(filename: str) -> str:
    """Read file contents into string."""
    with open(filename) as f:  # Opens file with name of "test.txt"
        data = f.read()  # Reads all the lines from the file and saves it as a string.
    return data


def read_file_contents_to_list(filename: str) -> list:
    """Read file contents into list of lines."""
    list_of_lines = read_file_contents(filename).split('\n')
    return list_of_lines


def read_csv_file(filename: str) -> list:
    """Read CSV file into list of rows."""
    csv_list = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_list.append(row)
    return csv_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """Write contents to file."""
    with open(filename, "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """Write lines to file."""
    with open(filename, "w") as f:
        lines = '\n'.join(lines)
        f.write(lines)


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_file: str, towns_file: str, csv_output: str) -> None:
    """
    Merge information from two files into one CSV file.

    dates_file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    towns_file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_file: Input file with names and dates.
    :param towns_file: Input file with names and towns.
    :param csv_output: Output CSV-file with names, towns and dates.
    :return: None
    """
    dates = []
    towns = []
    result = [["name", "town", "date"]]
    with open(dates_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            dates.append(row)
    with open(towns_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            towns.append(row)

    for date_person in dates:
        name, date = date_person
        result.append([name, '-', date])

    for town_person in  towns:
        name2, town = town_person
        for elem in result[1:]:
            if name2 == elem[0]:
                elem[1] = town
                break
        else:
            result.append([name2, town, '-'])

    with open(csv_output, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in result:
            csv_writer.writerow(row)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.
    Header line will be used for dict keys.

    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:

    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    list_of_dicts = []
    lists = read_csv_file(filename)
    if lists:
        header_list = lists[0]
        lists.remove(header_list)
        for content_list in lists:
            dic = {}
            for i in range(len(header_list)):
                key = header_list[i]
                value = content_list[i]
                dic[key] = value
            list_of_dicts.append(dic)
        return list_of_dicts
    else:
        return []


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None"""
    list_of_lists = []
    header = []  # header contains e.g name, hobby and etc
    for dic in data:  # get dictionary from list
        for key in dic:  # get dict key
            if key in header:  # if the key is already in header list, then go ahead
                continue
            else:
                header.append(key)
    list_of_lists.append(header)

    for dict in data:
        content = []
        for i in header:
            if i in dict.keys():  # check if element i is in dict
                content.append(dict[i])
            else:
                content.append('')
        list_of_lists.append(content)
    if len(data) == 0:
        list_of_lists = ''
        return write_csv_file(filename, list_of_lists)
    else:
        return write_csv_file(filename, list_of_lists)


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.
    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """

    csv_list = read_csv_file(filename)
    types_dict = {}
    if len(csv_list) == 0:
        return []
    else:
        header = csv_list[0]
        for row in csv_list[1:]:
            for i, value in enumerate(row):
                if value == '-':
                    if header[i] not in types_dict:
                        types_dict[header[i]] = ['-']
                    else:
                        types_dict[header[i]].append('-')
                    continue
                if is_date(value):
                    if header[i] not in types_dict:
                        types_dict[header[i]] = ['date']
                        continue
                    else:
                        types_dict[header[i]].append('date')
                        continue

                if not is_date(value) and not is_int(value):
                    if header[i] not in types_dict:
                        types_dict[header[i]] = ['str']
                        continue
                    else:
                        types_dict[header[i]].append('str')
                        continue

                if is_int(value):
                    if header[i] not in types_dict:
                        types_dict[header[i]] = ['int']
                    else:
                        types_dict[header[i]].append('int')
                    continue
                else:
                    if header[i] not in types_dict:
                        types_dict[header[i]] = ['str']
                    else:
                        types_dict[header[i]].append('str')

    # get final right type and write into dictionary
        for key in types_dict:
            val = types_dict[key]
            if 'str' in val:
                types_dict[key] = 'str'
                continue
            if 'int' in val and 'str' not in val and 'date' not in val:
                types_dict[key] = 'int'
            if 'date' in val and 'str' not in val and 'int' not in val:
                types_dict[key] = 'date'
            if '-' in val:
                continue

        final_list = []
        for row in csv_list[1:]:
            final_dict = {}
            for i, value in enumerate(row):
                if value == '-':
                    final_dict[header[i]] = None
                    continue
                if types_dict[header[i]] == 'str':
                    final_dict[header[i]] = str(value)
                    continue
                if types_dict[header[i]] == 'int':
                    final_dict[header[i]] = int(value)
                    continue
                if types_dict[header[i]] == 'date':
                    final_dict[header[i]] = datetime.strptime(value, "%d.%m.%Y").date()
            final_list.append(final_dict)
        return final_list
