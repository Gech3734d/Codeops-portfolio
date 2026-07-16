# variable declartion and data type
full_name = "Gizachew Dagnew "
age = 30
height = (1.65)
is_student = True
favorite_food = "Injera"
print(f"My name is {full_name}")
print(f"I am {age} years old and I am {height} meter")
print(f"am I a student ? {is_student}")
print(f"My favorite food is {favorite_food}")
 # Arithmetic Operation
num_one = int(input(" please enter the value of num_one :"))
num_two = int(input(" please enter the value of num_two :"))

sum = num_one + num_two
print(f"The sum of num-one and num_two is {sum}")
difference = num_one - num_two
print(f"The difference of num_one and num_two is {difference}")
multiplication = num_one * num_two
print(f"The multiplication of num_one and num_two is {multiplication}")
division =num_one / num_two
print(f" The division  of num_one and num_two is {division}")
module = num_one % num_two
print(f"The reminder of num_one % num_two is {module}")
floor_division = num_one // num_two
print(f" floor division of num_one and num_two is {floor_division}")

#    calculate year of birth accepting from user
birth_year = int(input("enter birth year :"))
current_year = 2026
age =current_year-birth_year
print(f" my age is {age}")
# checking score of student
score = int(input("enter the score of the student (0-100) :"))
if score >= 50:
    print("pass")
else:
    print("fail")
