#  list operation
Numbers = [10,25,40,15,60, 30]
for y in Numbers:
    if y > 30:
     print(y)
Numbers.sort()
print(Numbers)
#  sum and average operation of list
Total = sum(Numbers)
Average = Total /len(Numbers)
print("\n sum =",Total)
print("average =", Average)
#  Dictionary operation
Products = {"soap":80, "shoes":3000, "sugar": 200, "coffe": 1000, "fruit": 50}
for prod, price in Products.items():
   print(f"The result is: {prod} :{price}")
   product_name = input("Enter product name:")
   price = Products.get(product_name, "product not found")
   print(f"price of {product_name}:{price}")
        #  List comprenhensive
numbers = [y for y in range(0,21)]
print(numbers)
even_numbers =[new_list for new_list in range(0, 31) if new_list % 2 ==0]
print(even_numbers)

odd_numbers =[odd_num for odd_num in range(0,11)if odd_num % 2 != 0]
print(odd_numbers)

   