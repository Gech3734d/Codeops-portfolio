# tip calculator
bill_amount =int(input("Enter the bill value :"))
tip_percentage = float(input("Enter the tip percentage(15,20,25):"))
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
# simple quiz game
def _question(question, answer):
    user_answer = input(question + "").strip().lower
    if user_answer == answer.lower():
        print("correct \n")
        return 1
    else:
        print("wrong \n")
        return 0
def show_result(score, total):
    print(f"your final score : {score} / {total}")
    if score == total:
        print("excellent score")
    elif score >= 3:
        print("good job  good knowledge")
    else:
        print("keeping practice better for next")
def main():
    score = 0
    score += _question("1, what is the capital city of amhara ?","b/dar")
    score += _question("2,how many month in a year  ?","12")

    score += _question("3,how  many days in a month?","30")

    score += _question("4,what is the capital city of assosa ?","b/dar")

    score += _question("5,  what is 78 - 34 ?","28")
    
    show_result(score , 5)
main()
# create function to calculate tax and discount
def calculate_final_price(price, tax_rate=0.15,discount=0):
    discount_price = price - discount
    tax = discount_price * tax_rate
    final_price = discount_price + tax
    return final_price
print(calculate_final_price(100))
print(calculate_final_price(100, tax_rate=0.10))

print(calculate_final_price(100, discount=10))
print(calculate_final_price(300, 0.06,20))



