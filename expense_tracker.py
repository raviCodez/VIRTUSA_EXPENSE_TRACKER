import csv
from datetime import datetime

import matplotlib.pyplot as plt


def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category =input("Enter the category (Food, Travel,Bills): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")

    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

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

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis")
        print("5. Show Pie Chart")
        print("6. Exit")

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
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()