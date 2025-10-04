# Expense-Tracker

A simple command-line Expense Tracker built in Python.
It helps you record, view, update, delete, and analyze daily expenses.


---

Features

Add, view, update, and delete expenses

Store data in expenses.json file

Categories support (food, travel, bills, etc.)

Summary report (total + by category)

Filter expenses by date or category

Simple CLI menu for navigation



---

Requirements

Python 3.x

No external libraries (only uses built-in modules)



---

How to Run

1. Clone this repo or download the files


2. Make sure expenses.json exists in the same folder

If it’s empty, just keep it as:

[]

Without this file, the program won’t have storage



3. Run the app:

python expense_tracker.py




---

Notes

The program saves data in expenses.json.

If there are no expenses initially, the user must add data through the app itself.

Each expense has:

Amount

Date (YYYY-MM-DD)

Category

Note




---

Example Usage

1. Add
2. View
3. Update
4. Delete
5. Summary
6. Filter
0. Exit


---

Future Improvements

Add a minimal Tkinter UI

Export reports to CSV or PDF

Monthly/weekly analytics

Database (SQLite) integration
