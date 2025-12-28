import argparse
import datetime
from functions import valid_date, valid_date_ym

def create_parsers():
    parser = argparse.ArgumentParser(prog="Expense Tracker")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", type=int, required=True)
    add_parser.add_argument("--category", required=False, default="General")
    time = datetime.datetime.now()
    add_parser.add_argument("--date", type=valid_date, required=False, default=time.strftime("%Y-%m-%d"))         # Used for testing different dates. Defaults to current date.

    # Update

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", type=int, required=True)
    update_parser.add_argument("--description")
    update_parser.add_argument("--amount", type=int)
    update_parser.add_argument("--category")
    update_parser.add_argument("--date", type=valid_date)

    # Delete

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    # List

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--category")

    # Summary

    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--yrmth", type=valid_date_ym)
    summary_parser.add_argument("--category")

    # Budget

    budget_parser = subparsers.add_parser("budget")
    budget_parser.add_argument("--amount", type=int, required=True)

    # Export

    export_parser = subparsers.add_parser("export")

    return parser