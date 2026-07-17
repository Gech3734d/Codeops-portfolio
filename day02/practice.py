

# Accept the temperature in celsius for user to determine the label of temprature
temperature=float(input("enter temperature in C:"))
if temperature < 15:
    print("cold")
elif 15 <= temperature <= 28:
    print("warm")
else:
    print("hot")
# Display numbers 1 through 10 using range and for loop
for i in range(1,11):
    print(f"Receipt:#{i}")
    # Display even numbers 1 to 20
    even=1
    while even <= 20:
        if even % 2 == 0:
            print(f"{even} is  even number")
            even=even+1
            # write a discount function to display discount price
            def apply_discount(price,percent=10):
                return price-(price*percent /10)
                print(apply_discount(500))  

                print(apply_discount(500,30))
                # write a program to countdown 5 to 1
                count =5
                while count > 0:
                    print(count)
                    count=count-1
                    print("LIFTOFF")


