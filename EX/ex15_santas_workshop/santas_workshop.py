"""Santa."""

import csv
import json
import urllib.request
import urllib.error
from typing import Optional
from urllib import parse

API_URL = 'http://api.game-scheduler.com:8089/gift?'


# class World:
#     def __init__(self):
#         self.nice_children = []
#         self.naughty_children = []
#         self.normal_children = []
#         self.wishlist_children = []
#
#     def add_nice_children(self, children: list):
#         self.nice_children.extend(children)
#
#     def add_naughty_children(self, children: list):
#         self.naughty_children.extend(children)
#
#     def get_nice_children(self):
#         return self.nice_children
#
#     def get_naughty_children(self):
#         return self.naughty_children


class Product:
    """Product class."""

    def __init__(self, name, price, production_time, weight):
        self.name = name
        self.price = price
        self.production_time = production_time
        self.weight = weight

    def __repr__(self):
        return f'Product ({self.name}, {self.weight})'


class Warehouse:
    def __init__(self):
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
        self.children_dict = {}
        self.children = []
        self.wishes = {}
        self.wishlist_children = []

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

    def read_children_from_file(self, filename):
        """Read children from csv file."""
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                child = Child(row[0], row[1].strip(), self.wishes[row[0]])
                self.children.append(child)
                self.children_dict[row[0]] = child

    def get_children_list(self):
        """Getter for nice children."""
        return self.children

    def get_children_dict(self):
        """Getter for children dict: {name(str): name(obj)}."""
        return self.children_dict

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
        return f'{self.name}'

    def get_wishes(self):
        """Getter for child wishlist."""
        return self.wishlist


if __name__ == '__main__':
    warehouse = Warehouse()
    print(warehouse.get_product_from_factory('Swimming flippers'))
    # print(warehouse.get_product('Swimming flippers'))

    # nice...
    nice_children = ChildrenList()
    nice_children.read_wishes_from_file('ex15_wish_list.csv')
    nice_children.read_children_from_file('ex15_nice_list.csv')
    print(nice_children.get_children_list())
    nice_child1 = (nice_children.get_children_dict()['Libby'])
    # print(nice_child1)

    # naughty...
    naughty_children = ChildrenList()
    naughty_children.read_wishes_from_file('ex15_wish_list.csv')
    naughty_children.read_children_from_file('ex15_naughty_list.csv')
    print(naughty_children.get_children_list())
    naughty_child1 = (naughty_children.get_children_dict()['Tanya'])
    # print(naughty_child1)

    # Nice, Naughty, Normal children together...
    world = World()
    world.add_nice_children(nice_children.get_children_list())
    world.add_naughty_children(naughty_children.get_children_list())
