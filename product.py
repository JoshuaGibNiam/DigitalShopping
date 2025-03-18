import random
from seller import Seller
import json
class Product:
    products = {}
    def __init__(self, name, price, seller, description="", quantity=1):
        self.name = name
        self.price = price
        self.seller = seller #seller obj
        self.description = description
        self.sold = 0
        self.quantity = quantity
        self.id = self.set_id()
        Product.products[self.id] = self

    def __str__(self):
        return (f"Product {self.id}: {self.name} at ${self.price} \n"
                f"{self.description}\n")

    def pack(self):
        self.seller = self.seller.__dict__
        return self.__dict__

    def dump(self):
        self.pack()
        with open('files/products.json', 'w') as file:
            json.dump(self.pack(), file, indent=4)

    @classmethod
    def pack_all(cls):
        return {k: v.pack() for k, v in cls.products.items()}

    @classmethod
    def set_id(cls) -> str:
        """Sets a random product id (7 digits), returns a string"""
        id = random.randint(1, 9999999)
        while id in Product.products:
            id = random.randint(1, 9999999)
        return str(id)

    def restock(self, quantity: int) -> bool:
        """Adds a certain amount to the quantity"""
        if isinstance(quantity, int):
            self.quantity += quantity
            return True
        else:
            print("Quantity must be an integer! Action failed.")
            return False

    def sell(self, quantity=1) -> bool:
        if isinstance(quantity, int):
            self.sold += quantity
            self.quantity -= quantity
            return True
        else:
            print("Quantity must be an integer! Action failed.")
            return False

    def delete(self):
        self.name = "DELETED PRODUCT"
        self.price = 0
        self.description = "DELETED PRODUCT"
        self.quantity = 0

    def describe(self, desc: str):
        if isinstance(desc, str):
            self.description = desc
            return True
        else:
            print("Description must be an string! Action failed.")
            return False



class Shop:

    def __init__(self, name, field="null"):
        self.name = name
        self.field = field
        self.products = {} #id: obj
        self.products_sold = 0
        self.id = self.set_id()

    def pack(self):
        self.products = {k: v.__dict__ for k, v in self.products.items()}
        return self.__dict__



    @classmethod
    def set_id(cls) -> str:
        """Sets a random product id (7 digits), returns a string"""
        id = random.randint(1, 9999999)
        while id in Market.shops:
            id = random.randint(1, 9999999)
        return str(id)

    def add_product(self, *product):
        """Adds a product (pass Product obj as argument) to the shop"""
        for x in product:
            if isinstance(x, Product):
                self.products[x.id] = x
            else:
                print("Product type is not Product!")
                return False
        print("Action Successful.")
        return True

    def list_products(self):
        print(f"{self.name} sells: ")
        for v in self.products.values():
            print(f" - {v}")

class Market:
    """The whole online market."""
    shops = {} #id, obj

    def __init__(self):
        pass

    def pack(self):
        Market.shops = {k: v.__dict__ for k, v in Market.shops.items()}
        return Market.shops

    def add_shop(self, shop: Shop):
        if isinstance(shop, Shop):
            self.shops[shop.id] = shop
        else:
            print("Shop type is not Shop!")
            return False
        return True
    def load(self):
        self.pack()
        with open('products.json', 'w') as file:
            json.dump(self.shops, file, indent=4)
            file.close()


if __name__ == "__main__":
    seller1 = Seller("Joshy", "----", "019019019", "password123")
    pencil = Product("Pencil", 1, seller1, quantity=100, description="A Cheap&Easy pencil.")
    book = Product("Book", 10, seller1, quantity=10, description="Our very own book documenting the history of our company.")
    bookstore = Shop("Bookstore")
    bookstore.add_product(pencil, book)
    bookstore.list_products()

    bookstore.pack()
