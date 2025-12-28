import argparse
import datetime

parser = argparse.ArgumentParser(prog="Expense Tracker")

subparsers = parser.add_subparsers(dest="command", required=True)

# Add

add_parser = subparsers.add_parser("add")
add_parser.add_argument("--description", required=True)
add_parser.add_argument("--amount", type=int, required=True)
add_parser.add_argument("--category", required=False, default="General")
add_parser.add_argument("--date", required=False, default=datetime.datetime.now())                   # Used for testing. Defaults to current date.

# Update

update_parser = subparsers.add_parser("update")
update_parser.add_argument("--id", type=int, required=True)
update_parser.add_argument("--amount", type=int, required=True)

# Delete

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("--id", type=int, required=True)

# List

list_parser = subparsers.add_parser("list")

# Summary

summary_parser = subparsers.add_parser("summary")
summary_parser.add_argument("--month", type=int, required=False)

# Budget

budget_parser = subparsers.add_parser("budget")
budget_parser.add_argument("--amount", type=int, required=True)

# Main

args = parser.parse_args()

if args.command == "add":
    print(f"Add {args.description} with amount {args.amount} at {args.date}")
elif args.command == "update":
    pass
elif args.command == "delete":
    pass
elif args.command == "list":
    pass
elif args.command == "summary":
    pass
elif args.command == "budget":
    print(f"You have updated your monthly budget from {budget} to {args.amount}")
else:
    print("An error has occured.\n")