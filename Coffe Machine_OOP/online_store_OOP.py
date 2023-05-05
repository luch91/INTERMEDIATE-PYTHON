# Online store example

"""
class Product:
    def __init__(self, name, price, number=0):
        self.name = name
        self.price = price
        self.number = number


class Cart:
    def __init__(self, number):
        self.number = number
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    @property
    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price * self.number


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def remove_from_cart(self, item):
        self.cart.remove_item(item)

    def view_cart(self):
        for item in self.cart.items:
            print(f"{item.name}: ${item.price}")

    def checkout(self):
        total_price = self.cart.get_total_price
        print(f"Total price: ${total_price}. Thank you for shopping with us.")
        self.cart = Cart()


product1 = Product("Shirt", 20, 7)
product2 = Product("Pants", 30, 15)

customer1 = Customer("Alice")
customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer1.view_cart()

customer1.checkout()
"""


class Product:
    """
    Represents a product with a name, price, and an optional number.
    """
    def __init__(self, name, price, number=0):
        self.name = name
        self.price = price
        self.number = number


class Cart:
    """
    Represents a shopping cart with a number and a list of items.
    """
    def __init__(self, number=0):
        """
        Initializes a new Cart object.

        Args:
            number (int): The number of products in the cart.
        """
        self.number = number
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the cart.

        Args:
            item (Product): The product to add to the cart.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the cart.

        Args:
            item (Product): The product to remove from the cart.
        """
        self.items.remove(item)

    @property
    def num_products(self):
        """
        Calculates and returns the total number of products in the cart.

        Returns:
            int: The total number of products in the cart.
        """
        total_products = 0
        for item in self.items:
            total_products += item.number
        return total_products

    @property
    def get_total_price(self):
        """
        Calculates and returns the total price of all the items in the cart, multiplied by the number of products.

        Returns:
            float: The total price of all the items in the cart, multiplied by the number of products.
        """
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price * self.num_products


class Customer:
    """
    Represents a customer with a name and a cart.
    """
    def __init__(self, name):
        """
        Initializes a new Customer object.

        Args:
            name (str): The name of the customer.
        """
        self.name = name
        self.cart = Cart(number=1)

    def add_to_cart(self, item):
        """
        Adds an item to the customer's cart.

        Args:
            item (Product): The product to add to the cart.
        """
        self.cart.add_item(item)

    def remove_from_cart(self, item):
        """
        Removes an item from the customer's cart.

        Args:
            item (Product): The product to remove from the cart.
        """
        self.cart.remove_item(item)

    def view_cart(self):
        """
        Prints out the items in the customer's cart.
        """
        for item in self.cart.items:
            print(f"{item.name}: ${item.price}")

    def checkout(self):
        """
        Calculates and prints the total price of the items in the customer's cart, multiplied by the number of products.
        """
        total_price = self.cart.get_total_price
        print(f"Total price: ${total_price}. Thank you for shopping with us.")
        self.cart = Cart(number=1)


product1 = Product("Shirt", 20, 7)
product2 = Product("Pants", 30, 15)

customer1 = Customer("Alice")
customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer1.view_cart()

customer1.checkout()
