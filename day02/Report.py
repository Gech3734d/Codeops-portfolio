customers=[ ("Alemitu",2500),("dessie",5000),("meseret",2000),("Aedisu",800),("Abebe",100)]
def tire(balance):
    if balance >= 1000:
        return "Permium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"
for name,balance in customers:
    print(f"{name}:{tire(balance)} ({balance}ETB)")
    # count each tire
    if tire(balance)== "Permium":
        permium_count +=1
    elif tire(balance) == "Standard":
        standard_count +=1
else:
    basic_count +=1
    print(f"permium:{permium_count}")
    print(f"standard:{standard_count}")
    print(f"basic:{basic_count}")