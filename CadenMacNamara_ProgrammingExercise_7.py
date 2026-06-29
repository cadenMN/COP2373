
# Program uses regular expressions
import re

# Asks user to enter a paragraph and calls sentence_finder
def main():

    # Get user input for analysis
    userParagraph = input('Enter a paragraph for analysis: ')
    print('')

    # Runs sentence_finder using user input
    foundSentences = sentence_finder(userParagraph)

    # Define accumulator variable for number of sentences found
    totalSentences = 0

    # Prints every sentence and gets total number of sentences
    for sentence in foundSentences:
        print(sentence)
        totalSentences += 1

    # Print number of sentences found
    print('')
    print('Total sentences found was', totalSentences)

    # End of program


# Finds all sentences in user paragraph
def sentence_finder(userParagraph):

    # Define pattern for recognizing sentences
    # Sentences can start with a capital letter or a number
    sentPattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Finds every instance of a sentence in userParagraph
    foundSentences = re.findall(sentPattern, userParagraph, flags=re.DOTALL | re.MULTILINE)

    # Returns foundSentences to main function
    return foundSentences


# Call main for program to run
main()