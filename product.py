import random
class Product:
    def __init__(self, name, price, description="", quantity=1):
        self.name = name
        self.price = price
        self.description = description
        self.sold = 0
        self.quantity = quantity
        self.id = self.set_id()

    def __str__(self):
        return (f"Product {self.id}: {self.name} at ${self.price} \n"
                f"{self.description}\n")

    @classmethod
    def set_id(cls) -> str:
        """Sets a random product id (7 digits), returns a string"""
        id = random.randint(1, 9999999)
        while id in Shop.products:
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
    products = {}    #id: obj
    def __init__(self, name, field="null"):
        self.name = name
        self.field = field
        self.products = {}
        self.products_sold = 0

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


if __name__ == "__main__":
    pencil = Product("Pencil", 1, quantity=100, description="A Cheap&Easy pencil.")
    book = Product("Book", 10, quantity=10, description="Our very own book documenting the history of our company.")
    bookstore = Shop("Bookstore")
    bookstore.add_product(pencil, book)
    bookstore.list_products()




