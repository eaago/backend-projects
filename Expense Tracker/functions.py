import json
import argparse
import datetime
from parsers import *

def valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM-DD format")

def retrieve_expenses():
    with open("expenses.json", "a+") as f:
        f.seek(0)

        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

    return expenses

def delete_reorder(expenses):
    if len(expenses) != 1:
        for i, task in enumerate(expenses[1:]):
            task["id"] = i + 1
        return expenses
    else:
        return expenses

def add_expense(expenses, args):
    new_expense = {
        "id": len(expenses),
        "description": args.description,
        "amount": args.amount,
        "category": args.category,
        "date": args.date
    }
    expenses.append(new_expense)
    write_to_file(expenses)
    print(f"\nAdded {args.description} with amount {args.amount} at {args.date}")

def update_expense(expenses, args):
    if any([args.description, args.amount, args.category, args.date]) == False:
        print("\nupdate requires at least one of --description, --amount, --date, or --category")
        return
    
    found = False
    for item in expenses[1:]:
        if item["id"] == args.id:
            found = True
            if args.description != None:
                item["description"] = args.description
            if args.amount != None:
                item["amount"] = args.amount
            if args.category != None:
                item["category"] = args.category
            if args.date != None:
                item["date"] = args.date
            break
    if found == False:
        print("\nProvided expense id does not exist.")
        return
    else:
        print(f"\nUpdated expense id {args.id}")
        write_to_file(expenses)

def delete_expense(expenses, args):
    found = False
    for i, item in enumerate(expenses[1:]):
        if item["id"] == args.id:
            found = True
            expenses.pop(i + 1)
            break
    if found == False:
        print("\nProvided expense id does not exist.")
        return
    else:
        print(f"\nDeleted expense id {args.id}")
        expenses = delete_reorder(expenses)
        write_to_file(expenses)

def write_to_file(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent = 2)