import csv
import os
import datetime

def main():
    filename = "expenses.csv"
    expenses = []
    budget = 0.0
    expenses = load_expenses_from_csvfile(filename)
    
    while True:
        print("-----------------------------------------------------------------------")
        print("Welcome to the WMM (Where's My Money)")
        print("-----------------------------------------------------------------------")
        print("Operations availble in WMM")
        print("\t Type 1 for Adding a Transaction ")
        print("\t Type 2 for Viewing all your transactions so far ")
        print("\t Type 3 for Tracking your budget ")
        print("\t Type 4 for Saving the expenses to a file ")
        print("\t Type 5 for Saving the expenses and exit WMM ")
        print("-----------------------------------------------------------------------")

        user_choice = int(input("Please type in the number of the Operation that you wnat to perform :> "))

        if user_choice == 1:
            expense = get_expenses()
            expenses.append(expense) 
        elif user_choice == 2:
            view_expenses(expenses)
        elif user_choice == 3:
            track_budget(budget, expenses)
        elif user_choice == 4:
            save_expense_to_csvfile(expenses, filename)
        elif user_choice == 5:
            save_expense_to_csvfile(expenses, filename)
            print("Exiting WMM.....")
            break
        else:
            print("Invalid choice has been made. Please enter a valid operation number :>")
 

def set_budget():
    user_budget = float(input("Please enter your monthly budget >: "))
    return user_budget

def track_budget(budget, expenses):
    total_expense = sum(float(expense['amount']) for expense in expenses if expense['amount'])
    budget = set_budget()
              
    if total_expense < budget:
        print("You are WITHIN THE BUDGET and the remaining balance is: ", budget - total_expense)
        print("\n")
    elif total_expense > budget:
        print("You are OVER THE BUDGET and the remaining balance is: ", budget - total_expense)
        print("\n")
    else:
        print("You are AT LIMIT Of THE BUDGET and the remaining balance is: ", budget - total_expense)
        print("\n")


def check_if_file_exists(filename):
    return os.path.isfile(filename)


def view_expenses(expenses):   
    for index, expense in enumerate(expenses, start=1):   
        if not all(expense.values()):
            print(f"{index}, Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['desc']}")
            print("record is not complete \n")
        else:
            print(f"{index}, Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['desc']}")


def load_expenses_from_csvfile(filename):
    expenses = []
    if not check_if_file_exists(filename):
        print("Expense file does not exist. Starting with an emoty file")
        print("Please save the expense file by selecting Option 4")
        print("\n")
        return expenses
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            expenses.append(line)
    
    return expenses

def save_expense_to_csvfile(expense, filename):
    file_exists = os.path.isfile(filename)
    fields = ['date', 'category', 'amount', 'desc']

    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)   
        if not file_exists:
            writer.writeheader()

        writer.writerows(expense)
    print("Expense(s) has been saved")
    print("\n")

def validate_date(date_str):
        datetime.date.fromisoformat(date_str)
    

def get_expenses():
    
    expense_date = input("\t Enter the date in YYYY-MM-DD format :> ")
    expense_category = input("\t Enter the expense category :> ")
    expense_amount = float(input("\t Enter the amount :> "))
    expense_desc = input("\t enter the description :> ")
    
    expense = {
        'date' : expense_date,
        'category' : expense_category,
        'amount' : expense_amount,
        'desc' : expense_desc

    }
    print("Expense has been added")
    print("\n")
    return expense

if __name__ == "__main__":
    main()

