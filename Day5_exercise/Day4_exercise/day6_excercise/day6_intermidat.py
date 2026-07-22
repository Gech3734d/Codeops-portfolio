# The integration code of SRP and DIP
from abc import ABC, abstractmethod

# -----------------------------
# Notification Abstraction (DIP)
# -----------------------------
class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotifier(Notifier):
    def send_notification(self, message):
        print("Email:", message)


# -----------------------------
# Repository Abstraction (DIP)
# -----------------------------
class Repository(ABC):
    @abstractmethod
    def save(self, account):
        pass


class DatabaseRepository(Repository):
    def save(self, account):
        print(f"Account {account.account_number} saved to database.")


# -----------------------------
# Account Class (SRP)
# -----------------------------
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False


# -----------------------------
# Service Class
# -----------------------------
class AccountService:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def withdraw(self, account, amount):
        if account.withdraw(amount):
            self.repository.save(account)
            self.notifier.send_notification(
                f"Withdrawal of ${amount} successful."
            )
        else:
            print("Insufficient balance.")


# -----------------------------
# Example Usage
# -----------------------------
account = Account("A101", 1000)

repository = DatabaseRepository()
notifier = EmailNotifier()

service = AccountService(repository, notifier)

service.withdraw(account, 200)

print("Balance:", account.balance)

# Implementation of factory pattern
from abc import ABC, abstractmethod

# Abstract Class
class Account(ABC):
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance

    @abstractmethod
    def account_type(self):
        pass


# Savings Account
class SavingsAccount(Account):
    def __init__(self, owner, number, balance, interest_rate=5):
        super().__init__(owner, number, balance)
        self.interest_rate = interest_rate

    def account_type(self):
        return "Savings Account"


# Current Account
class CurrentAccount(Account):
    def __init__(self, owner, number, balance, overdraft_limit=1000):
        super().__init__(owner, number, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self):
        return "Current Account"


# Fixed Deposit Account
class FixedDepositAccount(SavingsAccount):
    def __init__(self, owner, number, balance, interest_rate=8):
        super().__init__(owner, number, balance, interest_rate)

    def account_type(self):
        return "Fixed Deposit Account"


# Factory Class
class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance):
        kind = kind.lower()

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        elif kind == "fixed":
            return FixedDepositAccount(owner, number, balance)

        else:
            raise ValueError("Invalid account type")


# Example Usage
acc1 = AccountFactory.create("savings", "Alice", "SA101", 1000)
acc2 = AccountFactory.create("current", "Bob", "CA201", 2000)
acc3 = AccountFactory.create("fixed", "Charlie", "FD301", 5000)

print(acc1.account_type())
print(acc2.account_type())
print(acc3.account_type())

# Implementation of Observer pattern
from abc import ABC, abstractmethod

# -----------------------------
# Observer Interface
# -----------------------------
class Observer(ABC):
    @abstractmethod
    def update(self, account_number, amount):
        pass


# SMS Observer
class SMSAlert(Observer):
    def update(self, account_number, amount):
        print(f"SMS Alert: Withdrawal of ${amount} from account {account_number}.")


# Audit Observer
class AuditLog(Observer):
    def update(self, account_number, amount):
        print(f"Audit Log: Large withdrawal of ${amount} recorded for account {account_number}.")


# -----------------------------
# Account Class (Subject)
# -----------------------------
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, amount):
        for observer in self.observers:
            observer.update(self.account_number, amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful.")

            # Notify observers if withdrawal is greater than 3000
            if amount > 3000:
                self.notify_observers(amount)
        else:
            print("Insufficient balance.")


# -----------------------------
# Example Usage
# -----------------------------
account = Account("A101", 10000)

# Register observers
account.add_observer(SMSAlert())
account.add_observer(AuditLog())

# Withdrawals
account.withdraw(1000)   # No notification
print()

account.withdraw(5000)   # Notifications sent

# Implementation of interface segregation principle

from abc import ABC, abstractmethod

# -----------------------------
# Base Account Class
# -----------------------------
class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")


# -----------------------------
# InterestBearing Interface
# -----------------------------
class InterestBearing(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def apply_interest(self):
        pass


# -----------------------------
# Savings Account
# -----------------------------
class SavingsAccount(Account, InterestBearing):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def apply_interest(self):
        self.balance += self.calculate_interest()


# -----------------------------
# Current Account
# -----------------------------
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit


# -----------------------------
# Example Usage
# -----------------------------
savings = SavingsAccount("SA101", "Alice", 1000, 5)
current = CurrentAccount("CA201", "Bob", 2000, 500)

print("Savings Balance:", savings.balance)
savings.apply_interest()
print("Balance After Interest:", savings.balance)

print("\nCurrent Balance:", current.balance)
current.deposit(500)
print("Balance After Deposit:", current.balance)

