print("================================= STUDENTS EXPENSE TRACKER ======================================================")

name = input("     Enter your name here:   ")
print("=======WELCOME,", name)

all_expenses = []
all_categories = []
all_descriptions = []

print("1. Add Expense")
print("2. View Expense")
print("3. Calculate total spending")
print("4. Find highest spending")
print("5. Exit")

while True:
    choice = int(input("Enter your choice here: "))

    if choice == 1:
        print("================= Add expenses =============")

        more_expenses_input = "yes"

        while more_expenses_input == "yes":
            expense_amount = int(input("     Enter your expense here:  "))

            category = input("   Enter category:  ")
            description = input("    Enter description:  ")

            all_expenses.append(expense_amount)
            all_categories.append(category)
            all_descriptions.append(description)

            more_expenses_input = input(
                "Do you have more expenses? (yes/no): "
            ).lower()

        print("Thank you for adding expenses.")

    elif choice == 2:
        print("View expenses")
        print("--- Your Expenses ---")

        for i in range(len(all_expenses)):
            print(
                f"Amount: {all_expenses[i]}, "
                f"Category: {all_categories[i]}, "
                f"Description: {all_descriptions[i]}"
            )

    elif choice == 3:
        print("Calculate total spending")

        total = 0

        if not all_expenses:
            print("No expenses to calculate total for yet.")
        else:
            for expense in all_expenses:
                total = total + expense

            print("Your total spending is:", "Rs", total)

    elif choice == 4:
        print("Find highest spending")

        if not all_expenses:
            print("No expenses to find highest spending for yet.")
        else:
            highest = 0

            for expense in all_expenses:
                if expense > highest:
                    highest = expense

            print("Your highest expense is:", "Rs", highest)

    elif choice == 5:
        print("==== Thank you for using Student Expense Tracker ====")
        print("=============================================================")
        print("=============================================================")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")