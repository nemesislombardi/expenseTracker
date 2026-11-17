Expense Tracker

A simple command-line expense tracker written in Python. Add, view, edit, delete and search your expenses, see your total spending, and export everything to CSV. Data is stored locally in a JSON file, so there is nothing to install and no database to set up.

Features
Add an expense with a title, amount and category
Show all saved expenses
Edit an existing expense by its ID
Delete an expense by its ID
Search an expense by its ID
Total of all expenses
Categories list
Export to CSV for use in Excel or Google Sheets
Input validation with clear error messages (empty title, non-numeric or negative amount, unknown category)
Requirements
Python 3.8 or newer
No external packages (uses only the standard library: json, csv, uuid, datetime)
Getting Started
Download or clone the project into a folder.
Make sure the folder contains an expenses.json file with an empty list:
json
[]
Open a terminal inside the project folder and run:
bash
python main.py

Run the program from the project folder. expenses.json and expenses.csv are read and written relative to the folder you start it from.

Usage

When the program starts you will see the menu:

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

Type a number and press Enter.

Adding an expense
Enter Choice; 1
Enter expense title; Coffee
Enter expense amount; 3.5
Enter expense catagory name; Food
Data succsefuly saved

Expense succsesfuly added.
Expense id: 613c4309

Keep the ID: you need it to edit, delete or search for that expense.

Categories
Category
Food
Shoping
Education
Health
Entertainment
Other

Category names are not case-sensitive (Food, food and FOOD all work) and are stored in lowercase.

Validation rules
Field	Rule
Title	Cannot be empty
Amount	Must be a number greater than 0
Category	Must be one of the categories above

If an input is invalid, the program shows an error message and returns to the menu without saving anything.

Project Structure
expenseTracker/
├── main.py          # Menu and program loop (entry point)
├── expenses.py      # Add, get, search, update and delete logic
├── validation.py    # Validates title, amount and category
├── storage.py       # Loads and saves expenses.json
├── reports.py       # Total expense and CSV export
├── exceptions.py    # Custom error helpers
└── expenses.json    # Your saved data

How the pieces fit together:

main.py ──> expenses.py ──> storage.py      (read / write JSON)
   │             └───────> validation.py    (check user input)
   └──────> reports.py  ──> expenses.py     (total, CSV export)
Data Format

Each expense is stored in expenses.json like this:

json
{
    "id": "613c4309",
    "title": "Coffee",
    "amount": 3.5,
    "catagory": "food",
    "date": "2026-11-18"
}
Field	Description
id	Random 8-character ID, generated automatically
title	What the expense was for
amount	Amount as a number
catagory	One of the categories above, in lowercase
date	Date the expense was added (YYYY-MM-DD)
CSV Export

Choosing 8. Export to CSV creates (or overwrites) expenses.csv in the project folder with the columns id, title, amount, catagory, date.

Possible Improvements
Filter expenses by category or date range
Show a total per category
Support more than one currency
Add automated tests
License

Free to use for learning and personal projects.
