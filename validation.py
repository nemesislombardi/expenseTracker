from exceptions import *


catagories = {
    "Food"
    "Shoping"
    "Education"
    "Health"
    "Entertainment"
    "Other"
}

def validateTitle(title):
    title = title.strip()

    if not title:
        print("Tittle cannot me empty")

    return title

def validateAmount(amount):
    try:
        amount = float(amount)

    except ValueError:
        invalidExpense("Amount must be a number!")


    if amount <= 0:
        print()


        