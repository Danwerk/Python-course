import csv


class NaughtyChild:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return self.name


class NiceChild:
    def __init__(self, name: str, country):
        self.name = name
        self.country = country
        self.gifts = []

    def __repr__(self):
        return self.name

    def add_gifts(self, gift):
        self.gifts.append(gift)


class SantaWorkshop:
    """Santa class."""
    def __init__(self):
        self.nice_children = []
        self.naughty_children = []
        self.child_gifts = {}

    def read_nice_children_from_file(self, filename):
        """Read nice children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = NiceChild(row[0], row[1])
                self.nice_children.append(child)

    def get_nice_children(self):
        """Getter for nice children."""
        return self.nice_children

    def read_naughty_children_from_file(self, filename):
        """Read naughty children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = NaughtyChild(row[0], row[1])
                self.naughty_children.append(child)

    def get_naughty_children(self):
        """Getter for naughty children."""
        return self.naughty_children


if __name__ == '__main__':
    santa = SantaWorkshop()
    santa.read_nice_children_from_file('ex15_nice_list.csv')
    santa.read_naughty_children_from_file('ex15_naughty_list.csv')
    print(santa.get_nice_children())
    print(santa.get_naughty_children())