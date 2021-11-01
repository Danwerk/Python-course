"""Bake cakes."""


class Factory:
    """Describe Factory class."""

    def __init__(self):
        """List of cakes."""
        self.cakes = []

    def bake_cake(self, toppings: int, base: int) -> int:
        """Bake cakes and get right amount of cakes."""
        cake = Cake(base, toppings)
        self.cakes.append(cake)

        cakes_amnt = 0

        big_cake = toppings // 5
        big_cake_amnt = toppings % 5
        cakes_amnt += big_cake

        medium_cake = big_cake_amnt // 2
        medium_cake_amnt = big_cake_amnt % 2
        cakes_amnt += medium_cake

        small_cake = medium_cake_amnt // 1
        cakes_amnt += small_cake

        return cakes_amnt

    def get_last_cakes(self, n: int) -> list:
        """Get last cakes from cakes list."""
        return self.cakes[-n:]

    def get_cakes_baked(self) -> list:
        """Get cakes baked."""
        return self.cakes

    def __str__(self):
        """Return basic, medium or large."""
        pass


class Cake:
    """Describe Cake class."""

    def __init__(self, base_amount, toppings_amount):
        """Class for cake."""
        pass

    @property
    def type(self):
        """Type of cake."""
        pass

    def __repr__(self):
        """Cake cake cake."""
        pass

    def __eq__(self, other):
        """More cakes."""
        pass


class WrongIngredientsAmountException(Exception):
    """If error, then call out this class."""

    pass
