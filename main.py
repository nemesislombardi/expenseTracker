from expenses import *
from validation import *
from reports import *

def showMenu():
    print("""
    ----- Expense Tracker App -----

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

def startApp():
    while True:
        showMenu()

        try:
            choice = int(input("Enter Choice; "))


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

                addExpense(title, amount, catagory)
                input("\nPress ENTER to continue...")

            elif choice == 2:
                showAll = getAllExpense()

                if not showAll:
                    print("No expenses found.")

                for x in showAll:
                    print("-" * 30)
                    print(f"ID; {x['id']}")
                    print(f"Title; {x['title']}")
                    print(f"Amount; {x['amount']}")
                    print(f"Catagory; {x['catagory']}")
                    print(f"Date; {x['date']}")

                input("\nPress ENTER to continue...")

            elif choice == 3:
                expenseID = input("Enter current expense ID; ")
                title = input("Enter new expense title; ")
                amount = input("Enter new expense amount; ")

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

                catagory = input("Enter new expense catagory name; ")

                updateExpense(expenseID, title, amount, catagory)

                input("\nPress ENTER to continue...")

            elif choice == 4:
                expenseID = input("Enter expense ID; ")

                deleteExpense(expenseID)
                input("\nPress ENTER to continue...")


            elif choice == 0:
                print("Closing..")
                break


        except Exception as e:
            print("Error Found; ", e)

startApp()