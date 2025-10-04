import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense(expenses):
    amount = input("Amount: ")
    if not amount.isdigit() or int(amount) <= 0:
        print("Invalid amount")
        return
    date = input("Date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date")
        return
    category = input("Category: ").strip().lower()
    note = input("Note: ")
    expenses.append({
        "id": len(expenses) + 1,
        "amount": int(amount),
        "date": date,
        "category": category,
        "note": note
    })
    save_expenses(expenses)
    print("Added.")

def view_expenses(expenses):
    if not expenses:
        print("No records.")
        return
    for e in expenses:
        print(f"{e['id']}. {e['date']} | {e['amount']} | {e['category']} | {e['note']}")

def update_expense(expenses):
    view_expenses(expenses)
    try:
        exp_id = int(input("ID to update: "))
        expense = next(e for e in expenses if e["id"] == exp_id)
    except:
        print("Invalid ID")
        return
    expense["amount"] = int(input(f"Amount ({expense['amount']}): ") or expense["amount"])
    new_date = input(f"Date ({expense['date']}): ")
    if new_date and validate_date(new_date):
        expense["date"] = new_date
    expense["category"] = input(f"Category ({expense['category']}): ") or expense["category"]
    expense["note"] = input(f"Note ({expense['note']}): ") or expense["note"]
    save_expenses(expenses)
    print("Updated.")

def delete_expense(expenses):
    view_expenses(expenses)
    try:
        exp_id = int(input("ID to delete: "))
        expenses[:] = [e for e in expenses if e["id"] != exp_id]
        save_expenses(expenses)
        print("Deleted.")
    except:
        print("Invalid ID")

def summary_report(expenses):
    if not expenses:
        print("No records.")
        return
    total = sum(e["amount"] for e in expenses)
    print(f"Total: {total}")
    cats = {}
    for e in expenses:
        cats[e["category"]] = cats.get(e["category"], 0) + e["amount"]
    for c, amt in cats.items():
        print(f"{c}: {amt}")

def filter_expenses(expenses):
    f = input("Filter by date/category: ").strip().lower()
    if f == "date":
        d = input("Date (YYYY-MM-DD): ")
        results = [e for e in expenses if e["date"] == d]
    elif f == "category":
        c = input("Category: ").strip().lower()
        results = [e for e in expenses if e["category"] == c]
    else:
        print("Invalid filter")
        return
    if not results:
        print("No matches.")
    else:
        for e in results:
            print(f"{e['id']}. {e['date']} | {e['amount']} | {e['category']} | {e['note']}")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add\n2. View\n3. Update\n4. Delete\n5. Summary\n6. Filter\n0. Exit")
        ch = input("Choice: ")
        if ch == "1":
            add_expense(expenses)
        elif ch == "2":
            view_expenses(expenses)
        elif ch == "3":
            update_expense(expenses)
        elif ch == "4":
            delete_expense(expenses)
        elif ch == "5":
            summary_report(expenses)
        elif ch == "6":
            filter_expenses(expenses)
        elif ch == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
