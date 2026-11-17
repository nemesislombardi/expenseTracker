import csv
from expenses import getAllExpense

dataFile = "expenses.csv"
FieldNames = ["id", "title", "amount", "catagory", "date"]

def totalExpense():
    expenses = getAllExpense()

    total = 0

    for x in expenses:
        amount = x['amount']
        total += amount

    print("Total amount; ", total)


def exportToCsv():
    expenses = getAllExpense()

    try:
        with open(dataFile, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, newfile="", FieldNames=FieldNames)
            writer.writeheader()
            writer.writerows(expenses)

        return dataFile

    except Exception as e:
        print("Error found;", e)
