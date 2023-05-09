"""
In this example, we will create a basic online marketplace with three classes: Product, Customer, and Marketplace.
The Product class will represent a product with a name, price, and quantity available.
The Customer class will represent a customer with a name, email, and balance. The Marketplace class will represent
the online marketplace itself and will contain a list of available products and a list of customers.
"""


class Product:
    """
    Represents a product with a name, price, and quantity available.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.quantity} available)"


class Customer:
    """
    Represents a customer with a name, email and balance
    """
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def __str__(self):
        return f"{self.name} ({self.email}) - ${self.balance}"


class Marketplace:
    """
    Represents an online marketplace with a list of available products and customers.
    """
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        """
        Add a product to the marketplace
        """
        self.products.append(product)

    def add_customer(self, customer):
        """
        Add a customer to the marketplace.
        """
        self.customers.append(customer)

    def buy_product(self, product_name, customer_name):
        """
        Buy a product from the marketplace
        """
        product = next((p for p in self.products if p.name == product_name and p.quantity > 0), None)
        customer = next((c for c in self.customers if c.name == customer_name and c.balance >= product.price), None)
        if product and customer:
            customer.balance -= product.price
            product.quantity -= 1
            print(f"{customer.name} bought {product.name}")
        else:
            print("Transaction failed")


# Create some products
p1 = Product("iPhone", 999, 10)
p2 = Product("MacBook", 1999, 5)
p3 = Product("Airpods", 199, 20)

# Create some customers
c1 = Customer("Ali", "ola@gmail.com", 3000)
c2 = Customer("Aijay", "aijay@gmail.com", 5000)

# Create the marketplace
m = Marketplace()

# Add the products and customers to the marketplace
m.add_product(p1)
m.add_product(p2)
m.add_product(p3)
m.add_customer(c1)
m.add_customer(c2)

# Buy some products
m.buy_product("iPhone", "Ali")
m.buy_product("iPhone", "Aijay")
m.buy_product("MacBook", "Ali")







