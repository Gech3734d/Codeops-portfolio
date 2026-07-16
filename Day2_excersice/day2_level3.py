# tip calculator
bill_amount =int(input("Enter the bill value :"))
tip_percentage = float(input("Enter the tip percentage(20,25,30):"))
payers = int(input("Enter the number of people spliting the bill :"))
# calculate tip_amount
tip_amount = bill_amount * (tip_percentage / 100)
# calculate total amount
total_amount = bill_amount + tip_amount
# calculate amount of each person pays
amount_per_person = total_amount / payers
print(f"bill amount :{bill_amount}")
print(f"Tip amount :{tip_amount}")
print(f"Total amount :{total_amount}")
print(f"Each person pays :{amount_per_person}")

