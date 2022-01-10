"""Santa."""

import csv
import json
import urllib.request
import urllib.error
from typing import Optional

API_URL = 'http://api.game-scheduler.com:8089/gift?'


class Product:
    """Product class."""

    def __init__(self, name: str, price: int, production_time: int, weight: int):
        """Product class constructor."""
        self.name = name
        self.price = price
        self.production_time = production_time
        self.weight = weight

    def __repr__(self):
        """Representation for Product."""
        return f'Product ({self.name}, {self.price}, {self.production_time}, {self.weight})'

    def get_name(self):
        """Get name."""
        return self.name

    def get_price(self):
        """Get price."""
        return self.price

    def get_production_time(self):
        """Get production time."""
        return self.production_time

    def get_weight(self):
        """Get weight."""
        return self.weight


class Warehouse:
    """Warehouse class."""

    def __init__(self):
        """Warehouse class constructor."""
        self.products = {}

    def get_product_from_factory(self, name: str) -> Optional[Product]:
        """Return product object from Warehouse."""
        qs = urllib.parse.urlencode({'name': name})
        try:
            with urllib.request.urlopen(API_URL + qs) as f:
                contents = f.read()
                print(contents.decode("utf-8"))

                # read json to python object
                data = json.loads(contents.decode('utf-8'))

                product = Product(data['gift'], data['material_cost'],
                                  data['production_time'], data['weight_in_grams'])

                if data['gift'] not in self.products:
                    self.products[data['gift']] = []
                self.products[data['gift']].append(product)

                return product
        except urllib.error.HTTPError:
            return None

    def get_product(self, name: str) -> Product:
        """Return product if it exists in products dict."""
        if name in self.products:
            return self.products[name]


class ChildrenList:
    """ChildrenList class."""

    def __init__(self):
        """Childrenlist class constructor."""
        self.children_dict = {}
        self.children = []
        self.wishes = {}
        self.nice = []
        self.naughty = []

    def read_wishes_from_file(self, filename):
        """Read children wishes from csv file into dict, where the key is the child and the value is list of wishes.

        Also check for child 'status' whether he/she is nice or naughty person and if neither then give 'normal' status.
        """
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                ret = []
                name = row[0]
                if len(row[1:]) > 5:
                    for g in row[1:6]:
                        gift = g.strip()
                        ret.append(gift)
                else:
                    for g in row[1:]:
                        gift = g.strip()
                        ret.append(gift)
                self.wishes[name] = ret

    def read_children_from_file(self, filename):
        """Read children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = Child(row[0], row[1].strip(), self.wishes[row[0]])
                self.children.append(child)
                self.children_dict[row[0]] = child

    def add_nice_children(self, children: list):
        """Add only nice children in nice_children list."""
        self.nice.extend(children)

    def add_naughty_children(self, children: list):
        """Add only naughty children in naughty_children list."""
        self.naughty.extend(children)

    def get_nice_children(self):
        """Get nice children list."""
        return self.nice

    def get_naughty_children(self):
        """Get naughty children list."""
        return self.naughty

    def get_children_list(self):
        """Getter for children."""
        return self.children

    def get_children_dict(self):
        """Getter for children dict: {name(str): name(obj)}."""
        return self.children_dict

    def get_wishes(self):
        """Getter for wishes dict: {name(str): wishes(list)}."""
        return self.wishes

    def country_of_origin(self, country: str) -> list:
        """Return list of people originated from same country."""
        ret = []
        for c in self.children:
            if c.country == country:
                ret.append(c)

        return ret


class Child:
    """Child class."""

    def __init__(self, name: str, country: str, wishlist: list):
        """Child class constructor."""
        self.name = name
        self.country = country
        self.wishlist = wishlist

    def __repr__(self):
        """Representation for child."""
        return f'{self.name}'

    def get_wishes(self):
        """Getter for child wishlist."""
        return self.wishlist


if __name__ == '__main__':
    warehouse = Warehouse()
    print(warehouse.get_product_from_factory('Zebra Jumpy'))
    print(warehouse.get_product('Zebra Jumpy'))

    # nice...
    nice_children = ChildrenList()
    nice_children.read_wishes_from_file('ex15_wish_list.csv')
    nice_children.read_children_from_file('ex15_nice_list.csv')
    print(nice_children.get_children_list())
    nice_children.add_nice_children(nice_children.get_children_list())
    print(nice_children.get_nice_children())

    c_origin1 = nice_children.country_of_origin('Estonia')
    nice_child1 = (nice_children.get_children_dict())
    # print(nice_child1)

    # naughty...
    naughty_children = ChildrenList()
    # naughty_children.read_wishes_from_file('ex15_wish_list.csv')
    # naughty_children.read_children_from_file('ex15_naughty_list.csv')
    # print(naughty_children.get_children_list())
    # naughty_children.add_naughty_children(naughty_children.get_children_list())
    # print(naughty_children.get_naughty_children())

    # naughty_child1 = (naughty_children.get_children_dict()['Tanya'])
    # print(naughty_child1)
