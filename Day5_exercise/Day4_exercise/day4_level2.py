#  student class
class Student:
    def __init__(self, name, stud_id,):
        self.name =name
        self.stud_id =stud_id
        self.stu_grade = []
    def add_grade(self, grade):
            self.stu_grade.append(grade)

    def average_grade(self):
            if len(self.stu_grade) == 0:
                return 0
            return sum(self.stu_grade) / len(self.stu_grade)


stud1 = Student("abebe", "s101")
stud1.add_grade(67)
stud1.add_grade(87)
stud1.add_grade(65)
stud1.add_grade(85)
stud1.add_grade(90)
print("student name:",stud1.name)
print("student id :", stud1.stud_id)
print("student grade :",stud1.stu_grade)
print("average of student grade :",stud1.average_grade())
    #  product class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        #  sell product and reduce stock
    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"{quantity}   {self.name} sold successfully")
        else:
            print("not enough stock available")
            # add products to stock
    def restock(self, quantity):
        self.stock += quantity
        print(f"{quantity}  {self.name} added to stock")
        product1 = Product("computer", 500, 10)
        product1.sell(3)
        print("current stock:",product1.stock)

        product1.restock(5)
        print("current stock:",product1.stock)
        
        #   Encapsulation practice
class Account:
    
    def __init__(self, balance=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")


# Example usage
account = Account(1000)

print("Current balance:", account.balance)

account.deposit(500)
print("Balance after deposit:", account.balance)

account.withdraw(300)
print("Balance after withdrawal:", account.balance)

account.withdraw(1500)   # Insufficient balance
account.withdraw(-50)    # Invalid amount


            #   Full bank account with properties
class BankAccount:

    def __init__(self, balance=0):
        self.__balance = balance

    # Getter
    @property
    def balance(self):
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    # Transfer method
    def transfer(self, to_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds for transfer.")
        else:
            self.__balance -= amount
            to_account.deposit(amount)
            print(f"Transferred {amount} successfully.")


# Create bank accounts
account1 = BankAccount(1000)
account2 = BankAccount(500)

# Test deposit (add)
account1.deposit(200)

# Test withdraw (borrow)
account1.withdraw(300)

# Test transfer (return)
account1.transfer(account2, 400)

# Display final balances
print("Account 1 Balance:", account1.balance)
print("Account 2 Balance:", account2.balance)

          

                         
                        

  
            
                # Book class
class Book:
     
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True

    # Getters
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__available

    # Methods to change availability
    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
        print(f'"{book.title}" added to the library.')

    def borrow_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                if book.borrow():
                    print(f'You borrowed "{book.title}".')
                else:
                    print(f'"{book.title}" is not available.')
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                book.return_book()
                print(f'"{book.title}" has been returned.')
                return
        print("Book not found.")


# Create Book objects
book1 = Book("Python Programming", "John Smith", "101")
book2 = Book("Data Structures", "Jane Doe", "102")

# Create Library object
library = Library()

# Test add_book()
library.add_book(book1)
library.add_book(book2)

# Test borrow_book()
library.borrow_book("101")
library.borrow_book("101")  # Already borrowed

# Test return_book()
library.return_book("101")

# Borrow again after returning
library.borrow_book("101")

     
       


                              

                        


        
                  








        