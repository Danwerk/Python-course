"""Fruits delivery application."""


class Product:
    """Product class."""

    def __init__(self, name, price):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        """Representation for Product class."""
        return self.name


class Order:
    """Order class."""

    def __init__(self, customer=None):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.order_products = {}
        self.products_names = set()
        self.customer = customer

    def get_products(self):
        """Getter for products dictionary."""
        return self.order_products

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """
        str_list = []
        for key, value in self.order_products.items():
            str_list.append(f'{key}: {value} kg')
        converted_str = ', '.join(str_list)
        return converted_str

    def add_product(self, product):
        """Method for adding a single product to the dictionary."""
        if product[0] in self.order_products:
            self.order_products[product[0]] += product[1]
        else:
            self.order_products[product[0]] = product[1]

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        for product in products:
            self.add_product(product)

    def get_customer(self):
        """Getter for customer."""
        return self.customer


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.products = self.import_products('pricelist.txt')
        self.orders = []
        self.all_customers = []
        self.orders_dict = {}

        for obj in self.products:
            self.orders_dict[obj.name] = obj.price

        for customer in self.all_customers:
            for order in customer.get_orders():
                for key, val in order.order_products.items():
                    if key not in self.orders_dict:
                        raise RuntimeError('Woopsie. There is no such product as')

    def get_products(self) -> list:
        """Getter for products list."""
        return self.products

    def get_customers(self):
        """Getter for customers list."""
        return self.all_customers

    def get_orders(self) -> list:
        """Getter for orders list."""
        return self.orders

    def import_products(self, filename='pricelist.txt') -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        ret = []
        with open(filename, 'r') as f:
            f = f.readlines()
            for line in f:
                products = line.split(' - ')
                product = Product(products[0], float(products[1].replace('\n', '')))
                ret.append(product)
        return ret

    def order_products(self, products):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        Products here is list of tuples.
        """
        order = Order()
        if isinstance(products, tuple):
            order.add_product(products)
        elif isinstance(products, list):
            order.add_products(products)
        self.orders.append(order)

    def order(self, name: str, products: list):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        i = len(self.orders)
        for customer_name in self.all_customers:
            if customer_name.get_name() == name:
                self.order_products(products)
                customer_name.add_new_order(self.orders[i])

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.all_customers.append(customer)

    def add_customers(self, customers: list):
        """Method for adding several customers to the list."""
        for customer in customers:
            self.all_customers.append(customer)

    def show_all_orders(self, is_summary: bool) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        ret = []
        if is_summary is True:
            for customer in self.all_customers:
                ret.append(f'{str(customer)}:\n')  # append customer's name.
                if customer.order_is_empty():  # do this if order is empty.
                    ret.append('nothing\n')
                    ret.append(f"Total: {round(self.calculate_total(customer), 2):.2f}\n")
                    ret.append('\n')
                    continue
                else:  # here we add products
                    for order in customer.get_orders():
                        str_order = order.get_products_string()
                        ret.append(f'{str_order}\n')
                        continue
                #  and here we add the total sum of customer's orders.
                ret.append(f"Total: {round(self.calculate_total(customer), 2):.2f}\n")
                ret.append('\n')
            ret.pop()  # remove newline from the end.
            last_elem = ret[-1].replace('\n', '')
            ret.pop()
            ret.append(last_elem)

        elif is_summary is False:
            for customer in self.all_customers:
                ret.append(f"{str(customer)}:\n")
                if customer.order_is_empty():
                    ret.append('nothing\n')
                    ret.append('\n')
                    continue
                else:
                    for order in customer.get_orders():
                        str_order = order.get_products_string()
                        ret.append(f"{str_order}\n")
                        continue
                    ret.append('\n')

            ret.pop()
            last_elem = ret[-1].replace('\n', '')
            ret.pop()
            ret.append(last_elem)
        final_str = ''.join(ret)

        return final_str

    def calculate_total(self, customer) -> float:
        """Method for calculating total price for all customer's orders."""
        total = 0.00
        for order in customer.get_orders():
            for key, val in order.order_products.items():
                if key not in self.orders_dict:
                    total += 0.00
                else:
                    total += val * self.orders_dict[key]
        return total

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        total = 0.00
        for customer in self.all_customers:
            total += self.calculate_total(customer)
        return f"{self.show_all_orders(True)}\nALL ORDERS TOTAL: {total:.2f}"

    def find_product_by_name(self, name):
        """Method for finding product by its name."""
        for product in self.products:
            if product.name == name:
                return product


class Customer:
    """Customer to implement."""

    def __init__(self, name, address):
        """Customer constructor."""
        self.name = name
        self.address = address
        self.orders = []

    def __repr__(self):
        """Representation for Customer class."""
        return self.name

    def get_name(self):
        """Getter for name."""
        return self.name

    def get_address(self):
        """Getter for address."""
        return self.address

    def add_new_order(self, order):
        """Add new order to the orders list."""
        self.orders.append(order)

    def get_orders(self):
        """Getter for orders list."""
        return self.orders

    def order_is_empty(self) -> bool:
        """Return boolean value even the order is empty or not."""
        for order in self.orders:
            if len(order.order_products) != 0:
                return False
        return True


if __name__ == '__main__':
    app = App()
    # Adding default customers to our app.
    app.add_customers([Customer("Anton", "home"), Customer("Rubber Duck", "home-table"), Customer("Svetozar", "Dorm 1"),
                       Customer("Toivo", "Dorm 2"), Customer("Muhhamad", "Muhha's lair"), Customer("test", "TEST")])
    # Ordering some food for everyone.
    app.order("Anton", [("Avocado", 2), ("Orange", 1), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Anton", [("Avocado", 4), ("Orange", 2), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Rubber Duck", [("Mango Irwin", 6)])
    app.order("Svetozar", [("Lemon", 1)])
    app.order("Svetozar", [("Grapefruit", 10)])
    app.order("Muhhamad", [("Grenades", 13), ("Cannon", 1), ("Red pepper", 666)])
    app.order("Toivo", [("Granadilla", 3), ("Chestnut", 3), ("Pitaya(Dragon Fruit)", 3)])

    # Checking products dictionary format (we want numeric price, not string).
    print(app.get_products())

    print("=======")
    # Checking how all orders and summary look like.
    print(app.show_all_orders(False))
    print("=======")
    print(app.show_all_orders(True))
    print("=======")
    app.calculate_summary()
