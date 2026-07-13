
# Creates class BankAcct that has the information of a bank account
# as variables. Has methods for altering information.
class BankAcct:

    #
    def __init__(self, name, accNumber, balance, intRate):
        self.name = name
        self.accNumber = accNumber
        self.balance = balance
        self.intRate = intRate

    # Method for changing account interest rate
    def adj_intRate(self):
        self.intRate = float(input("What is your account's new interest rate (enter as a decimal): "))

    # Method for withdrawing or depositing money from account
    def balance_adj(self):
        # Get user choice of adding or taking money
        withDeposit = input('Would you like to withdraw or deposit (type w or d)? ')

        # Check user choice, get amount to change, and apply balance change
        if withDeposit == 'w':
            self.balance -= float(input("How much would you like to withdraw? $"))
        if withDeposit == 'd':
            self.balance += float(input("How much would you like to deposit? $"))

    # Method for printing current balance and interest rate
    def __str__(self):
        return ('Your account balance is $'+ str(self.balance) + ' with an interest rate of ' + str(self.intRate))

    # Method for calculating interest based on number of days
    def intPredict(self):

        # Get number of days, calculate interest from those days, and print it to user
        days = int(input("How many days is your interest building? "))
        predictedInterest = self.balance * days * (self.intRate / 365)
        print("Your interest after " + str(days) + " days is $" + str(round(predictedInterest,2)))

# Function that tests usage of the BankAcct class
def test():

    # Creates instance of a BankAcct class
    testAcct = BankAcct('Caden', '123456', 1000, .5)

    # Uses methods to change and print account information
    print('')
    testAcct.adj_intRate()
    print('')
    testAcct.balance_adj()
    print('')
    print(testAcct)
    print('')
    testAcct.intPredict()

    # End of program


# Calls test function for program to run
test()