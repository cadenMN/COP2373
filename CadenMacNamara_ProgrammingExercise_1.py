
# Defining variables and constants
LIMIT = 4
TICKET_LIMIT = 10

sold = 0
bought = 0
remaining = TICKET_LIMIT
buyers = 0

# Main body of code
def main():

    # Calls to run ticket selling process
    selling()

    # Prints number of buyers/ end of program
    print('')
    print('All tickets sold!')
    print('There were ' + str(buyers) + ' buyers in total.')


# Operation of ticket selling
def selling():

    # Weren't recognized as global due to later defining
    global sold
    global buyers

    # Asks for input, states remaining tickets, totals sold tickets, and totals number of buyers
    while sold != TICKET_LIMIT:
        while True:
            try:
                bought = int(input('Number of movie tickets you need: (limit is ' + str(LIMIT) +') '))

                # Catches input higher than LIMIT
                if bought > LIMIT:
                    a = b # intentional error to reset input

                # Totals sold tickets, tells remaining left, and counts buyers
                sold += bought
                remaining = TICKET_LIMIT - sold
                print('')
                print('The remaining number of tickets is ' + str(remaining))
                buyers += 1
                break

            # Catches input that isn't a number
            except:
                print('')
                print('Please buy ' + str(LIMIT) + ' or less tickets!')


# Calling to run code
main()