cities = ["addis ababa","bahir dar", "hawssa","addis ababa","bahir dar"]
unique_cities = set(cities)
for city in unique_cities:
     print(city)
print(len(unique_cities))

#  create dictionary of product with price

prices = { "burgger": 300,"meat": 1000,"shiro": 120,"fruit" : 200 }
for item, price in prices.items():
    print(f"{item}: {price} ETB")


    # list compreshension

prices = [100, 250, 400, 80]
with_tax = [p *0.15 for p in prices] 
print(with_tax)  
cheap = [p for p in prices if p < 200]
print(cheap) 
       
       # safe division
try:
     num1 = int(input("Enter the value of num1 :"))
     division = num1 / 1000
except ValueError:
      print("please insert valid number")
except ZeroDivisionError:
       print("number can not be zero")
else:
     print(division)
finally:
     print("Done")