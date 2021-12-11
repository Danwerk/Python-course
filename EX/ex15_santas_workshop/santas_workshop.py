import csv


class ChristmasGift:

    def __init__(self, name):
        """Constructor for ChristmasGift."""
        self.name = name

    def __repr__(self):
        """Representation for ChristmasGift."""
        return self.name


class NaughtyChild:
    """Constructor for NaughtyChild."""
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        """Representation for NaughtyChild."""
        return self.name


class NiceChild:
    def __init__(self, name: str, country):
        """Constructor for NiceChild."""
        self.name = name
        self.country = country
        self.gifts = []

    def __repr__(self):
        """Representation for NiceChild."""
        return self.name


class SantaWorkshop:
    """Santa class."""

    def __init__(self):
        """Constructor for Santa."""
        self.nice_children = []
        self.naughty_children = []
        self.children = {}
        self.gifts = {}
        self.children_gifts = {}  # dict where the key is a child and value is his/her wishes.

    def read_nice_children_from_file(self, filename):
        """Read nice children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = NiceChild(row[0], row[1])
                self.nice_children.append(child)
                self.children[row[0]] = child

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
                self.children[row[0]] = child

    def get_naughty_children(self):
        """Getter for naughty children."""
        return self.naughty_children

    def read_wishes_from_file(self, filename):
        """Read children wishes from csv file into dict, where the key is the child and the value is list of wishes."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                ret = []
                for g in row[1:]:
                    gift = ChristmasGift(g.strip())
                    ret.append(gift)
                self.children_gifts[self.children[row[0]]] = ret

    def get_children_wishes(self):
        """Getter for children gifts."""
        for k, v in self.children_gifts.items():
            return v
        return self.children_gifts


if __name__ == '__main__':
    santa = SantaWorkshop()
    santa.read_nice_children_from_file('ex15_nice_list.csv')
    santa.read_naughty_children_from_file('ex15_naughty_list.csv')
    santa.read_wishes_from_file('test_one_wish.csv')
    print(santa.get_nice_children())
    print(santa.get_naughty_children())
    print(santa.get_children_wishes())
    #print(santa.read_wishes_from_file('ex15_wish_list.csv'))
