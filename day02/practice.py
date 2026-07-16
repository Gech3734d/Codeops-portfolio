

# Accept the temprature in celsius for user to determine the label of temprature
tempreature=float(input("enter tepmpreature in b0C:"))
if tempreature < 15:
    print("cold")
elif 15 <= tempreature <= 28:
    print("warm")
else:
    print("hot")
# Display numbers 1 through 10 using range and for loop
for i in range(1,11):
    print(f"Reciept:#{i}")
    # Display even numbers 1 to 20
    even=1
    while even <= 20:
        if even % 2 == 0:
            print(f"{even} is  even number")
            even=even+1
            # write a disccount function to display disccount price
            def applye_discount(price,percent=10):
                return price-(price*percent /10)
                print(applye_discount(500))  

                print(applye_discount(500,30))
                # write a program to countdown 5 to 1
                count =5
                while count > 0:
                    print(count)
                    count=count-1
                    print("LIFTOFF")


