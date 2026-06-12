
# Program: Asks user for an email input and checks for spam
def main():

    # Asks user to input an email message
    userMessage = input("Enter an email message: ")

    # Runs scan_message to evaluate how likely message is spam
    # and assigns variables from scan_message into this function
    spamScore, caughtWords = scan_message(userMessage)

    # Prints spam evaluation to user. Likelihood based on spamScore ranges
    print('')
    print('The emails spam score is ' + str(spamScore))
    if spamScore < 5:
        print('The message is most likely not spam. It should be ok.')
    elif spamScore <= 10:
        print('The message is possibly spam. Be skeptical!')
    elif spamScore > 10:
        print('The message is most likely spam. Check its validity or disregard it!')
    # Prints words that counted as spam
    print('The words/phrases that counted as spam were: ' + ', '.join(caughtWords))

    # End of program


# Compares user input to list of common spam words/phrases and counts how many
def scan_message(userMessage, ):

    # list of 30 common spam words and phrases
    spamWords = ['limited time', 'immediate action', 'winner', 'free money', 'risk-free', 'cash bonus', 'act now',
                 'free trial', 'last chance', "don't miss out", 'cure', 'miracle', 'health benefits', 'dear friend',
                 'dear customer', 'verify', 'click the link', 'your safety', 'get started now', '100% free',
                 'be your own boss', 'billion', 'eliminate bad credit', 'fast cash', 'free access', 'gift',
                 'full refund', 'giveaway', 'lowest price', 'prize']
    # Define variables for later use
    spamScore = 0
    caughtWords = []
    lowerUserMessage = userMessage.lower()

    # Uses for loop to go through each word/phrase in spamWords
    for i in spamWords:
        # Counts total spam occurrences
        spamScore += lowerUserMessage.count(i)

        # Checks if word/phrase was caught
        caught = lowerUserMessage.count(i)
        if caught > 0:
            # Collects words/phrases that counted as spam
            caughtWords.append(i)
        # Reset value
        caught = 0

    # Returns values for use in Main
    return spamScore, caughtWords

# Calls main for program to run
main()