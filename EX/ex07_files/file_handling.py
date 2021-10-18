import csv
'''


csv_list = []
with open('csv_date.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        csv_list.append(row)

list_of_dicts = []
lists = csv_list
if lists:
    header_list = lists[0]
    lists.remove(header_list)
    print(lists)
    for content_list in lists:
        dict = {}
        for i in range(len(header_list)):
            key = header_list[i]
            value = content_list[i]
            dict[key] = value
        list_of_dicts.append(dict)

print(list_of_dicts)
'''
'''
dates = []
towns = []
result = [["name", "town", "date"]]
with open('csv_date.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
        dates.append(row)
with open('csv_town.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
        towns.append(row)
for row in dates:
    name = row[0]
    date = row[1]
    result.append([name, '-', date])

print(result)
#print(dates)
print(towns)


for row2 in towns:
    name2 = row2[0]
    town = row2[1]
    for elem in result[1:]:
        if name2 == elem[0]:
            elem[1] = town
            continue
    result.append([name2, town, '-'])



with open('test.txt', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in result:
        csv_writer.writerow(row)

print(result)
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
    for row in dates:
        name = row[0]
        date = row[1]
        result.append([name, '-', date])
    for row in towns:
        name = row[0]
        town = row[1]
        for rows in result:
            if name == rows[0]:
                rows[1] = town
    with open('test.txt', 'w', newline='') as csv_file:
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