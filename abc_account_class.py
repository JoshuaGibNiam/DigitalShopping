from abc import ABC, abstractmethod
import random
class Account(ABC):
    accounts = {} #id, obj

    @classmethod
    def set_id(cls) -> str:
        """Sets a random account id (6 digits), returns a string"""
        id = random.randint(1, 999999)
        for k in Account.accounts.keys():
            while Account.accounts[k] == id:
                id = random.randint(1, 999999)

        return str(id)

    def __init__(self, name, email, phone):
        self.name = name
        self._email = email
        self._phone = phone
        self._cart = []
        self.__balance = 0
        self.__order_history = {}
        self.status = "unverified"
        self.id = Account.set_id()

        Account.accounts[self.id] = self


    @property
    def email(self, email):
        self._email = email

    @email.getter
    def email(self):
        return self._email

    @email.deleter
    def email(self):
        self._email = None

    @property
    def phone(self, phone):
        self._phone = phone

    @phone.getter
    def phone(self):
        return self._phone

    @phone.deleter
    def phone(self):
        self._phone = None

    @property
    def balance(self, balance):
        self.__balance = balance

    @balance.getter
    def balance(self):
        return self.__balance

    @balance.deleter
    def balance(self):
        self.__balance = None

    def deactivate(self):
        self.status = "deactivated"
        del self.__order_history
        del self.__balance
        del self._email
        del self._phone
        del self.name
        del self._cart

    @abstractmethod
    def __str__(self):
        pass





