#  Complete Refactoring of Account class using Five solid principles

from abc import ABC, abstractmethod

# =====================================
# Notification Interfaces (DIP + ISP)
# =====================================
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotifier(Notifier):
    def send(self, message):
        print("Email:", message)


class SMSNotifier(Notifier):
    def send(self, message):
        print("SMS:", message)


# =====================================
# Repository Interface (DIP)
# =====================================
class Repository(ABC):
    @abstractmethod
    def save(self, account):
        pass


class DatabaseRepository(Repository):
    def save(self, account):
        print(f"Account {account.account_number} saved to database.")


# =====================================
# Interest Interface (ISP)
# =====================================
class InterestBearing(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def apply_interest(self):
        pass


# =====================================
# Abstract Account Class (OCP)
# =====================================
class Account(ABC):
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @abstractmethod
    def statement(self):
        pass


# =====================================
# Savings Account
# =====================================
class SavingsAccount(Account, InterestBearing):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def apply_interest(self):
        self._balance += self.calculate_interest()

    def statement(self):
        print(f"Savings Account")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")


# =====================================
# Current Account
# =====================================
class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance, overdraft):
        super().__init__(account_number, owner, balance)
        self.overdraft = overdraft

    def statement(self):
        print(f"Current Account")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
        print(f"Overdraft: {self.overdraft}")


# =====================================
# Account Service (SRP)
# =====================================
class AccountService:
    def __init__(self, repository, notifier):
        self.repository = repository
        self.notifier = notifier

    def deposit(self, account, amount):
        account.deposit(amount)
        self.repository.save(account)
        self.notifier.send(f"${amount} deposited.")

    def withdraw(self, account, amount):
        if account.withdraw(amount):
            self.repository.save(account)
            self.notifier.send(f"${amount} withdrawn.")
        else:
            print("Insufficient balance.")


# =====================================
# Factory Pattern (OCP)
# =====================================
class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance):
        if kind.lower() == "savings":
            return SavingsAccount(number, owner, balance, 5)

        elif kind.lower() == "current":
            return CurrentAccount(number, owner, balance, 1000)

        else:
            raise ValueError("Invalid account type")


# =====================================
# Example
# =====================================
repository = DatabaseRepository()
notifier = EmailNotifier()

service = AccountService(repository, notifier)

acc1 = AccountFactory.create("savings", "Alice", "S101", 1000)
acc2 = AccountFactory.create("current", "Bob", "C101", 2000)

service.deposit(acc1, 500)
service.withdraw(acc2, 300)

acc1.apply_interest()

print()
acc1.statement()

print()
acc2.statement()
 
#   Refactor Code of  singleton + factory + Observer

from abc import ABC, abstractmethod

# =====================================
# Singleton Pattern
# =====================================
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BankConfig, cls).__new__(cls)
            cls._instance.savings_interest = 5
            cls._instance.fixed_interest = 8
        return cls._instance


# =====================================
# Observer Pattern
# =====================================
class Observer(ABC):
    @abstractmethod
    def update(self, account_number, amount):
        pass


class SMSAlert(Observer):
    def update(self, account_number, amount):
        print(f"SMS Alert: Large transaction of ${amount} on Account {account_number}")


class AuditLog(Observer):
    def update(self, account_number, amount):
        print(f"Audit Log: Transaction ${amount} recorded for Account {account_number}")


# =====================================
# Account Classes
# =====================================
class Account:
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, amount):
        for observer in self.observers:
            observer.update(self.number, amount)

    def deposit(self, amount):
        self.balance += amount

        if amount > 3000:
            self.notify(amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

            if amount > 3000:
                self.notify(amount)
        else:
            print("Insufficient balance.")

    def statement(self):
        print(f"\nOwner: {self.owner}")
        print(f"Account: {self.number}")
        print(f"Balance: ${self.balance}")


class SavingsAccount(Account):
    def __init__(self, owner, number, balance):
        super().__init__(owner, number, balance)
        self.interest_rate = BankConfig().savings_interest

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate / 100


class CurrentAccount(Account):
    def __init__(self, owner, number, balance):
        super().__init__(owner, number, balance)


class FixedDepositAccount(Account):
    def __init__(self, owner, number, balance):
        super().__init__(owner, number, balance)
        self.interest_rate = BankConfig().fixed_interest

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate / 100


# =====================================
# Factory Pattern
# =====================================
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


# =====================================
# Example Usage
# =====================================

# Create accounts using Factory
acc1 = AccountFactory.create("savings", "Alice", "S101", 10000)
acc2 = AccountFactory.create("current", "Bob", "C201", 5000)
acc3 = AccountFactory.create("fixed", "Charlie", "F301", 20000)

# Register observers
for acc in [acc1, acc2, acc3]:
    acc.add_observer(SMSAlert())
    acc.add_observer(AuditLog())

# Transactions
acc1.deposit(4000)      # Observer notified
acc2.withdraw(3500)     # Observer notified
acc3.apply_interest()

# Statements
acc1.statement()
acc2.statement()
acc3.statement()

# Refactoring Challenge
#  Create new Investment Class
# New account type
class InvestmentAccount(Account):
    def __init__(self, owner, number, balance, risk_level):
        super().__init__(owner, number, balance)
        self.risk_level = risk_level

    def calculate_return(self):
        # Example investment return calculation
        return self.balance * 0.10

    def statement(self):
        print("\n--- Investment Account ---")
        print("Owner:", self.owner)
        print("Account Number:", self.number)
        print("Balance:", self.balance)
        print("Risk Level:", self.risk_level)
#  Update The Factory

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

        elif kind == "investment":
            return InvestmentAccount(owner, number, balance, "Medium")

        else:
            raise ValueError("Invalid account type")
#  Create an Investment account using the factory

investment = AccountFactory.create(
    "investment",
    "David",
    "INV101",
    50000
)

investment.statement()

print("Expected Return:", investment.calculate_return())

# MiniProject:clean Addis Bank system

from abc import ABC, abstractmethod


# =====================================================
# Singleton Pattern: Bank Configuration
# =====================================================
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.savings_interest = 5
            cls._instance.overdraft_limit = 1000
        return cls._instance


# =====================================================
# Observer Pattern
# =====================================================
class Observer(ABC):

    @abstractmethod
    def update(self, account, amount):
        pass


class SMSAlert(Observer):
    def update(self, account, amount):
        print(
            f"SMS ALERT: Large withdrawal of ${amount} "
            f"from account {account.number}"
        )


class AuditLog(Observer):
    def update(self, account, amount):
        print(
            f"AUDIT LOG: Withdrawal ${amount} "
            f"recorded for {account.owner}"
        )


# =====================================================
# Notification Service (DIP)
# =====================================================
class NotificationManager:

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, account, amount):
        for observer in self.observers:
            observer.update(account, amount)


# =====================================================
# Abstract Account Class
# =====================================================
class Account(ABC):

    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    @abstractmethod
    def statement(self):
        pass

    def apply_interest(self):
        pass


# =====================================================
# Account Types
# =====================================================
class SavingsAccount(Account):

    def __init__(self, owner, number, balance):
        super().__init__(owner, number, balance)
        self.interest_rate = BankConfig().savings_interest

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self._balance += interest

    def statement(self):
        print("\n--- Savings Account ---")
        print("Owner:", self.owner)
        print("Number:", self.number)
        print("Balance:", self.balance)
        print("Interest:", self.interest_rate, "%")


class CurrentAccount(Account):

    def __init__(self, owner, number, balance):
        super().__init__(owner, number, balance)
        self.overdraft = BankConfig().overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self._balance -= amount
            return True
        return False

    def statement(self):
        print("\n--- Current Account ---")
        print("Owner:", self.owner)
        print("Number:", self.number)
        print("Balance:", self.balance)
        print("Overdraft:", self.overdraft)


# Bonus Feature
class InvestmentAccount(Account):

    def apply_interest(self):
        self._balance += self.balance * 0.10

    def statement(self):
        print("\n--- Investment Account ---")
        print("Owner:", self.owner)
        print("Number:", self.number)
        print("Balance:", self.balance)


# =====================================================
# Factory Pattern
# =====================================================
class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance):

        kind = kind.lower()

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        elif kind == "current":
            return CurrentAccount(owner, number, balance)

        elif kind == "investment":
            return InvestmentAccount(owner, number, balance)

        else:
            raise ValueError("Unknown account type")


# =====================================================
# Bank Service (Business Logic)
# =====================================================
class Bank:

    def __init__(self):
        self.accounts = []

        self.notifications = NotificationManager()
        self.notifications.add_observer(SMSAlert())
        self.notifications.add_observer(AuditLog)


    def add_account(self, account):
        self.accounts.append(account)


    def find_account(self, number):
        for account in self.accounts:
            if account.number == number:
                return account
        return None


    def withdraw(self, number, amount):

        account = self.find_account(number)

        if account:

            if account.withdraw(amount):

                print("Withdrawal successful.")

                if amount > 3000:
                    self.notifications.notify(account, amount)

            else:
                print("Withdrawal failed.")

        else:
            print("Account not found.")


    def apply_interest_all(self):

        for account in self.accounts:
            account.apply_interest()

        print("Interest applied.")


    def show_accounts(self):

        for account in self.accounts:
            account.statement()


# =====================================================
# Console Application
# =====================================================

bank = Bank()


while True:

    print("""
========= Addis Bank =========
1. Create Account
2. Deposit
3. Withdraw
4. Show All Accounts
5. Apply Interest
6. Exit
""")

    choice = input("Choose option: ")


    try:

        if choice == "1":

            kind = input(
                "Account type (savings/current/investment): "
            )

            owner = input("Owner name: ")
            number = input("Account number: ")
            balance = float(input("Initial balance: "))

            account = AccountFactory.create(
                kind,
                owner,
                number,
                balance
            )

            bank.add_account(account)

            print("Account created.")


        elif choice == "2":

            number = input("Account number: ")
            amount = float(input("Deposit amount: "))

            account = bank.find_account(number)

            if account and account.deposit(amount):
                print("Deposit successful.")
            else:
                print("Deposit failed.")


        elif choice == "3":

            number = input("Account number: ")
            amount = float(input("Withdrawal amount: "))

            bank.withdraw(number, amount)


        elif choice == "4":

            bank.show_accounts()


        elif choice == "5":

            bank.apply_interest_all()


        elif choice == "6":

            print("Goodbye!")
            break


        else:

            print("Invalid choice.")


    except ValueError:

        print("Please enter valid information.")
