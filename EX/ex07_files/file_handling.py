import csv

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