


# Freecodecamp guided project

# learning Lamba Funcs
# A dictionary is another built-in data type in Python. 
# A dictionary is a collection of data in the form of key-value pairs. 
# Dictionaries are defined with curly braces {} 
# and they contain key-value pairs separated by commas. 
# Each key is followed by a colon : and the value:

# Lambda functions are brief, anonymous functions in Python, 
# ideal for simple, one-time tasks. They are defined by the lambda keyword,
# and they use the following syntax: lambda x: expr
# Lambda functions can be valuably combined with the map() function,
# which executes a specified function for each element 
# in a collection of objects, such as a list: map(lambda x: x * 2, [1, 2, 3])   === [2, 4, 6]

# The sum() function returns the sum of the items 
# in the iterable which is passed as its argument. 
# You are going to use sum() together with map() 
# and lambda functions to get the total amount of expenses.

# float() will take a str or int number as an argument and return a floating point number

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for5 {category}: ')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice =='5':
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()

# Commeted out: orginal tests for sum(), map(), and lambda
# test = lambda x: x * 2
# print(sum(map(test, [2, 3, 5, 8])))