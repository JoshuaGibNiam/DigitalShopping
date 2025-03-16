from abc_account_class import Account

class Seller(Account):
    def __str__(self):
        return f"Seller Account {self.id}: {self.name}, status: {self.status}"