class Factory:
    def __init__(self):
        self.cakes = []

    def bake_cake(self, toppings: int, base: int) -> int:
        cake = Cake(base, toppings)
        self.cakes.append(cake)
        # basic_cake = 1
        # medium_cake = 2
        # large_cake = 5
        count = 0
        if toppings == 1:
            return 1
        if 1 < toppings < 5:
            if toppings % 2 == 0:
                self.cakes.append(cake)
                return toppings // 2

        if toppings >= 5:
            if toppings % 5 == 0:
                return toppings // 5

    def get_last_cakes(self, n: int) -> list:
        return self.cakes[-n:]

    def get_cakes_baked(self) -> list:
        return self.cakes

    def __str__(self):
        pass


class Cake:

    def __init__(self, base_amount, toppings_amount):
        pass
    @property
    def type(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


class WrongIngredientsAmountException(Exception):
    pass
