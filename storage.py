import json

dataFile = "expenses.json"

def loadExpense():

    try:
        with open(dataFile, "r", encoding="utf-8") as f:
            expenses = json.load(f)

        return expenses

    except Exception as e:
        print("Error found; ", e)
        return []

def saveExpense(expense):

    try:
        with open(dataFile, "w", encoding="utf-8") as f:
            json.dump(expense, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Error found; ", e)