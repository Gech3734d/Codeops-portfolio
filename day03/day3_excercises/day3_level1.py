# list and tuple training
favorite_food = ["Injera", "Bread","meat","fruit","potato","burger"]
print(favorite_food)
print("the first food is :",favorite_food[0])
print("The last food is :",favorite_food[-1])
favorite_food.append("milk")
favorite_food.pop(1)
print("updated food :", favorite_food)
#   create tuple of coordinates for ethiopia
Coordinates ={9.145, 40.4897}
#  unpack coordinates into two variables
latitude, longitude = Coordinates
print(latitude)
print(longitude)
 
#  create a dictionary student with key:value pairs
student = {"Name":"Abebe", "Age": 25, "Grade": "A", "City": "Adama", "Department": "SE"}
print(student["Name"], student["Department"], student["Grade"])
student["Phone"] = "0987654321"
student["Grade"] = "C"
print("Updated Dictionary:",student["Grade"])


#   print set item by creating duplicated list
Country = ["Ethiopia", "America", "Kenya", "Canada", "Kenya", "Ethiopia"]
Unique_country = set(Country)
print(Unique_country)
Unique_country.add("Nijeria")
print("updated set :",Unique_country)

