from expenses import *
from validation import *
from reports import *

def showMenu():
    print("=" *30)
    print("         EXPENSE TRACKER         ")
    print("=" *30)
    print()

    print("""
    
    1. Add Expense
    2. Show All Expense
    3. Edit Expense
    4. Delete Expense
    5. Search Expense
    6. Show Total Expense
    7. Show Catagories
    8. Export to CSV

    0. Exit
    
    """)
    print("=" *30)

def startApp():
    while True:
        showMenu()

        choice = int(input("Enter Choice; "))

        try:
            if choice == 1:
                title = input("Enter expense title; ")
                amount = input("Enter expense amount; ")

                print("""
                    -----  Pick Expense Catagory  -----

                    Food
                    Shoping
                    Education
                    Health
                    Entertainment
                    Other

                    ------------------------------------
                """)

                catagory = input("Enter expense catagory name; ")

        except Exception



            elif choice == 2:
                getAllExpense()

            elif choice 