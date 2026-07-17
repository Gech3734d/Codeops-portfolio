students = [ ("Abebe",90), ("Kebede",80), ("Aster", 65), ("Belay", 50), ("Meseret", 50)]
#  writing to the file
with open("students.txt", "w") as f:
    for name, score in students:
        f.write(f"{name}, {score}\n")
        print("student data has been written to students.txt")


        #  reading the file and calculate the average score


try:

    total = 0
    count = 0
    with open("students.txt", "r") as f:
     for line in f:
      name, score = line.strip().split(",")
      total += int(score)
      count +=1
      if count > 0:
       average = total / count
       print(f"Average score : {average}")
     else:
       print("the file is empty")
except FileNotFoundError:
     print("Error : students.txt does not exist")
          

        #   Error Handling
try:
   
   num1 = int(input("Enter the value of num1:"))
   num2 = int(input("Enter the value of num2 :"))
   Result = num1 / num2
except ValueError:
   print("The input value  to be number")
except ZeroDivisionError:
   print("The input can not be zero")
else:
   print("The Result of  num1 divide by num2 is :",Result)
finally:
   print("Calculation attempt completed")
     
    #  Inventory Manager
inventory = {}
def add_product():
   product = input("Enter product name :")
   if product in inventory:
      print("product already exist")
   else:
      try:
         quantity = int(input("Enter quantity:"))
         inventory[product] = quantity
         print("product added successfully")
      except ValueError:
         print("please enter a valid number")
def update_quantity():
   product = int(input("Enter product name"))
   if product in inventory:
     try:
        quantity =int(input("Enter new quantity"))
        inventory[product] = quantity
        print("Quantity updated successfully!")
     except ValueError:
            print("Please enter a valid number.")
     else:
        print("Product not found!")

def view_products():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\n--- Inventory ---")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")

def save_to_file():
    filename = "inventory.txt"

    try:
        with open(filename, "w") as file:
            for product, quantity in inventory.items():
                file.write(f"{product},{quantity}\n")
        print("Inventory saved successfully.")
    except Exception as e:
        print("Error saving file:", e)

def load_from_file():
    filename = "inventory.txt"

    try:
        with open(filename, "r") as file:
            inventory.clear()
            for line in file:
                product, quantity = line.strip().split(",")
                inventory[product] = int(quantity)
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error loading file:", e)

# Main Menu
while True:
    print("\n===== Inventory Manager =====")
    print("1. Add new product")
    print("2. Update quantity")
    print("3. View all products")
    print("4. Save to file")
    print("5. Load from file")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        view_products()
    elif choice == "4":
        save_to_file()
    elif choice == "5":
        load_from_file()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-6.")
   

