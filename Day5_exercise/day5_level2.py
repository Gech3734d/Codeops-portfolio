from abc import ABC, abstractmethod

# Abstract Parent Class
class Account(ABC):
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance   # Protected attribute

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance.")

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
        return 0

    def statement(self):
        super().statement()
        print("Overdraft Limit: $", self.overdraft_limit)


# Example usage
savings = SavingsAccount("SA101", "Alice", 1000, 5)
current = CurrentAccount("CA201", "Bob", 500, 1000)

savings.deposit(200)
savings.statement()
print("Interest:", savings.calculate_interest())

print()

current.deposit(300)
current.statement()
print("Interest:", current.calculate_interest())
                          



from abc import ABC, abstractmethod

# ==========================
# Abstract Parent Class
# ==========================
class Account(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def statement(self):
        print("\n---------------------------")
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)

    @abstractmethod
    def calculate_interest(self):
        pass


# ==========================
# Savings Account
# ==========================
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def apply_interest(self):
        self._balance += self.calculate_interest()

    def statement(self):
        super().statement()
        print("Account Type: Savings")
        print("Interest Rate:", self.interest_rate, "%")


# ==========================
# Current Account
# ==========================
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self._balance -= amount
            print("Withdrawal successful.")
        else:
            print("Overdraft limit exceeded.")

    def calculate_interest(self):
        return 0

    def statement(self):
        super().statement()
        print("Account Type: Current")
        print("Overdraft Limit:", self.overdraft_limit)


# ==========================
# Bonus Class
# ==========================
class FixedDepositAccount(SavingsAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate, years):
        super().__init__(account_number, holder_name, balance, interest_rate)
        self.years = years

    def statement(self):
        super().statement()
        print("Account Type: Fixed Deposit")
        print("Duration:", self.years, "years")


# ==========================
# Bank System
# ==========================
accounts = []


def find_account(acc_no):
    for acc in accounts:
        if acc.account_number == acc_no:
            return acc
    return None


while True:
    print("\n====== Addis Bank System ======")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Show Statement")
    print("6. Apply Interest to Savings Accounts")
    print("7. Show All Accounts")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_no = input("Account Number: ")
        name = input("Holder Name: ")
        balance = float(input("Initial Balance: "))
        rate = float(input("Interest Rate (%): "))

        accounts.append(SavingsAccount(acc_no, name, balance, rate))
        print("Savings account created.")

    elif choice == "2":
        acc_no = input("Account Number: ")
        name = input("Holder Name: ")
        balance = float(input("Initial Balance: "))
        limit = float(input("Overdraft Limit: "))

        accounts.append(CurrentAccount(acc_no, name, balance, limit))
        print("Current account created.")

    elif choice == "3":
        acc_no = input("Account Number: ")
        acc = find_account(acc_no)

        if acc:
            amount = float(input("Deposit Amount: "))
            acc.deposit(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        acc_no = input("Account Number: ")
        acc = find_account(acc_no)

        if acc:
            amount = float(input("Withdraw Amount: "))
            acc.withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "5":
        acc_no = input("Account Number: ")
        acc = find_account(acc_no)

        if acc:
            acc.statement()
        else:
            print("Account not found.")

    elif choice == "6":
        for acc in accounts:
            if isinstance(acc, SavingsAccount):
                acc.apply_interest()
        print("Interest applied to all savings accounts.")

    elif choice == "7":
        if len(accounts) == 0:
            print("No accounts available.")
        else:
            for acc in accounts:
                acc.statement()

    elif choice == "8":
        print("Thank you for using Addis Bank System.")
        break

    else:
        print("Invalid choice.")
                  




    