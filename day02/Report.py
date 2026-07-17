customers=[ ("Alemitu",300),("Dessie",1200),("meseret",850),("Aedisu",450),("Abebe",1500)]
def tire(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"
for name,balance in customers:
    print(f"{name}:{tire(balance)} ({balance}ETB)")
    # count each tire
    premium_count = 0
    standard_count = 0

    basic_count = 0
    if tire(balance)== "Premium":
       premium_count += 1
    elif tire(balance) == "Standard":
        standard_count += 1
else:
    basic_count += 1
    print(f"premium:{premium_count}")
    print(f"standard:{standard_count}")
    print(f"basic:{basic_count}")