# Expense Tracker CLI

A terminal-based expense tracking application written in Python. Track daily expenses, manage a monthly budget, view summaries, and export records through a structured command-line interface.

Project specs can be found in [Expense Tracker CLI](https://roadmap.sh/projects/expense-tracker).

---

## Features

* Add, update, and delete expenses
* Categorize expenses (default: `General`)
* Set and update a monthly budget
* View expense lists with optional category filtering
* Generate expense summaries by month, category, or both
* Automatic budget warnings when monthly expenses exceed the set limit
* Export expenses to a CSV file
* Persistent storage using a JSON file

---

## Requirements

* Python **3.8+**
* External dependencies:

  * `tabulate`

Install dependency:

```bash
pip install tabulate
```

---

## Installation

1. Clone or download this repository
2. Ensure Python is installed:

```bash
python --version
```

3. Navigate to the project directory

---

## Usage

Run the application:

```bash
python expense_tracker.py <command> [options]
```

---

## Commands

### `add`

Add a new expense.

```text
add --description <text> --amount <number> [--category <text>] [--date YYYY-MM-DD]
```

Example:

```text
python expense_tracker.py add --description "Lunch" --amount 250 --category Food --date 2025-12-22
```

---

### `update`

Update one or more fields of an existing expense.

```text
update --id <expense_id> [--description <text>] [--amount <number>] [--category <text>] [--date YYYY-MM-DD]
```

Example:

```text
python expense_tracker.py update --id 2 --amount 300 --category Dining
```

---

### `delete`

Delete an expense by its ID.

```text
delete --id <expense_id>
```

Example:

```text
python expense_tracker.py delete --id 3
```

---

### `list`

List all expenses or filter by category.

```text
list [--category <text>]
```

Example:

```text
python expense_tracker.py list --category Food
```

---

### `summary`

Display summarized expenses.

```text
summary [--yrmth YYYY-MM] [--category <text>]
```

Examples:

```text
python expense_tracker.py summary
python expense_tracker.py summary --yrmth 2025-12
python expense_tracker.py summary --category Transport
python expense_tracker.py summary --yrmth 2025-12 --category Food
```

---

### `budget`

Set or update the monthly budget.

```text
budget --amount <number>
```

Example:

```text
python expense_tracker.py budget --amount 5000
```

---

### `export`

Export all recorded expenses to a CSV file.

```text
export
```

The file will be saved as:

```text
user_expenses.csv
```

---

## Data Storage

Expenses are stored in a file named:

```text
expenses.json
```

Data structure:

```json
[
  5000,
  {
    "id": 1,
    "description": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2025-12-22"
  }
]
```

* Index `0` stores the current monthly budget
* Expense IDs are reassigned after deletions

---

## Notes & Limitations

* Dates must follow `YYYY-MM-DD` format
* Summary month format is `YYYY-MM`
* Category matching is case-sensitive
* Negative amounts are not allowed
* Budget warnings do not block expense creation

---

## License

This project is for learning and personal use. Feel free to modify and expand it.
