from abc_account_class import Account


class Customer(Account):
    def __str__(self):
        return (f"Customer Account: {self.id} ({self.name}), "
                f"Status: {self.status}")




if __name__ == "__main__":
    t = Customer("Joshua Niam", "-", "019-729-0559",
                "randomrandomshit")

    t.verify()