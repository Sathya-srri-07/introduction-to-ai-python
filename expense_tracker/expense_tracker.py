# Expense Tracker

print("===== Expense Tracker =====")

expenses = []
total = 0

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        expenses.append([name, amount])
        total += amount

        print("Expense added successfully!")

    elif choice == "2":
        print("\n===== Expenses =====")

        if len(expenses) == 0:
            print("No expenses added.")
        else:
            for expense in expenses:
                print(expense[0], ":", expense[1])

    elif choice == "3":
        print("\nTotal Expense:", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
