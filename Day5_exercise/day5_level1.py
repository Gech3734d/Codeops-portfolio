
# Parent class
class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# Child class: Car
class Car(Vehicle):
    def __init__(self, name, model, year, doors):
        super().__init__(name, model, year)
        self.doors = doors  # Unique attribute

    def open_trunk(self):  # Unique method
        print(f"The trunk of the {self.name} is now open.")


# Child class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, name, model, year, engine_type):
        super().__init__(name, model, year)
        self.engine_type = engine_type  # Unique attribute

    def do_wheelie(self):  # Unique method
        print(f"The {self.name} is doing a wheelie!")


# Example usage
car = Car("Toyota", "Corolla", 2023, 4)
bike = Motorcycle("Yamaha", "R1", 2022, "998cc")

print("Car Information:")
car.info()
print("Doors:", car.doors)
car.open_trunk()

print("\nMotorcycle Information:")
bike.info()
print("Engine Type:", bike.engine_type)
bike.do_wheelie()
                  


                  # Parent class
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")


# Child class
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest Added: ${interest:.2f}")


# Example usage
savings = SavingsAccount("SA101", "Alice", 1000, 5)

savings.display_balance()
savings.add_interest()
savings.display_balance()
                     

                     # Parent class
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")


# Child class
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest Added: ${interest:.2f}")


# Example usage
savings = SavingsAccount("SA101", "Alice", 1000, 5)

savings.display_balance()
savings.add_interest()
savings.display_balance()
                 



                       # Parent class
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def statement(self):
        print("----- Account Statement -----")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Balance: $", self.balance)


# Child class: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def statement(self):   # Overridden method
        super().statement()
        print("Interest Rate:", self.interest_rate, "%")


# Child class: CurrentAccount
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def statement(self):   # Overridden method
        super().statement()
        print("Overdraft Limit: $", self.overdraft_limit)


# Example usage
savings = SavingsAccount("SA101", "Alice", 1000, 5)
current = CurrentAccount("CA201", "Bob", 500, 1000)

print("Savings Account")
savings.statement()

print("\nCurrent Account")
current.statement()
              




                    # Parent class
class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def statement(self):
        print("----- Account Statement -----")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Balance: $", self.balance)


# Child class: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def statement(self):
        super().statement()
        print("Interest Rate:", self.interest_rate, "%")


# Child class: CurrentAccount
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def statement(self):
        super().statement()
        print("Overdraft Limit: $", self.overdraft_limit)


# Create objects
acc = Account("A101", "John", 1000)
sav = SavingsAccount("S101", "Alice", 2000, 5)
cur = CurrentAccount("C101", "Bob", 1500, 500)

# List containing all account types
accounts = [acc, sav, cur]

# Demonstrate polymorphism
for account in accounts:
    account.statement()
    account.deposit(100)
    print("New Balance: $", account.balance)
    print("-" * 30)
    from abc import ABC, abstractmethod

# Abstract Parent Class
class Account(ABC):
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def statement(self):
        print("----- Account Statement -----")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Balance: $", self.balance)

    @abstractmethod
    def calculate_interest(self):
        pass


# SavingsAccount Class
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

    def statement(self):
        super().statement()
        print("Interest Rate:", self.interest_rate, "%")


# CurrentAccount Class
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        return 0  # Current accounts do not earn interest

    def statement(self):
        super().statement()
        print("Overdraft Limit: $", self.overdraft_limit)


# Example usage
savings = SavingsAccount("SA101", "Alice", 1000, 5)
current = CurrentAccount("CA201", "Bob", 500, 1000)

savings.statement()
print("Interest:", savings.calculate_interest())

print()

current.statement()
print("Interest:", current.calculate_interest())


