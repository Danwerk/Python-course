class Factory:
    def __init__(self):
        self.cakes = []

    def bake_cake(self, toppings: int, base: int) -> int:
        cake = Cake(base, toppings)
        self.cakes.append(cake)

    def get_last_cakes(self, n: int) -> list:
        return self.cakes

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
