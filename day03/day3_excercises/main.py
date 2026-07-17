from Utils import add_tax
price = float(input("Enter the price"))
total_price = add_tax(price)
print("price including tax:", total_price)