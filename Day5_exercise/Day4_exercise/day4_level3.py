           #   Full bank account with properties
class BankAccount:
    def __init__(self, owner, balance =0):
        self.owner =owner
        self.__balance = balance
        # Getter
        @property
        def balance(self):
            return self.__balance
        #   Setter
        @balance.setter
        def balance(self, amount):
            if amount >= 0:
                self.__balance = amount
            else:
                raise ValueError("balance can not be negative")
            #  Deposit money
        def deposit(self, amount):
                if amount >= 0:
                    self.__balance += amount
                    print(f"{amount} deposited successfully")
                else:
                    print("deposit must be positive")

                    # Withdraw money
                    def withdraw(self, amount):
                         if amount <= 0:
                          print("withdraw amount must be positive")
                         elif amount > self.__balance:
                          print("insufficient funds")
                         else:
                             self.__balance -= amount
                             print(f" {amount} withdraw successfully")


                            #  Transfer money
                             def transfer(self, to_account, amount):
                              if amount <= 0:
                                  print("transfer must be positive")
                              elif amount > self.__balance:
                                  print("insufficient funds for transfer")
                              else:
                                  self.__balance -= amount
                                  to_account.__balance += amount
                                  print(f"{amount} transferred to {to_account.owner} successfully")
                                     
                                    #  create BankAccount object
                account1 = BankAccount("chalie", 2300)
                account2 = BankAccount("Worku", 1000)
                #    test balance property
                print("chalie balance", account1.balance)
                print("worku balance :", account2.balance)

                         
                        

                            #  Test deposit
                account1.deposit(200)
                print("chalie balance :",account1.balance)
                    
                    # test withdraw
                account1.withdraw(230)
                print("chalie balance :",account1.balance)
                    #  Test 
                account1.transfer(account2, 200)
                print("Final chalie balance :", account1.balance)
                print("Final worku balance :", account2.balance)
            
                # Book class
                class Book:
                    def __init__(self, title, author, isbn):
                        self.__title = title
                        self.__author = author
                        self.__isbn = isbn
                        self.__available =True

                        # Getters
                        def get_title(self):
                            return self.__title
                        def get_isbn(self):
                         def get_author(self):
                            return self.__author
                            return self.__isbn
                        def get_available(self):
                            return self.available
                        #  Setter for availability
                        def set_available(self, status):
                            set_available =status
                            #  Library class
                            class Library:
                                def __init__(self):
                                    self__books = []
                                    # Add a book
                                    def add_book(self, book):
                                        self.__books.append(book)
                                        print(f"{book.get_title()}, added to the Library")
                                           
                                        #    Borrow a book
                                        def borrow_book(self,isbn):
                                            for book in self.__books:
                                                if book.get_isbn() == isbn:
                                                    if book.is_available():
                                                        book.set_available(False)
                                                        print(f'you borrowed "{book.get_title()}"')
                                                    else:
                                                        print("book is already borrowed ")
                                                        return 
                                                    print("book not found")
                                                    #  return  a book
                                                    def return_book(self, isbn):
                                                        for book in self.__books:
                                                            if book.get_isbn() == isbn:
                                                                if not book.is_available():
                                                                    book.set_available(True)
                                                                    print(f'you returned"{book.get_title}"')

                                                                else:
                                                                    print("book was not borrowed")
                                                                    return
                                                                print("book not found")
                                                                # Testing the classes
                                                                library = Library()
                                                                book1 = Book("python","java","html")
                                                                # add book
                                                                library.add_book(book1)
                                                                #  borrow book
                                                                library.borrow_book("ibsoo1")
                                                                #  return book
                                                                library.return_book("isboo1")
                                                                # try returning again
                                                                library.return_book("isboo1")

                              

class Car:
     def __init__(self, speed=0, fuel=100):
        self.__speed = speed
        self.__fuel = fuel

    # Getter and Setter for speed
        @property
        def speed(self):
         return self.__speed

        @speed.setter
        def speed(self, value):
         if value >= 0:
            self.__speed = value
         else:
            print("Speed cannot be negative.")

    # Getter and Setter for fuel
        @property
        def fuel(self):
          return self.__fuel

        @fuel.setter
        def fuel(self, value):
         if 0 <= value <= 100:
            self.__fuel = value
         else:
            print("Fuel must be between 0 and 100.")

def accelerate(self):
        if self.__fuel > 0:
            self.__speed += 10
            self.__fuel -= 5
            print("Car accelerated.")
        else:
            print("Not enough fuel!")

def brake(self):
        if self.__speed > 0:
            self.__speed -= 10
            if self.__speed < 0:
                self.__speed = 0
            print("Car slowed down.")
        else:
            print("Car is already stopped.")

def refuel(self, amount):
        if amount > 0:
            self.__fuel += amount
            if self.__fuel > 100:
                self.__fuel = 100
            print("Fuel added.")
        else:
            print("Invalid fuel amount.")


# Testing Car object
car1 = Car()

car1.accelerate()
print("Speed:", car1.speed)
print("Fuel:", car1.fuel)

car1.brake()
print("Speed:", car1.speed)

car1.refuel(20)
print("Fuel:", car1.fuel)


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def owner(self):
        return self.__owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def account_info(self):
        print("\nAccount Information")
        print("Account Number:", self.__account_number)
        print("Owner:", self.__owner)
        print("Balance:", self.__balance)


# Bonus: SavingsAccount inheritance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=5):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added.")


# Store accounts
accounts = {}


# Menu-driven program
while True:
    print("""
==== Addis Bank Account System ====
1. Create new account
2. Deposit
3. Withdraw
4. Check balance
5. View account info
6. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        acc_number = input("Enter account number: ")

        if acc_number in accounts:
            print("Account already exists.")
        else:
            name = input("Enter owner name: ")
            accounts[acc_number] = BankAccount(acc_number, name)
            print("Account created successfully.")

    elif choice == "2":
        acc_number = input("Enter account number: ")

        if acc_number in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[acc_number].deposit(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        acc_number = input("Enter account number: ")

        if acc_number in accounts:
            amount = float(input("Enter withdrawal amount: "))
            accounts[acc_number].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        acc_number = input("Enter account number: ")

        if acc_number in accounts:
            print("Balance:", accounts[acc_number].balance)
        else:
            print("Account not found.")

    elif choice == "5":
        acc_number = input("Enter account number: ")

        if acc_number in accounts:
            accounts[acc_number].account_info()
        else:
            print("Account not found.")

    elif choice == "6":
        print("Thank you for using Addis Bank.")
        break

    else:
        print("Invalid choice. Try again.")




        
                  
