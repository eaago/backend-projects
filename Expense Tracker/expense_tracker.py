from parsers import *
from functions import *

# Main

parser = create_parsers()

args = parser.parse_args()
expenses = retrieve_expenses()

if len(expenses) == 0:
    expenses.append(5000)       # Default budget if user did not set amount yet

if args.command == "add":
    add_expense(expenses, args)
elif args.command == "update":
    update_expense(expenses, args)
elif args.command == "delete":
    delete_expense(expenses, args)
elif args.command == "list":
    list_expense(expenses, args)
elif args.command == "summary":
    summary_expense(expenses, args)
elif args.command == "budget":
    budget_update(expenses, args)
else:
    print("An error has occured.\n")