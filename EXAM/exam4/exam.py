"""Exam 4 (2022-01-15)."""


def pairwise_max_letter(s: str) -> str:
    """
    Take higher letter from each pair of letters.

    The length of the input string is an even number.
    Take each pair and take only the higher of those two elements.
    "ab" => "b"
    "aa" => "a"
    "ax" => "x"
    There are only lower case latin letters (a-z) in input.

    Hint: you can compare elements: "z" > "a" (True), "a" > "b" (False)

    pairwise_max_letter("") => ""
    pairwise_max_letter("ab") => "b"
    pairwise_max_letter("abaa") => "ba"
    pairwise_max_letter("xaxy") => "xy"
    """
    ret = ''
    if s == '':
        return ''
    pairs = []
    pairs_amnt = int(len(s) / 2)
    for i in range(pairs_amnt):
        pair = s[0:2]
        pairs.append(pair)
        s = s.replace(pair, '', 1)

    for j in pairs:
        if j[0] > j[1]:
            ret += j[0]
        elif j[0] < j[1]:
            ret += j[1]
        elif j[0] == j[1]:
            ret += j[0]
    return ret


# print(pairwise_max_letter(""))  # ""
# print(pairwise_max_letter("ab"))  # "b"
# print(pairwise_max_letter("abaa"))  # "ba"
# print(pairwise_max_letter("xaxy"))  # "xy"
# print(pairwise_max_letter('xxxxxx'))


def remove_divisible_by_3(numbers: list):
    """
    Return list where numbers divisible by 3 are removed from the input list.

    remove_divisible_by_3([1, 2, 3]) => [1, 2]
    remove_divisible_by_3([3, 198, 3]) => []
    remove_divisible_by_3([0, 100]) => [100]
    remove_divisible_by_3([-1, -3]) => [-1]
    """
    ret = []
    for nr in numbers:
        if nr % 3 != 0:
            ret.append(nr)
    return ret


# print(remove_divisible_by_3([1, 2, 3]))  # [1, 2]
# print(remove_divisible_by_3([3, 198, 3]))  # []
# print(remove_divisible_by_3([0, 100]))  # [100]
# print(remove_divisible_by_3([-1, -3]))  # [-1]


def prettify_string(input_string: str) -> str:
    """
    Prettify string.

    - After every punctuation there should be at least one space.
    - Every sentence should start with an uppercase letter.

    Examples:
    "Hello,I am the input of this function.please make me pretty!" => "Hello, I am the input of this function. Please
    make me pretty!"
    "there should be space after me-and also space after me;next sentence should be capitalized! i need to be capitalized but
    no new space should be added." => "There should be space after me- and also space after me; next sentence should be capitalized! I need to be capitalized but
    no new space should be added."
    :return modified string
    """
    punctuation = {'.': '. ', ',': ', ', '!': '! ', '?': '? ', ':': ': ', ';': ';', '-': '- '}
    #  lauselõpumärk(.?!)
    # # kirjavahemärgid(',.!?:;-')
    # fixed_sentence = ''
    # sentence_end = ['?', '!', '.']
    # for s in range(len(input_string)):
    #     inp = input_string[s]
    #     if inp in punctuation:
    #         fixed_sentence += punctuation[inp]
    #     else:
    #         fixed_sentence += inp
    #

    result = ""
    add_space = False
    capitalize = True
    for c in input_string:
        if c in '!?.':
            capitalize = True
        if c in "!?.,;:-":
            add_space = True
        else:
            if add_space and c != ' ':
                result += " "
            add_space = False
            if capitalize and c != ' ':
                c = c.upper()
                capitalize = False

        result += c
    return result


# print(prettify_string('Hello,I am the input of this function.please make me pretty!'))


def max_average(data: list, n: int) -> float:
    """
    Find maximum average with window width of n.

    max_average([1, 2, 3], 2) = (2 + 3) / 2
      possible variants with window 2: [1, 2], [2, 3]
    max_average([1, 7, 4, 5, 6], 3) = (7 + 4 + 5) / 3 = 5.333333
      possible variants with window 2: [1, 7, 4], [7, 4, 5], [4, 5, 6]

    :param data - data with at least n + 1 elements.
    :param n - Window width. Amount of consecutive numbers to take into calculation.

    :return Maximum average achievable with current parameters.
    """
    ret = []
    end = n
    for i in range(len(data) - (n - 1)):
        s = data[i:end]
        ret.append(s)
        end += 1

    max_sum = -1000000000000
    for r in ret:
        if sum(r) > max_sum:
            max_sum = sum(r)
    return max_sum / n


# print(max_average([1, 2, 3, 1, 6, 5, 2, 3], 2))
# print(max_average([1, 7, 4, 5, 6], 3))


def find_parenthesis(s: str) -> str:
    """
    Find parenthesis.

    Given a string that contains a single pair of parenthesis,
    compute recursively a new string made of only of the parenthesis
    and their contents, so "xyz(abc)123" yields "(abc)".

    find_parenthesis("xyz(abc)123") => "(abc)"
    find_parenthesis("x(hello)") => "(hello)"
    find_parenthesis("(xy)1") => "(xy)"
    """
    if s[0] == '(' and s[-1] == ')':
        return s
    elif s[0] == '(' and s[-1] != ')':
        return find_parenthesis(s[0:-1])
    elif s[0] != '(' and s[-1] == ')':
        return find_parenthesis(s[1:])
    else:
        return find_parenthesis(s[1:-1])


# print(find_parenthesis("xyz(abc)123"))  # "(abc)"
# print(find_parenthesis("x(hello)"))  # "(hello)"
# print(find_parenthesis("(xy)1"))  # "(xy)"


def convert_to_roman(nr: int) -> str:
    """
    Convert a number into Roman number.

    The rules for Roman numbers:
    - I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.
    - Zero is not represented.
    - Numbers greater than 3,999 are not represented.
    - Roman numerals are repeated to add value: III is equivalent to 1 +1 +1 = 3.
    - Only powers of 10 may be repeated in this way. Thus, VV is invalid; 5 + 5 would instead be expressed as X.
    - No more than three repetitions of a numeral can be used. Five repetitions can be represented with a single, larger numeral;
    to represent four, use the next larger numeral, but precede it with a numeral to subtract from it.
    Thus, IIII is invalid and would instead be written as IV (one less than five).
    Likewise, XC represents 90 (10 less than 100), and XL represents 40 (10 less than 50).
    - A numeral used for subtraction in this way must be the largest power of 10 that is less than the numeral it precedes.
    Thus, XC is valid but IC is invalid.

    If the input number is not within the allowed range, return empty string "".

    convert_to_roman(1) => "I"
    convert_to_roman(55) => "LV"
    convert_to_roman(44) => "XLIV"
    convert_to_roman(2021) => MXXI
    convert_to_roman(1999) => MCMXCIX
    convert_to_roman(1009) => MIX

    """
    result = []
    amnts = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    ret = [1000, 500, 100, 50, 10, 5, 1]
    for i in ret:
        amnt = nr // i
        if amnt > 0:
            nr -= i
            result.append(amnts[i])

    return ''.join(result)


# print(convert_to_roman(1))  # "I"
# print(convert_to_roman(55))  # "LV"
#
# print(convert_to_roman(44))  # "XLIV"
# print(convert_to_roman(2021))  # MXXI
# print(convert_to_roman(1999))  # MCMXCIX
# print(convert_to_roman(1009))  # MIX


class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """
        Car class constructor.

        :param color: car color
        :param make: car make
        :param engine_size: car engine size
        """
        self.color = color
        self.make = make
        self.engine_size = engine_size

    def __repr__(self):
        """Representation for car."""
        return f'({self.make} {self.color})'


class Service:
    """Represent car service model."""

    def __init__(self, name: str, max_car_num: int):
        """
        Service class constructor.

        Car service should also have a database to keep and track all cars standing in queue for repair.
        :param name: service name
        :param max_car_num: max car number service can take for repair at one time
        """
        self.name = name
        self.max_car_num = max_car_num
        self.service_queue = []

    def can_add_to_service_queue(self, car: Car) -> bool:
        """
        Check if it possible to add car to service queue.

        Car can be added if:
        1. after adding new car, total car number in service does not exceed max_car_number (allowed car number in service)
        2. there is no car with the same color and make present in this service (yes, this world works this way).

        If car can be added, return True. Otherwise return False.
        """
        if self.service_queue == []:
            return True
        can_add = True
        for c in self.service_queue:
            if c.make == car.make and c.color == car.color:
                can_add = False
        if len(self.service_queue) + 1 <= self.max_car_num and can_add == True:
            return True
        else:
            return False

    def add_car_to_service_queue(self, car: Car):
        """
        Add car to service if it is possible.

        The function does not return anything.
        """
        if self.can_add_to_service_queue(car) is True:
            self.service_queue.append(car)

    def get_service_cars(self) -> list:
        """Get all cars is service."""
        return self.service_queue

    def repair(self) -> Car:
        """
        Repair car in service queue.

        Normally, the first car in queue is repaired.
        However, if there is a car in queue which color + make characters length is exactly 13 ->
        this car is chosen and is repaired (might be multiple suitable cars -> choose any).
        After the repair, car is no longer in queue (is removed).
        :return: chosen and repaired car
        """
        car_to_repair = self.service_queue[0]
        for car in self.service_queue:
            if len(car.color) + len(car.make) == 13:
                car_to_repair = car
                break

        self.service_queue.remove(car_to_repair)
        return car_to_repair

    def get_the_car_with_the_biggest_engine(self) -> list:
        """
        Return a list of cars (car) with the biggest engine size.

        :return: car (cars) with the biggest engine size
        """
        ret = []
        max_size = max(car.engine_size for car in self.service_queue)
        for c in self.service_queue:
            if c.engine_size == max_size:
                ret.append(c)
        return ret


class Plant:
    """The plants that the plant store sells and the plant collector can purchase."""

    def __init__(self, species: str, rarity: int, size: int):
        """
        Constructor.

        The price for the plant is taken from the table based on the size and rarity.
        """
        self.species = species
        self.rarity = rarity
        self.size = size

        self.price = 0

    def __repr__(self):
        """String representation of the plant, which is the species of the plant."""
        return self.species

    def update_rarity(self, rarity: int):
        """Update the rarity of the plant."""
        self.rarity = rarity


class PlantStore:
    """Plant store where the different plants are sold and the plant collectors can purchase from."""

    def __init__(self, name: str, pricing_coefficient: float):
        """Constructor."""
        self.pricing_coefficient = pricing_coefficient
        self.name = name
        self.stock = {}
        self.members_club = []
        self.members_only_stock = {}

    def update_stock(self, plant: Plant, amount: int):
        """
        Add plants and their amounts to the stock.

        If the plant is already in stock, adds new amount to current amount.
        """
        if plant not in self.stock:
            self.stock[plant] = amount
        else:
            self.stock[plant] += amount

    def update_members_only_stock(self, plant: Plant, amount: int):
        """
        Add plants and their amounts to the members only stock.

        If the plant is already in stock, adds new amount to current amount.
        """
        if plant not in self.members_only_stock:
            self.members_only_stock[plant] = amount
        else:
            self.members_only_stock[plant] += amount

    def sell_plant(self, plant: Plant, customer: 'PlantCollector'):
        """
        Sell the plant to the customer, removing one plant of that type from stock.

        It is important to note that plants that are in the members only stock are to be removed
        from that particular stock and are only sold to customers with a
        membership.
        """
        if customer in self.members_club:
            if plant in self.members_only_stock:
                self.members_only_stock.pop(plant)
        elif customer not in self.members_club:
            if plant in self.stock:
                self.stock.pop(plant)

    def get_members_only_stock(self):
        """Return the members only stock."""
        return self.members_only_stock

    def get_stock(self):
        """Return the stock available to all customers."""
        return self.stock

    def assign_membership(self, customer: 'PlantCollector'):
        """Add a customer to the members list."""
        if customer not in self.members_club:
            self.members_club.append(customer)

    def get_stock_value(self) -> int:
        """
        Calculate the sale value of the whole stock (both regular and members only stock).

        Multiply the prices and amounts of each plant and then also multiply everything
        by the store's pricing coefficient. Note that the members only stock plants
        do not need to be multiplied by the pricing coefficient, their price is already their sale price.
        """
        pass

    def is_in_stock(self, plant_name: str, customer: 'PlantCollector') -> bool:
        """
        Respond to a customer's query about whether a plant by that name (species) is in stock.

        It is important to note that if a plant is in members only stock and the customer is not a member,
        the plant is not 'in stock' for them, even if the store actually has the plant they are asking for.
        Returns the boolean True if the plant is in stock, and False if not.
        """

        # is_in_stock = False
        # for plant in self.members_only_stock:
        #     if plant.species == plant_name and customer not in self.members_club:
        #         is_in_stock = False
        #         return is_in_stock
        #     elif plant.species == plant_name and customer in self.members_club:
        #         is_in_stock = True
        #         return is_in_stock
        #
        #
        # for p in self.stock:
        #     if plant.species == plant_name and customer
        # return is_in_stock

    def get_plant_details(self, plant_name: str) -> Plant:
        """
        Return the full plant object by name (species).

        If no such plant exists in the store's stock, returns None.
        """
        plant = None
        get_plant = None
        for p in self.stock:
            if p.species == plant_name:
                plant = p
                get_plant = True

        if get_plant:
            return plant
        else:
            return None


class PlantCollector:
    """Plant collector who buys and collects plants."""

    def __init__(self, name: str):
        """Constructor."""
        self.name = name
        self.collection = []
        self.wishlist = []
        self.room = {}

    def add_to_collection(self, plant: Plant):
        """Add a plant to the collector's collection if not already there."""
        if plant not in self.collection:
            self.collection.append(plant)

    def add_to_wishlist(self, plant_name: str):
        """Add a plant's name to the collector's wishlist if not already there."""
        if plant_name not in self.wishlist:
            self.wishlist.append(plant_name)

    def remove_from_wishlist(self, plant_name: str):
        """Remove a plant name from the collector's wishlist."""
        if plant_name in self.wishlist:
            self.wishlist.remove(plant_name)

    def add_space(self, space_type: int, space_amount: int):
        """
        Add space to the collector's home.

        If there are no spaces of that size, create a new entry in the dict, otherwise
        add to the amount that already exists.
        """
        if space_type not in self.room:
            self.room[space_type] = space_amount
        else:
            self.room[space_type] += space_amount

    def calculate_collection_value(self):
        """
        Calculate the collector's plant collection value.

        Add the prices of all the plants together.
        """
        total = 0
        for plant in self.collection:
            total += plant.price

    def most_expensive_wishlist_plant(self, store: PlantStore):
        """
        Find the most expensive wishlist plant.

        As different stores have different prices (pricing coefficient can be
        different), a PlantStore object is also given as an argument to the function. Return the name of the most expensive
        plant or if none of the plants in the wishlist are in stock at the store, return None.
        """
        ret = []
        most_expensive = 0
        for wish_plant in self.wishlist:
            for plant in store.stock:
                if plant.species == wish_plant:
                    ret.append(plant)
                    break

        if ret != []:
            sorted_most_expensive = sorted(ret, key=lambda x: x.price, reverse=True)
            return sorted_most_expensive[0].species
        else:
            return None

    def buy_wishlist_plant(self, store: PlantStore) -> str:
        """
        Buy the plant that's both the most expensive and biggest one on their wishlist that they have space for.

        It's important to note that a store always carries only one size of any given plant,
        so if a plant is sold at the store, it is only available in that one size.
        If a plant is bought, it should be added to the collection, removed from wishlist and the store and also place it
        somewhere in the home of the collector, meaning a corresponding free space slot should be removed.
        If purchasing a plant was successful, this function returns the species of the plant, if not, returns the string
        "No wishlist plants are for sale in this store of fit in your home!"
        """
        pass

    def buy_plant(self, plant_name: str, store: PlantStore) -> str:
        """
        Buy the plant if it is possible.

        Buys the plant with the given name from the store if it is in stock. Add the plant to collection, remove from wishlist,
        remove from the stock of the store and amend the amount of space available in the home.
        If the purchase is successful, returns the species of the plant, if not, returns the string "Cannot buy this plant!"
        """
        for plant in store.stock:
            if plant.species == plant_name:
                p = plant
                self.collection.append(p)
                self.wishlist.remove(p)
                self.room[p.size] -= p.size


if __name__ == '__main__':
    # assert pairwise_max_letter("") == ""
    # assert pairwise_max_letter("abba") == "bb"
    #
    # assert remove_divisible_by_3([1, 2, 3]) == [1, 2]
    # assert remove_divisible_by_3([-3, 3]) == []
    #
    # assert prettify_string("Hello,I am the input of this function.please make me pretty!") \
    #        == "Hello, I am the input of this function. Please make me pretty!"
    #
    # assert max_average([1, 2, 3, 3], 2) == 3.0  # (3 + 3) / 2
    # assert max_average([1, 7, 2, 3, 3], 1) == 7.0
    # assert max_average([1, 7, 2, 3, 3], 3) == 4.0  # (7 + 2 + 3) / 3
    # assert max_average([8, 2, 9], 2) == 5.5  # (2 + 9) / 2
    #
    # assert find_parenthesis("a(b)c") == "(b)"
    # assert find_parenthesis("()") == "()"
    #
    # assert convert_to_roman(1) == "I"
    # assert convert_to_roman(44) == "XLIV"
    # assert convert_to_roman(55) == "LV"
    # assert convert_to_roman(444) == "CDXLIV"
    # assert convert_to_roman(1991) == "MCMXCI"
    # assert convert_to_roman(2021) == "MMXXI"
    # assert convert_to_roman(1009) == "MIX"
    #
    # Car service

    car = Car("blue", "honda", 1800)
    service = Service("autoLUX", 5)

    # print(service.can_add_to_service_queue(car))  # True
    # service.add_car_to_service_queue(car)
    # print(service.get_service_cars())  # [car]
    #
    # car2 = Car("blue", "hond", 1500)
    #
    # print(service.can_add_to_service_queue(
    #     car2))  # False; since there is already car in service with the same make and color
    # car3 = Car("red", "hoenda", 1600)
    # car5 = Car("reeed", "hoeeenda", 1600)
    # car6 = Car("reeed", "hoeeeeaa", 1600)
    # service.add_car_to_service_queue(car2)
    # service.add_car_to_service_queue(car3)

    # Plant store
    jungle_garden = PlantStore("Jungle Garden", 1.2)
    # assert jungle_garden.name == "Jungle Garden"
    # assert jungle_garden.pricing_coefficient == 1.2
    # assert jungle_garden.stock == {}
    # assert jungle_garden.members_club == []
    # assert jungle_garden.members_only_stock == {}

    lancifolia = Plant("Calathea Lancifolia", 0, 2)
    monstera_deliciosa = Plant("Monstera Deliciosa", 0, 0)
    micans = Plant("Philodendron Micans", 1, 1)
    jungle_garden.update_stock(lancifolia, 9)
    jungle_garden.update_stock(monstera_deliciosa, 3)
    jungle_garden.update_stock(micans, 8)

    ago = PlantCollector('ago')
    ago.add_to_wishlist('Calathea Lancifolia')
    ago.add_to_wishlist('Monstera Deliciosa')

    ago.most_expensive_wishlist_plant(jungle_garden)


    expected_stock = {
        micans: 8,
        lancifolia: 9,
        monstera_deliciosa: 3
    }
    assert jungle_garden.get_stock() == expected_stock
    assert jungle_garden.get_stock_value() == 774.0
