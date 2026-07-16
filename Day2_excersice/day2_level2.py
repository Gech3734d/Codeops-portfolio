# calculate grade of student
score  = int(input("enter the score (0-100):"))
if 90 <= score <= 100:
    print("Excellent")
elif 80 <= score <= 89:
    print("Very good")
elif 70 <= score <= 79:
    print("Good")
elif 50 <= score <= 59:
    print("pass")
elif 0 <= score <= 50:
    print("fail")
else:
    print("The score is invalid")
# Number patterns
for y in range(1,21):
    
 if y % 2 != 0:
    print(f"The number {y} is Odd")
    if y % 5 == 0:
       print(f"the number {y} is divisible by 5")

    
    #    Display positive number acecept from user reach to zero
number = int(input(" enter the number (0 to stop)"))

sum =0
while True:
   if number == 0:
     break
     sum += number
     print(f"the sum {sum}")
# function practice
def greet(name):
   print(f"well come {name}")     
def square(number):
   return number * number

def is_even(number):
    return number % 2 == 0
greet("Abebe")
print(square(5))
print(is_even(64))
print(is_even(3))
   
       
       