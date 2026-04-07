import csv
from datetime import datetime

import matplotlib.pyplot as plt


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    month = date[:7]

    total = 0

    # Calculate current total
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].startswith(month):
                    total += float(row[2])
    except FileNotFoundError:
        pass

    new_total = total + amount

    budget = get_budget(month)

    # Save expense
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print(f"Expense added. Total this month: {new_total}")

    #ALERT LOGIC
    if budget:
        if new_total > budget:
            print(" Budget exceeded! Stop spending!")
        elif new_total >= 0.8 * budget:
            print(" Warning: You are nearing your budget. Spend carefully!")
        else:
            print("You are within budget.")
    else:
        print("No budget set for this month.")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader =csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")

def monthly_summary():
    month=input("Enter mont (YYYY-MM): ")
    total=0

    with open("expenses.csv","r") as file:
        reader=csv.reader(file)
        print(reader)
        for row in reader:
            if(row[0].startswith(month)):
                total+=float(row[2])
    print(f"Total expenses for {month}: {total}")


def set_budget():
    month = input("Enter month (YYYY-MM): ")
    budget = float(input("Enter your monthly budget: "))

    with open("budget.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([month, budget])

    print("Budget saved successfully!")

def get_budget(month):
    try:
        with open("budget.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == month:
                    return float(row[1])
    except FileNotFoundError:
        return None

    return None

def category_analysis():
    data={}

    with open("expenses.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            category=row[1]
            amount=float(row[2])

            if category in data:
                data[category]+=amount
            else:
                data[category]=amount
    print("Category Analysis:")
    for category,total in data.items():
        print(f"{category}: {total}")

    max_category=max(data,key=data.get)
    print(f"Highest spending category: {max_category} with {data[max_category]}")

def show_pie_chart():
    data={}

    with open("expenses.csv", "r") as file:
        reader=csv.reader(file)
        for row in reader:
            category=row[1]
            amount=float(row[2])

            if category in data:
                data[category]+=amount
            else:
                data[category]=amount
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution ")
    plt.show()

def edit_expense():
    rows=[]

    try:
        with open("expenses.csv", "r") as file:
            reader=csv.reader(file)
            rows=list(reader)

            for i, row in enumerate(rows):
                print(f"{i}: {row}")

            index=int(input("enter the index to edit: "))

            if 0 <= index < len(rows):
                date=input("enter the date: ")
                category=input("Enter the new category: ")
                amount=input("Enter new amount : ")
                description=input("Enter new description: ")

                rows[index] = [date,category,amount,description]

                with open("expenses.csv", "w", newline="") as file:
                    writer=csv.writer(file)
                    writer.writerows(rows)
                print("Expense updated successfully!")
            else:
                print("Invalid index")
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")

def delete_expense():
    rows=[]

    try:
        with open("expenses.csv", "r") as file:
            reader=csv.reader(file)
            rows=list(reader)

        for i, row in enumerate(rows):
            print(f"{i}: {row}")

        index=int(input("Enter the index to delete: "))
        if 0 <= index < len(rows):
            rows.pop(index)

            with open("expenses.csv", "w", newline="") as file:
                writer=csv.writer(file)
                writer.writerows(rows)
            print("Expense deleted successfully!")
        else:
            print("Invalid index")
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")

def budget_alert():
    limit=float(input("Enter your monthly budget: "))
    month = input("Enter month (YYYY-MM):")

    total=0

    try:
        with open("expenses.csv", "r") as file:
            reader= csv.reader(file)
            for row in reader:
                if row[0].startswith(month):
                    total+=float(row[2])
        print(f"Total spent: {total}")

        if total > limit:
            print("Budget exceeded! Consider reducing your expenses.")
        else:
            print("You are within your budget.")
    except FileNotFoundError:
        print("No expenses found. Please add an expense first.")


def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis")
        print("5. Show Pie Chart")
        print("6. Edit Expense")
        print("7. Delete Expense")
        print("8. Budget Warning")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            show_pie_chart()
        elif choice == "6":
            edit_expense()
        elif choice == "7":
            delete_expense()
        elif choice == "8":
            budget_alert()
        elif choice == "9":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()