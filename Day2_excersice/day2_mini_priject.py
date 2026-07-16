# Personal Finance Tracker

balance = 0.0


def add_income():
    global balance
    try:
        income = float(input("Enter income amount: "))
        if income < 0:
            print("Income cannot be negative.")
        else:
            balance += income
            print("Income added successfully.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def add_expense():
    global balance
    try:
        expense = float(input("Enter expense amount: "))
        if expense < 0:
            print("Expense cannot be negative.")
        elif expense > balance:
            print("Insufficient balance!")
        else:
            balance -= expense
            print("Expense added successfully.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def show_balance():
    print(f"Current Balance: ${balance:.2f}")


while True:
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            add_income()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            show_balance()
        elif choice == 4:
            print("Thank you for using Personal Finance Tracker!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter a number.")