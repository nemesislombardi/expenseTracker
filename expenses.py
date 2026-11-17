import uuid
from datetime import date
from storage import *
from validation import *
from exceptions import expensesNotFound

def addExpense(title, amount, catagory):

    expenses = loadExpense()

    expense ={
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "catagory": validateCatagory(catagory),
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    saveExpense(expenses)

    print("Expense succsesfuly added.")
    print(f"Expense id: {expense['id']}")

    return expense

def getAllExpense():
    return loadExpense()

def searchExpense(expenseID):
    expenses = loadExpense()

    for x in expenses:
        if x["id"] == expenseID:
            print("-" *30)

            print(f"ID; {x['id']}")
            print(f"Title; {x['title']}")
            print(f"Amount; {x['amount']}")
            print(f"Catagory; {x['catagory']}")
            print(f"Date; {x['date']}")
            
            return

    print(expensesNotFound())

def updateExpense(expenseID, title, amount, catagory):
    expenses = loadExpense()

    for x in expenses:
        if x["id"] == expenseID:
            x["title"] = validateTitle(title)
            x["amount"] = validateAmount(amount)
            x["catagory"] = validateCatagory(catagory)

            saveExpense(expenses)
            return "Succsesfuly updated."

    expensesNotFound()

def deleteExpense(expenseID):
    expenses = loadExpense()

    for x in expenses:
        if x["id"] == expenseID:
            expenses.remove(x)
            saveExpense(expenses)
            return "Succsesfuly removed."

    expensesNotFound()
