#  person class 

class person:
  def __init__(self, name, age):
    self.Name = name
    self.Age = age
  def introduce(self):
   print(f"My name is  {self.Name} and I am {self.Age} Years Old")
   
person1 =person("Aelmaz",23)
person2 =person("Meseret", 34)
person1.introduce()
person2.introduce()
      #   Rectangle class
class Rectangle:
    def __init__(self, width, length):
        self.width =width
        self.length = length
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 *(self.width + self.length)
    
        print(f"Area of Rectangle is :{self.area}")
        print(f"Perimeter of Rectangle is : {self.Perimeter}")
rectangle1 = Rectangle(80,100)
rectangle2 = Rectangle(45, 32)

print("\n area and perimeter of rectangle1")
print(" area of rectangle is :",rectangle1.area())
print("Perimeter of rectangle is:",rectangle1.perimeter())
print(" area and perimeter of rectangle2")
print(" area of rectangle is :",rectangle2.area())
print("Perimeter of rectangle is:",rectangle2.perimeter())
         
        #  Account  class
class Account:
   def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance
   def deposit(self, amount): 
         self.balance += amount
         print(f"deposited amount : {amount}")
         print(f"updated balance: {self.balance} ")
   def withdraw(self, amount):
          if amount <= self.balance:
             self.balance -= amount 
             print(f"print current balance: {self.balance}")
          else:
             print("the is insufficient")
acc = Account("Meseret", 3000)
acc.deposit(2000)
acc.withdraw(500)
    
           