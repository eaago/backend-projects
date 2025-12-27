import argparse
import datetime

parser = argparse.ArgumentParser(prog="Expense Tracker")

subparsers = parser.add_subparsers(dest="command", required=True)

# Add

add_parser = subparsers.add_parser("add")
add_parser.add_argument("--description", required=True)
add_parser.add_argument("--amount", type=int, required=True)
add_parser.add_argument("--date", required=False, default=datetime.datetime.now())                   # Used for testing. Defaults to current date.

# Update



# Main

args = parser.parse_args()

if args.command == "add":
    print(f"Add {args.description} with amount {args.amount} at {args.date}")