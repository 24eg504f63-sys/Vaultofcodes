import json
from datetime import datetime

# File name where expense data will be stored
FILE_NAME = "expenses.json"

# List to store all expenses
expenses = []

# Function to load expenses from file
def load_expenses():
    global expenses
    try:
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        # If file does not exist, start with empty list
        expenses = []

# Function to save expenses to file
def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Transport, etc.): ")

    # Date can be auto or user-defined
    choice = input("Use today's date? (y/n): ").lower()
    if choice == 'y':
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        date = input("Enter date (YYYY-MM-DD): ")

    # Store expense as dictionary
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

# Function to view summary
def view_summary():
    if not expenses:
        print("No expenses found.")
        return

    total_spending = 0
    category_summary = {}

    for expense in expenses:
        total_spending += expense["amount"]

        # Category-wise calculation
        if expense["category"] in category_summary:
            category_summary[expense["category"]] += expense["amount"]
        else:
            category_summary[expense["category"]] = expense["amount"]

    print("\n--- Expense Summary ---")
    print(f"Total Overall Spending: ₹{total_spending}")

    print("\nCategory-wise Spending:")
    for category, amount in category_summary.items():
        print(f"{category}: ₹{amount}")

# Function to view spending over time
    date_summary = {}

    for expense in expenses:
        if expense["date"] in date_summary:
            date_summary[expense["date"]] += expense["amount"]
        else:
            date_summary[expense["date"]] = expense["amount"]

    print("\n--- Spending Over Time ---")
    for date, amount in sorted(date_summary.items()):
        print(f"{date}: ₹{amount}")

# User Menu
def menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View Spending Over Time")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            spending_over_time()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Main Program Execution
load_expenses()   # Load data at start
menu()            # Show menu
