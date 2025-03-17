from customer import Customer
from seller import Seller
from product import Product
import random
from datetime import datetime
class Order:
    @classmethod
    def set_id(cls) -> str:
        """Sets a random account id (1-9 digits), returns a string"""
        id = random.randint(1, 999999999)
        for k in Order.orders.keys():
            while Order.orders[k] == id:
                id = random.randint(1, 999999999)

        return str(id)

    orders = {} #id, obj
    def __init__(self, product: Product, customer: Customer, seller: Seller):
        self.product = product
        self.customer = customer
        self.seller = seller
        self.id = Order.set_id()
        current_datetime = datetime.now()
        self.time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        Order.orders[self.id] = self

    def __str__(self):
        return (f"Order {self.id}: Customer {self.customer.id}; Seller: {self.seller.id} \n"
                f"  Order for product {self.product.id} made at {self.time} .")

    def list_orders(self):
        for e, v in enumerate(Order.orders.values()):
            print(f"{e}: {v}")

#TODO: to save to json, create a convertto dict method in each classes and save to json.