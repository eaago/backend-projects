import json
import argparse
import datetime
import tabulate
import csv
from parsers import *
from pathlib import Path

def valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM-DD format")
    
def valid_date_ym(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m")
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM format")

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
    if args.amount < 0:
        print("\nExpense amount cannot be negative.")
        return
    
    total = args.amount
    for item in expenses[1:]:
        item_date = item["date"].split("-")
        args_date = args.date.split("-")
        if args_date[0] == item_date[0] and args_date[1] == item_date[1]:
            total = total + item["amount"]

    if total > expenses[0]:
        print(f"\nWarning: You are exceeding the P{expenses[0]} that you have set. You now have a total of P{total} in expenses in the year {args_date[0]} month {args_date[1]}")

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
                if args.amount < 0:
                    print("\nExpense amount cannot be negative.")
                    return
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

def list_expense(expenses, args):
    if len(expenses) > 1:
        category = False
        header = expenses[1].keys()
        rows = []
        if args.category != None:
            category = True
            for item in expenses[1:]:
                if args.category == item["category"]:
                    rows.append(item.values())
        else:
            for item in expenses[1:]:
                rows.append(item.values())

        if len(rows) == 0 and category == True:
            print("\nNo expenses match the category. Note that this is case sensitive.")
        elif len(rows) == 0 and category == False:
            print("\nThere are no expenses recorded yet.")
        else:
            print(f"\nMonthly budget set: P{expenses[0]}")
            print(tabulate.tabulate(rows, header, tablefmt="grid"))
    else:
        print("\nNo expenses yet to list.")

def summary_expense(expenses, args):
    if len(expenses) > 1:
        if any([args.yrmth, args.category]) == False:
            total = 0
            for item in expenses[1:]:
                total = total + item["amount"]
            print(f"\nTotal expenses: P{total}")
        else:
                total = 0
                if args.yrmth != None and args.category == None:
                    for item in expenses[1:]:
                        item_date = item["date"].split("-")
                        args_date = args.yrmth.split("-")
                        if args_date[0] == item_date[0] and args_date[1] == item_date[1]:
                            total = total + item["amount"]
                    print(f"\nTotal expenses for year {args_date[0]} month {args_date[1]}: P{total}")
                elif args.yrmth == None and args.category != None:
                    for item in expenses[1:]:
                        if args.category == item["category"]:
                            total = total + item["amount"]
                    print(f"\nTotal expenses with category {args.category}: P{total}")
                elif args.yrmth != None and args.category != None:
                    for item in expenses[1:]:
                        item_date = item["date"].split("-")
                        args_date = args.yrmth.split("-")
                        if args_date[0] == item_date[0] and args_date[1] == item_date[1] and args.category == item["category"]:
                            total = total + item["amount"]       
                    print(f"\nTotal expenses for year {args_date[0]} month {args_date[1]} with category {args.category}: P{total}")   
                else:
                    print("\nAn error has occurred.")
    else:
        print("\nNo expenses yet to summarize.")

def budget_update(expenses, args):
    if args.amount < 0:
        print("\nBudget amount cannot be negative.")
        return
    
    previous = expenses[0]
    expenses[0] = args.amount
    write_to_file(expenses)
    print(f"\nBudget amount has been updated from P{previous} to P{args.amount}")

def write_to_file(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent = 2)

def export_expenses(expenses):
    if len(expenses) > 1:
        current_file_path = Path(__file__).resolve()
        header = expenses[1].keys()
        rows = []
        for item in expenses[1:]:
            rows.append(item)
        with open("user_expenses.csv", "w", newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=header)
            dict_writer.writeheader()
            dict_writer.writerows(rows)
        print(f"\nSaved expenses as a csv file at: {current_file_path.parent}\\user_expenses.csv")
    else:
        print("\nNo expenses recorded. There is nothing to export.")