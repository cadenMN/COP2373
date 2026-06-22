
# Imports reduce from functools for use
from functools import reduce

# Program: Asks user to list their expenses (type and cost)
# then totals costs and states highest and lowest expenses
def main():

    # Creates list for tuples of expenses to be added
    expenses = []

    # Asks for number of expenses that will be entered
    numOfExpenses = int(input("How many expenses do you want to analyze/have: "))

    # For loop to do exact number of expenses
    for i in range(numOfExpenses):

        # Asks user for the expense and its cost, then adds it as a tuple to expenses list
        # List of tuples to keep expense and its cost together
        print('')
        expenseType = input("Expense type: ")
        expenseCost = int(input("Cost of expense: $"))
        expenses.append((expenseType, expenseCost))

    # Calculates total cost, highest and lowest expense

    # Adds only expenseCost of tuples together
    # Total = accumulator, item[1] = cost part of each tuple
    totalCost = reduce(lambda total, item: total + item[1], expenses, 0)
    # Find the highest cost expense
    # item1 and item2 = first and second tuples being compared
    # Compares cost part of each tuple
    highestExpense = reduce(lambda item1, item2: item1 if item1[1] > item2[1] else item2, expenses)
    # Find the lowest expense
    lowestExpense = reduce(lambda item1, item2: item1 if item1[1] < item2[1] else item2, expenses)

    # Prints results to user
    print('')
    print('Your total expenses are: $' + str(totalCost))
    print('Your highest expense is "' + str(highestExpense[0]) + '" with a cost of $' + str(highestExpense[1]))
    print('Your lowest expense is "' + str(lowestExpense[0]) + '" with a cost of $' + str(lowestExpense[1]))

    # End of program

# Call code to run program
main()