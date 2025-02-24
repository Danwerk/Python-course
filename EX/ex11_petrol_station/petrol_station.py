"""Petrol Station."""
import copy
from abc import ABC, abstractmethod
from datetime import date
from enum import Enum, auto


class ClientType(Enum):
    """
    Client type.

    Due to the fact that the client type is used in several places,
    it is more convenient if it is indicated by an object rather than a string.
    Status can be:

         1) basic (he is not a regular customer and he has no discounts)

         2) bronze customer (membership in the club starts with a discount of 0.025 euros for each liter of fuel and
         in the store
         5% for the goods received)

         3) silver customer (II level club membership, the conditions for receiving it is that the amount of purchases
         is 1000 euros,
         there is a discount on fuel in the amount of 0.05 euros and a 10% discount on goods in the store)

         4) gold customer (club membership level III, awarded for purchases of EUR 5,000,
         fuel discount is 0.1 euros and the store has a 15% discount on the entire product range)

         For levels II and III, they are thrown in bronze if the customer has not been active for 2 months
    """

    Basic = auto()
    Bronze = auto()
    Silver = auto()
    Gold = auto()


class OrderItem(ABC):
    """One line from bill."""

    def __init__(self, name: str, price: float):
        """
        Constructor (NB! Variables must be private).

        In case the price is negative, raise RuntimeError().
        """
        self.__name = name
        self.__price = price
        if self.__price < 0:
            raise RuntimeError('not okay')

    def get_name(self) -> str:
        """
        Return the item name.

        :return: str: name
        """
        return self.__name

    def get_price(self) -> float:
        """
        Return the price of the product.

        :return: float: price
        """
        return self.__price

    def get_total_price(self, client_type: ClientType, quantity: float = 1.0) -> float:
        """
        Return the price of the item.

        Returns the price of the goods from the given receipt line,
        taking into account the discount and the purchased quantity.

        :param client_type: the client type
        :param quantity: quantity of a product
        :return: float: total price
        """
        return quantity * (self.get_price() - self.get_discount(client_type))

    @abstractmethod
    def get_discount(self, client_type: ClientType) -> float:
        """
        Abstract because fuels and products have different uses for discounts.

        There is no need to write anything here.

        :param client_type
        :return: float: the discount
        """
        pass

    def __hash__(self):
        """Hash for using with dictionaries."""
        return hash((self.__name, self.__price))

    def __eq__(self, other):
        """Return True if OrderItems are equal, else - False."""
        if type(other) is type(self):
            return (self.__name == other.__name) and (self.__price == other.__price)
        else:
            return False

    def __repr__(self):
        """String representation for OrderItem."""
        return f'{self.__name}'


class ShopItem(OrderItem):
    """
    The product in the store.

    The product class in the store, which has a price, name and discount, calculated for 1 customer.
    """

    def __init__(self, name: str, price: float):
        """Constructor."""
        super().__init__(name, price)

    def get_discount(self, client_type: ClientType) -> float:
        """
        Discount for shop item.

        Abstract because fuels and products have different uses for discounts.
        (there is no need to write anything here)
        :param client_type
        :return: float: the discount
        """
        ret = 0
        if client_type == ClientType.Basic:
            ret = 0
        elif client_type == ClientType.Bronze:
            ret = 0.05
        elif client_type == ClientType.Silver:
            ret = 0.1
        elif client_type == ClientType.Gold:
            ret = 0.15
        return self.get_price() * ret


class Fuel(OrderItem):
    """
    The fuel.

    The fuel class, including price, name and discount, calculated for customers per liter.
    """

    def __init__(self, name: str, price: float):
        """Construtor."""
        super().__init__(name, price)

    def get_discount(self, client_type: ClientType) -> float:
        """
        Discount for fuel.

        Abstract because fuels and products have different uses for discounts.
        (there is no need to write anything here)
        :param client_type
        :return: float: the discount
        """
        ret = 0
        if client_type == ClientType.Basic:
            ret = 0
        elif client_type == ClientType.Bronze:
            ret = 0.025
        elif client_type == ClientType.Silver:
            ret = 0.05
        elif client_type == ClientType.Gold:
            ret = 0.1
        return ret


class Order:
    """Order with order items and date."""

    def __init__(self, items: dict[OrderItem, float], order_date: date, client_type: ClientType):
        """
        Constructor (NB! Variables must be private).

        In case the item quantity is negative, raise RuntimeError().

        : param items: dictionary where key is product / fuel and value is quantity
        : param order_date: date of purchase
        : param client_type: The type of client that made the purchase
        """
        self.__items = items
        self.__order_date = order_date
        self.__client_type = client_type

        for value in items.values():
            if value < 0:
                raise RuntimeError('not okay!')

    def get_date(self) -> date:
        """
        Return the date of purchase.

        :return: date
        """
        return self.__order_date

    def get_final_price(self) -> float:
        """
        Calculate the total cost of purchases.

        :return: float
        """
        ret = 0
        for key, val in self.__items.items():
            ret += key.get_total_price(self.__client_type, val)
        return ret

    def __hash__(self):
        """Hash for using with dictionaries."""
        return hash((self.__items, self.__order_date, self.__client_type))

    def __eq__(self, other):
        """Return True if Orders are equal, else - False."""
        if type(other) is not type(self):
            return False
        if not (self.__client_type == other.__client_type) or not (self.__order_date == other.__order_date) \
                or (len(self.__items) != len(other.__items)):
            return False

        return all(map(lambda x: x[0] == x[1], zip(self.__items, other.__items)))

    def __repr__(self):
        """String representation for Order."""
        return f"{', '.join(map(lambda item: item.get_name(), self.__items.keys()))}"


class Client:
    """Client itself."""

    def __init__(self, name: str, balance: float, client_type: ClientType):
        """
        Constructor (NB! Variables must be private).

        :param name: client name
        :param balance: customer money
        :param client_type: client type
        """
        self.__name = name
        self.__balance = balance
        self.__client_type = client_type

        self.__order_history = []

    def get_name(self):
        """Return client name."""
        return self.__name

    def get_client_type(self) -> ClientType:
        """
        Return the customer type.

        :return: ClientType
        """
        return self.__client_type

    def set_client_type(self, value: ClientType):
        """
        Set customer's status.

        :param value: ClientType
        """
        self.__client_type = value

    def get_balance(self) -> float:
        """
        Return the customer's money balance.

        :return: float
        """
        return self.__balance

    def get_history(self) -> list['Order']:
        """
        Return customer's purchase history.

        Returns our customer's purchase history as a copy of the purchase history
        Use deepcopy.So that changes made with the dictionary in the class do not affect the dictionary object that does not belong to the class.
        :return: list['Order']
        """
        return copy.deepcopy(self.__order_history)

    def clear_history(self):
        """Clear the purchase history."""
        self.__order_history.clear()

    def get_member_balance(self) -> float:
        """
        The sum of all purchases made by the member's history.

        :return: float: the sum
        """
        return sum(pur.get_final_price() for pur in self.__order_history)

    def buy(self, order: 'Order') -> bool:
        """
        Purchasing process.

        The purchase price is calculated.
        If the customer has enough money, a purchase will be made.
        The customer pays for the purchase and the purchase is added to the purchase history.
        If all succeeded will be returned True, otherwise False.
        :param order:
        :return: boolean
        """
        tot_price = order.get_final_price()
        if tot_price <= self.__balance:
            self.__balance -= tot_price
            self.__order_history.append(order)
            return True
        else:
            return False

    def __repr__(self):
        """String representation of the client."""
        return f"{self.__name} - {self.get_client_type().name} customer"


class PetrolStation:
    """Petrol Station with fuel and shop items."""

    def __init__(self, fuel_stock: dict[Fuel, float], shop_item_stock: dict[ShopItem, float]):
        """
        Constructor (NB! Variables must be private).

        Used the deepcopy.
        So that changes made with the dictionary in the class do not affect the dictionary object that does not belong
        to the class.
        :param fuel_stock: fuel tank
        :param shop_item_stock: products warehouse
        """
        self.__fuel_stock_copy = copy.deepcopy(fuel_stock)
        self.__shop_item_stock_copy = copy.deepcopy(shop_item_stock)
        self.__sell_history = {}

    def add_fuel(self, fuel: Fuel, quantity: float):
        """
        Add fuel to the tank.

        :param fuel:
        :param quantity:
        """
        if fuel in self.__fuel_stock_copy:
            self.__fuel_stock_copy[fuel] += quantity
        else:
            self.__fuel_stock_copy[fuel] = quantity

    def add_shop_item(self, item: ShopItem, quantity: float):
        """
        Add goods to the warehouse.

        :param item:
        :param quantity:
        """
        if item in self.__shop_item_stock_copy:
            self.__shop_item_stock_copy[item] += quantity
        else:
            self.__shop_item_stock_copy[item] = quantity

    def remove_fuel(self, fuel: Fuel, quantity: float):
        """
        Remove fuel.

        Fuel is dispensed from the tank, first it is checked whether
        it is possible to dispense as much fuel
        if so, then the quantity of the fuel in the tank is lowered,
        if not, the error RuntimeError() is thrown out.

        :param fuel:
        :param quantity:
        """
        if fuel not in self.__fuel_stock_copy:
            raise RuntimeError()
        if quantity > self.__fuel_stock_copy[fuel]:
            raise RuntimeError()
        else:
            self.__fuel_stock_copy[fuel] -= quantity

    def remove_items(self, item: ShopItem, quantity: float):
        """
        Remove items.

        The product is released from the warehouse, first it is checked whether it is possible to dispense as many products, if so,
        then the quantity of the product is lowered, if not, the error RuntimeError () is thrown out.
        :param item:
        :param quantity:
        """
        if item not in self.__shop_item_stock_copy:
            raise RuntimeError()
        if quantity > self.__shop_item_stock_copy[item]:
            raise RuntimeError("Not enough!")
        else:
            self.__shop_item_stock_copy[item] -= quantity

    def get_fuel_dict(self) -> dict[Fuel, float]:
        """Return dict with Fuel objects as keys and quantities as values."""
        return {key: value for key, value in self.__fuel_stock_copy.items() if isinstance(key, Fuel)}

    def get_shop_item_dict(self) -> dict[ShopItem, float]:
        """Return dict with ShopItem objects as keys and quantities as values."""
        return {key: value for key, value in self.__shop_item_stock_copy.items() if isinstance(key, ShopItem)}

    def get_sell_history(self) -> dict[Client, list[Order]]:
        """Return sell history dict where key is Client, value is a list of Orders."""
        return self.__sell_history

    def raise_exception_if_need(self, i):
        """Raise exeption if needed."""
        if isinstance(i[0], Fuel):
            if i[0] not in self.__fuel_stock_copy or self.__fuel_stock_copy[i[0]] < i[1]:
                raise RuntimeError('woops, not enough petrol or no such type of petrol')

        elif isinstance(i[0], ShopItem):
            if i[0] not in self.__shop_item_stock_copy or self.__shop_item_stock_copy[i[0]] < i[1]:
                raise RuntimeError('woops not enough items or no such type of item')

    def update_client_status(self, client):
        """Update client status if it is needed or possible."""
        if client.get_member_balance() > 1000:
            client.set_client_type(ClientType.Silver)
        if client.get_member_balance() > 6000:
            client.set_client_type(ClientType.Gold)

    def client_purchase_history(self, client, order):
        """Add client purchase info in history dict."""
        if client not in self.__sell_history:
            self.__sell_history[client] = [order]
        else:
            self.__sell_history[client].append(order)

    def add_items_to_dict(self, i, ret):
        """Add elements to dict, where the key is a name of element and value is quantity."""
        if i[0] not in ret:
            ret[i[0]] = i[1]
        else:
            ret[i[0]] += i[1]

    def sell(self, items_to_sell: list[tuple[OrderItem, float]], client: Client = None):
        """
        Sell item.

        If there are not enough items in the station, raise RuntimeError().
        In that case, the quantities of the items should not be changed.

        Use the parameter items_to_sell to create a Purchase Receipt Order
        (must be converted to tuple -> dict format), date put today's date.

        Then do the following with the client:

        Check if his loyalty status is valid.

        Check how much time this customer has had since the last purchase, if 2 months or more, the user will be downgraded to Bronze level and their purchase history will be cleared.

        If the customer is not a regular customer, it remains Basic

        An attempt is made to sell the purchase to the customer (through the purchase method), if this is successful, the purchase is transferred to the sales archive of the service station, the type of which is dict. The key is the customer and the valueon his purchase.

        If the purchase is successful, we will try to raise the level of the customer

        Check how much the user has spent and if he has spent enough to move to the next status, his status will change.

        :param items_to_sell: is the customer's purchase request, given in the form of a `tuple`,
        which contains the position (fuel or product) and the quantity (NB! the quantity is always a` float`,
        even if the number is a product)
        :param client: is a customer, but the customer can be specified as None,
        in which case a new customer must be created with `Basic` status and a sufficient amount of money to purchase
        """
        ret = {}
        for i in items_to_sell:
            self.raise_exception_if_need(i)
            self.add_items_to_dict(i, ret)  # add elements to dict

        total = 0
        for i in items_to_sell:
            total += i[1]
        client_downgrade = False

        if not client:
            client = Client('Incognito', total, ClientType.Basic)
        else:
            if len(client.get_history()) > 0:
                max_range_date = max(d.get_date() for d in client.get_history())
                # calculate number of days between two given dates
                date_interval = (date.today() - max_range_date).days
                if date_interval > 60:
                    client_downgrade = True
            else:
                client_downgrade = True

            if client_downgrade is True:
                client.set_client_type(ClientType.Bronze)
                client.clear_history()

        order = Order({i[0]: i[1] for i in items_to_sell}, date.today(), client.get_client_type())

        self.client_purchase_history(client, order)  # add client's purchase history in dictionary
        client.buy(order)  # make a purchase
        self.update_client_status(client)  # check whether client status is needed to update to silver or gold

        for item, quantity in ret.items():
            if type(item) == Fuel:
                self.remove_fuel(item, quantity)
            elif type(item) == ShopItem:
                self.remove_items(item, quantity)


if __name__ == '__main__':
    my_client = Client("keegi", 15666.15, ClientType.Bronze)

    my_petrol_station = PetrolStation({}, {})
    my_petrol_station.add_fuel(Fuel("fuelka", 5.5), 10.12)
    my_petrol_station.add_fuel(Fuel("fuelkaa", 5.5), 9000.21412)
    print(my_petrol_station.get_fuel_dict())
    my_petrol_station.add_shop_item(ShopItem("item", 4.123), 154.24)
    my_petrol_station.add_shop_item(ShopItem("item", 4.123), 32.5451)
    print(my_petrol_station.get_shop_item_dict())
    my_petrol_station.sell([(Fuel("fuelkaa", 5.5), 1900.1), (Fuel("fuelka", 5.5), 2.1)], my_client)
    my_petrol_station.sell([(ShopItem("item", 4.123), 43.24)], my_client)
    print(my_petrol_station.get_fuel_dict(), my_petrol_station.get_shop_item_dict(),
          my_petrol_station.get_sell_history())

    print(my_petrol_station.get_sell_history())
    print(my_client.get_history())
