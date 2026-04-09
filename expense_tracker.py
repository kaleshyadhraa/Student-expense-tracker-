import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: ₹"))
    date = input("Enter date (DD-MM-YYYY): ")

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['category']} | ₹{expense['amount']}")


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total}")


def category_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        summary[category] = summary.get(category, 0) + amount

    print("\n--- Category-wise Summary ---")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Student Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
