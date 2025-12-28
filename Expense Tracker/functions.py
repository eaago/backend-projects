
def retrieve_expenses():
    with open("expenses.json", "a+") as f:
        f.seek(0)

        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []