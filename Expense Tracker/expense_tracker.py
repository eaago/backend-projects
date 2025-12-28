import json
from parsers import *
from functions import *

parser = create_parsers()

# Main

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
    pass
elif args.command == "summary":
    pass
elif args.command == "budget":
    # print(f"You have updated your monthly budget from {budget} to {args.amount}")
    pass
else:
    print("An error has occured.\n")