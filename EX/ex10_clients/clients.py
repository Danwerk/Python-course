"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Client earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        money_per_day = (self.current_amount - self.starting_amount) / self.account_age
        return money_per_day


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    ret = []
    with open(filename, 'r') as f:
        f = f.readlines()
        for line in f:
            clients = line.split(',')
            client = clients[0]
            client = Client(client, clients[1], int(clients[2]), int(clients[3]), int(clients[4]))
            ret.append(client)
    return ret


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    ret = []
    for person in read_from_file_into_list(filename):
        if bank in person.bank:
            ret.append(person)
    return ret


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    ret = []
    people = read_from_file_into_list(filename)
    sorted_people = sorted(people, key=lambda p: p.account_age)
    sorted_people = sorted(sorted_people, key=lambda p: p.earnings_per_day(), reverse=True)
    for person in sorted_people:
        if Client.earnings_per_day(person) > 0:
            ret.append(person)
    if ret == []:
        return None
    else:
        return ret[0]


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    pass


if __name__ == '__main__':

    #print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]

    #print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]

    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh

    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
