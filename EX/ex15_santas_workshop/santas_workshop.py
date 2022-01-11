"""Santa."""

import csv
import json
import urllib.request
import urllib.error
from typing import Optional
import math

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


class Logistics:
    """Logistics class"""

    def __init__(self, children: list):
        """Logistics constructor."""
        self.children = children
        self.carriages = {}
        self.product_objects = {}
        self.total_weight_amount_per_child = {}
        self.countries_and_children = {}

    def get_children(self):
        """Getter for children"""
        return self.children

    def children_from_countries_to_deliver(self):
        for c in self.children:
            if c.country not in self.countries_and_children:
                self.countries_and_children[c.country] = [c]
            else:
                self.countries_and_children[c.country].append(c)

    def get_children_from_countries_to_deliver(self):
        return self.countries_and_children

    def import_products_from_warehouse(self):
        for c in self.children:
            for i in c.wishlist:
                w = Warehouse()
                if i in self.product_objects:
                    continue
                else:
                    obj = w.get_product_from_factory(i)
                    self.product_objects[i] = obj

    def get_products(self):
        """Return products objects."""
        return self.product_objects

    def country_of_origin(self, country: str) -> list:
        """Return list of people originated from given country."""
        ret = []
        for c in self.children:
            if c.country == country:
                ret.append(c)

        return ret

    def get_products_total_volume(self) -> int:
        """Get total amount of products weight."""
        total = 0
        for p in self.product_objects:
            if p in self.product_objects and self.product_objects[p] is not None:
                total += self.product_objects[p].weight

        return total

    def products_total_volume_per_child(self, c: str) -> dict:
        """Return total amount of products weight per one child."""
        for country in self.countries_and_children:
            ret = {}
            for p in self.countries_and_children[country]:
                total = 0
                for w in p.wishlist:
                    total += self.product_objects[w].weight
                ret[p] = total
                self.total_weight_amount_per_child[country] = ret

        return self.total_weight_amount_per_child[c]

    def get_products_total_volume_per_child_per_country(self, country: str):
        return self.total_weight_amount_per_child[country]

    def amount_of_carriages_needed_to_carry_products_to_country(self, country) -> int:
        """Calculate the number of sleighs you need to carry all products to country."""
        total = 50000
        ret = math.ceil(sum(self.total_weight_amount_per_child[country].values()) / total)
        return ret

    def pack_carriages_to_country(self, country: str):
        """Pack carriages to given country according to max carriage load capacity(50000g)."""
        total = 50000
        total_w = self.products_total_volume_per_child(country)
        for i in range(self.amount_of_carriages_needed_to_carry_products_to_country(country)):
            ret = [(k, v) for k, v in total_w.items()]
            children_products_to_carry = {}
            amount = 0

            for c in range(len(ret)):
                if amount + ret[c][1] < total:
                    amount += ret[c][1]
                    children_products_to_carry[ret[c][0]] = ret[c][0].wishlist
                    del total_w[ret[c][0]]
                elif amount + ret[c][1] >= total:
                    carriage = Carriage(country, children_products_to_carry)

                    if country not in self.carriages:
                        self.carriages[country] = [carriage]
                    else:
                        self.carriages[country].append(carriage)

        carriage = Carriage(country, children_products_to_carry)
        if country not in self.carriages:
            self.carriages[country] = [carriage]
        else:
            self.carriages[country].append(carriage)

    def pack_all_carriages_to_countries(self):
        """Pack carriages for every country."""
        for country in self.get_children_from_countries_to_deliver():
            self.pack_carriages_to_country(country)

    def get_packed_carriages_to_countries(self) -> dict:
        """Get all packed carriages."""
        return self.carriages

    def delivery_notes_for_carriage_per_country(self, country: str):
        for i in self.carriages[country]:
            print(i.delivery_note())

    def delivery_notes_for_carriage_all(self):
        for k in self.carriages:
            for v in self.carriages[k]:
                print(v.delivery_note())


class Carriage:
    """Class carriage."""

    def __init__(self, country: str, products: dict):
        """Carriage class constructor."""
        self.country = country
        self.products = products

    def __repr__(self):
        """Representation for Carriage."""
        return f'{self.country}'

    def delivery_note(self):
        """Make the delivery notes ready."""
        santa = ''
        santa += r"""                        DELIVERY ORDER
                                                          _v
                                                     __* (__)
             ff     ff     ff     ff                {\/ (_(__).-.
      ff    <_\__, <_\__, <_\__, <_\__,      __,~~.(`>|-(___)/ ,_)
    o<_\__,  (_ ff ~(_ ff ~(_ ff ~(_ ff~~~~~@ )\/_;-"``     |
      (___)~~//<_\__, <_\__, <_\__, <_\__,    | \__________/|
      // >>     (___)~~(___)~~(___)~~(___)~~~~\\_/_______\_//
                // >>  // >>  // >>  // >>     `'---------'` """
        santa += '\n'

        santa += f"""\nFROM: NORTH POLE CHRISTMAS CHEER INCORPORATED
TO: /{self.country.upper()}/\n\n"""

        str_name = "Name"
        str_gifts = "Gifts"
        str_total_weight = "Total Weight(kg)"
        table = []
        max_name_len = 4
        max_gift_len = 5
        max_total_weight_len = 16
        name_len = max(len(child.name) for child in self.products)
        gift_len = max(len(', '.join(self.products[c])) for c in self.products)
        if name_len > max_name_len:
            max_name_len = name_len
        if gift_len > max_gift_len:
            max_gift_len = gift_len

        table.append('//' + '=' * (max_name_len + 2) + '[]' + '=' * (
                max_gift_len + 2) + '[]' + '=' * max_total_weight_len + '=' * 2 + f'\\\\' + '\n')
        table.append(f'|| {str_name:^{max_name_len}} || {str_gifts:^{max_gift_len}} || {str_total_weight:^2} ||\n')
        table.append('|]' + '=' * (max_name_len + 2) + '[]' + '=' * (
                max_gift_len + 2) + '[]' + '=' * max_total_weight_len + '=' * 2 + f'[|' + '\n')

        for c in self.products:
            table.append(f'|| {c.name:<{max_name_len}} || {", ".join(self.products[c]):<{max_gift_len}} || ... \n')

        table.append(f'\\\\' + '=' * (max_name_len + 2) + '[]' + '=' * (
                max_gift_len + 2) + '[]' + '=' * max_total_weight_len + '=' * 2 + f'//' + '\n')

        s = ''.join(table)
        santa += s
        return santa


if __name__ == '__main__':
    warehouse = Warehouse()
    # print(warehouse.get_product_from_factory('Zebra Jumpy'))
    # print(warehouse.get_product('Zebra Jumpy'))

    # nice...
    nice_children = ChildrenList()
    nice_children.read_wishes_from_file('ex15_wish_list.csv')
    nice_children.read_children_from_file('ex15_nice_list.csv')
    # print(nice_children.get_children_list())
    nice_children.add_nice_children(nice_children.get_children_list())
    # print(nice_children.get_nice_children())


    # naughty...
    naughty_children = ChildrenList()
    # naughty_children.read_wishes_from_file('ex15_wish_list.csv')
    # naughty_children.read_children_from_file('ex15_naughty_list.csv')
    # print(naughty_children.get_children_list())
    # naughty_children.add_naughty_children(naughty_children.get_children_list())
    # print(naughty_children.get_naughty_children())

    # naughty_child1 = (naughty_children.get_children_dict()['Tanya'])
    # print(naughty_child1)

    libby = Child("Libby", 'Germany', ['Zebra Jumpy', 'Princess dress', 'Lego death star'])
    keira = Child("Keira", 'Germany', ['LED light up sneakers', '7200 Riot Points gift card'])
    lexie = Child("Lexie", 'Tallinn',
                  ['Mermaid barbie', 'Pink fluffy pen', 'World of Warcraft: Shadowlands Collectors Edition'])

    amelia = Child("Amelia", 'Germany', ['Zebra Jumpy', 'Princess dress', 'Lego death star', 'LED light up sneakers',
                                         '7200 Riot Points gift card'])
    #
    # l2 = Logistics(nice_children.get_children_list())
    # print(l2.country_of_origin('Estonia'))

    l = Logistics(nice_children.get_nice_children())
    print(l.get_children())

    l.import_products_from_warehouse()

    print(l.country_of_origin("Germany"))  # check where person comes from.
    # print(l.get_products())
    # print(l.get_products_total_volume())
    # print(l.get_products_total_volume_per_child())

    # print(l.amount_of_carriages_needed_to_carry_products_to_country("Germany"))

    l.children_from_countries_to_deliver()
    print(l.get_children_from_countries_to_deliver())
    print(l.get_packed_carriages_to_countries())

    l.pack_all_carriages_to_countries()
    print(l.get_packed_carriages_to_countries())
    print(l.delivery_notes_for_carriage_per_country("Estonia"))
    # print(l.delivery_notes_for_carriage_all())

# make a list of countries to deliver
