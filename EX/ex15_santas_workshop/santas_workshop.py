"""Santa."""
import csv


class SantaWorkshop:
    """Santa workshop class."""

    def __init__(self):
        self.children = {}
        self.nice = []
        self.naughty = []
        self.wishes = {}

    def read_wishes_from_file(self, filename):
        """Read children wishes from csv file into dict, where the key is the child and the value is list of wishes.

        Also check for child 'status' whether he/she is nice or naughty person and if neither then give 'normal' status.
        """
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                ret = []
                name = row[0]
                for g in row[1:]:
                    gift = g.strip()
                    ret.append(gift)
                self.wishes[name] = ret

    def read_nice_children_from_file(self, filename):
        """Read nice children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = Child(row[0], row[1].strip(), self.wishes[row[0]])
                self.nice.append(child)
                self.children[row[0]] = child

    def read_naughty_children_from_file(self, filename):
        """Read naughty children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = Child(row[0], row[1].strip(), self.wishes[row[0]])
                self.naughty.append(child)
                self.children[row[0]] = child

    def get_nice_children(self):
        """Getter for nice children."""
        return self.nice

    def get_naughty_children(self):
        """Getter for naughty children."""
        return self.naughty

    def get_children(self):
        """Getter for children dict: {name(str): name(obj)}."""
        return self.children

    def get_wishes(self):
        """Getter for wishes dict: {name(str): wishes(list)}."""
        return self.wishes


class Child:
    """Child class."""

    def __init__(self, name: str, country: str, wishlist: list):
        self.name = name
        self.country = country
        self.wishlist = wishlist

    def __repr__(self):
        """Representation for child."""
        return self.name

    def get_wishes(self):
        """Getter for child wishlist."""
        return self.wishlist


class Product:
    """Product class."""
    pass


class ChildList:
    pass


'''

class ChristmasGift:
    """Gift class.

    Represents gifts, which every child would get.
    """

    def __init__(self, name):
        """Constructor for ChristmasGift."""
        self.name = name

    def __repr__(self):
        """Representation for ChristmasGift."""
        return self.name


class NaughtyChild:
    """Naughty child class.

    Represents naughty children, who should not get gifts for christmas.
    """

    def __init__(self, name, country):
        """Constructor for NaughtyChild."""
        self.name = name
        self.country = country

    def __repr__(self):
        """Representation for NaughtyChild."""
        return self.name


class NiceChild:
    """Nice child class.

    Represents nice children, who should get gifts for christmas.
    """

    def __init__(self, name: str, country):
        """Constructor for NiceChild."""
        self.name = name
        self.country = country
        self.gifts = []

    def __repr__(self):
        """Representation for NiceChild."""
        return self.name


class NormalChild:
    """Normal child class.

    Represents normal children, who may get gifts for christmas but not necessarily.
    """

    def __init__(self, name: str, country: str):
        """Constructor for NormalChild."""
        self.name = name
        self.country = country

    def __repr__(self):
        """Representation for NormalChild."""
        return self.name


class SantaWorkshop:
    """Santa class."""

    def __init__(self):
        """Constructor for Santa."""
        self.nice_children = []
        self.naughty_children = []
        self.normal_children = []  # normal children are children that don't belong to nice or naughty children
        self.children = {}  # but they are in Santa's wish list.
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
        """Read children wishes from csv file into dict, where the key is the child and the value is list of wishes.

        Also check for child 'status' whether he/she is nice or naughty person and if neither then give 'normal' status.
        """
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                ret = []
                name = row[0]
                if name not in self.children:
                    child = NormalChild(row[0], row[1])
                    self.normal_children.append(child)
                else:
                    for g in row[1:]:
                        gift = ChristmasGift(g.strip())
                        ret.append(gift)
                    self.children_gifts[self.children[row[0]]] = ret

    def get_children_wishes(self):
        """Getter for children gifts."""
        return self.children_gifts

'''
if __name__ == '__main__':
    santa = SantaWorkshop()
    santa.read_wishes_from_file('ex15_wish_list.csv')
    santa.read_nice_children_from_file('ex15_nice_list.csv')
    santa.read_naughty_children_from_file('ex15_naughty_list.csv')
    child = Child('Stacy', 'United Kingdom',
                  ['Polyhedral dice set', 'Wall-mount diamond pickaxe', '500 TikTok followers'])
    print(child.get_wishes())

    print(santa.get_nice_children())
    print(santa.get_naughty_children())
    print(santa.get_children())
    print(santa.get_wishes())
