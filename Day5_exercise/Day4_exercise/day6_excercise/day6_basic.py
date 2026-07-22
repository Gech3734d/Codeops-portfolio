# before using single responsibility principle
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def save_to_file(self):
        with open("employees.txt", "a") as file:
            file.write(f"{self.name}, {self.calculate_salary()}\n")

    def send_email(self):
        print(f"Email sent to {self.name} about salary.")

        # after using single responsibility principle
        #  Employee class

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
#   salary calculator class
class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.hours_worked * employee.hourly_rate
  
#   Employee file manager class
class EmployeeFileManager:
    def save_to_file(self, employee, salary):
        with open("employees.txt", "a") as file:
            file.write(f"{employee.name}, {salary}\n")
# Email service class
class EmailService:
    def send_email(self, employee, salary):
        print(f"Email sent to {employee.name}.")
        print(f"Your salary is {salary}.")
# Create employee
employee = Employee("Abebe", 40, 250)

# Create helper objects
salary_calculator = SalaryCalculator()
file_manager = EmployeeFileManager()
email_service = EmailService()

# Calculate salary
salary = salary_calculator.calculate_salary(employee)

# Save to file
file_manager.save_to_file(employee, salary)

# Send email
email_service.send_email(employee, salary)

print("Salary:", salary)

#   Before using open/ closed principle

def calculate_bonus(employee_type):
    if employee_type == "Manager":
        return 5000
    elif employee_type == "Developer":
        return 3000
    elif employee_type == "Intern":
        return 1000
    else:
        return 0


# Testing
print("Manager Bonus:", calculate_bonus("Manager"))
print("Developer Bonus:", calculate_bonus("Developer"))
print("Intern Bonus:", calculate_bonus("Intern"))
    # After using open /closed principle

# Base class
class Employee:
    def calculate_bonus(self):
        return 0


# Manager class
class Manager(Employee):
    def calculate_bonus(self):
        return 5000


# Developer class
class Developer(Employee):
    def calculate_bonus(self):
        return 3000


# Intern class
class Intern(Employee):
    def calculate_bonus(self):
        return 1000


# Function remains unchanged
def show_bonus(employee):
    print("Bonus:", employee.calculate_bonus())


# Testing
manager = Manager()
developer = Developer()
intern = Intern()

show_bonus(manager)
show_bonus(developer)
show_bonus(intern)
 
#  Before using  Liskov substitution principle
class Bird:
    def fly(self):
        print("Bird is flying.")


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly!")


def make_bird_fly(bird):
    bird.fly()


sparrow = Bird()
penguin = Penguin()

make_bird_fly(sparrow)    # Works
make_bird_fly(penguin)    # Error!

# After using Liskov substitution principle

# Base class
class Bird:
    def eat(self):
        print("Bird is eating.")


# Flying Bird class
class FlyingBird(Bird):
    def fly(self):
        print("Flying bird is flying.")


# Sparrow can fly
class Sparrow(FlyingBird):
    pass


# Penguin cannot fly
class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming.")



# Function works only with birds that can fly
def make_bird_fly(bird):
    bird.fly()


# Testing
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)    # Works
penguin.swim()            # Works


# Checking The code  which principle violated

# class Account:
#     def __init__(self):
#         self.notifier =EmailNotifier()

#     def withdraw(self, amount):
#         ...
#         self.notifier.send_email(...)
#         self.save_to_db(...)
# #  Single responsibility principle Account class has more responsibility
# # Dependency Inversion principle Account class  depends Emailnotifier
# # open /closed principle 

