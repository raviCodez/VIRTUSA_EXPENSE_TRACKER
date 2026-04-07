import streamlit as st
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import os

FILE = "expenses.csv"

# Ensure file exists
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        pass

# Load data
def load_data():
    data = []
    with open(FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                data.append(row)
    return data

# Save data
def save_data(data):
    with open(FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# UI Title
st.title(" Smart Expense Tracker")

# Sidebar menu
menu = st.sidebar.selectbox("Choose Option", [
    "Add Expense",
    "View Expenses",
    "Monthly Summary",
    "Category Analysis",
    "Pie Chart",
    "Edit Expense",
    "Delete Expense",
    "Budget Alert"
])

data = load_data()

# 1. Add Expense
if menu == "Add Expense":
    st.subheader("Add New Expense")

    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Travel", "Bills"])
    amount = st.number_input("Amount", min_value=0.0)
    description = st.text_input("Description")

    if st.button("Add"):
        with open(FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([str(date), category, amount, description])
        st.success("Expense Added!")

# 2. View Expenses
elif menu == "View Expenses":
    st.subheader("All Expenses")

    if data:
        for i, row in enumerate(data):
            st.write(f"{i}: {row}")
    else:
        st.warning("No data found")

# 3. Monthly Summary
elif menu == "Monthly Summary":
    st.subheader("Monthly Summary")

    month = st.text_input("Enter Month (YYYY-MM)")

    if st.button("Calculate"):
        total = 0
        for row in data:
            if row[0].startswith(month):
                total += float(row[2])

        st.info(f"Total expenses: {total}")

# 4. Category Analysis
elif menu == "Category Analysis":
    st.subheader("Category Analysis")

    category_data = {}

    for row in data:
        cat = row[1]
        amt = float(row[2])

        category_data[cat] = category_data.get(cat, 0) + amt

    for k, v in category_data.items():
        st.write(f"{k}: {v}")

    if category_data:
        max_cat = max(category_data, key=category_data.get)
        st.success(f"Highest spending: {max_cat}")

# 5. Pie Chart
elif menu == "Pie Chart":
    st.subheader("Expense Distribution")

    category_data = {}

    for row in data:
        cat = row[1]
        amt = float(row[2])
        category_data[cat] = category_data.get(cat, 0) + amt

    if category_data:
        fig, ax = plt.subplots()
        ax.pie(category_data.values(), labels=category_data.keys(), autopct='%1.1f%%')
        ax.set_title("Expense Distribution")
        st.pyplot(fig)
    else:
        st.warning("No data to display")

# 6. Edit Expense
elif menu == "Edit Expense":
    st.subheader("Edit Expense")

    if data:
        index = st.number_input("Enter index", min_value=0, max_value=len(data)-1)

        if st.button("Load"):
            st.session_state["edit_data"] = data[int(index)]

        if "edit_data" in st.session_state:
            row = st.session_state["edit_data"]

            date = st.text_input("Date", row[0])
            category = st.text_input("Category", row[1])
            amount = st.text_input("Amount", row[2])
            description = st.text_input("Description", row[3])

            if st.button("Update"):
                data[int(index)] = [date, category, amount, description]
                save_data(data)
                st.success("Updated successfully!")

    else:
        st.warning("No data found")

# 7. Delete Expense
elif menu == "Delete Expense":
    st.subheader("Delete Expense")

    if data:
        index = st.number_input("Enter index to delete", min_value=0, max_value=len(data)-1)

        if st.button("Delete"):
            data.pop(int(index))
            save_data(data)
            st.success("Deleted successfully!")

    else:
        st.warning("No data found")

# 8. Budget Alert
elif menu == "Budget Alert":
    st.subheader("Budget Alert")

    limit = st.number_input("Enter Budget", min_value=0.0)
    month = st.text_input("Enter Month (YYYY-MM)")

    if st.button("Check"):
        total = 0
        for row in data:
            if row[0].startswith(month):
                total += float(row[2])

        st.write(f"Total spent: {total}")

        if total > limit:
            st.error("⚠️ Budget exceeded!")
        else:
            st.success("✅ Within budget")