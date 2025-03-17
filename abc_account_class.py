from abc import ABC, abstractmethod
import random

from pywin.dialogs import status


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

    def __init__(self, name, email, phone, password):
        self.name = name
        self._email = email
        self._phone = phone
        self._cart = []
        self.__balance = 0
        self.__order_history = {}
        self.status = "unverified"
        self.id = Account.set_id()
        self.__password = password

        Account.accounts[self.id] = self
        self.verifyid = random.randint(1, 99999999)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @password.deleter
    def password(self):
        del self.__password

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

    def verify(self):  #this is rather obsolete
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        gmail_user = "anonymousgilbert44.gmail.com"
        gmail_password = "iamgilberttheking" #no steal i use new useless acc i cannot set up app password

        to_email = f"{self.email}"
        subject = "Account Verification"
        body = (f"This is concerning your account set-up. To successfully activate your account, \n"
                f"Please enter the following number into your console: \n"
                f"{self.verifyid}\n")


        msg = MIMEMultipart()
        msg["From"] = gmail_user
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, to_email, msg.as_string())
            server.quit()
            print("A verification email was sent successfully to your email. ")
            idtry = input("Please enter the verification number: ")
            if idtry == self.verifyid:
                print("Account will be now activated!")
                self.status = "active"
            else:
                print("Unsuccessful. Account will be deactivated.")
                self.status = "deactivated"
        except Exception as e:
            print("Failed to send email:", e)


    def overridestatus(self, status):
        if status == "deactivated":
            self.deactivate()
        elif status == "active":
            self.status = status
        elif status == "unverified":
            self.status = status
        else:
            self.status = "unverified"






