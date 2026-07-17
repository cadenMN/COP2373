

# Program uses randomization
import random

# Define class for making card decks
class Deck():

    # Makes card deck of any size
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    # Deals new cards for a hand
    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

# Main body of code
def main():

    # Define card ranks and suits
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    # Make list to hold hand
    hand = []

    # Make instance of deck
    cardDeck = Deck(52)

    # Makes a poker hand of 5 cards
    # Deal makes randomization of number between 1 and size entered
    # rank and suit use math to get number's associated rank and suit
    # Ex: card = 18, rank = 5 -> 7, suit = 0 -> Clubs
    print()
    for i in range(5):
        card = cardDeck.deal()
        rank = card % 13
        suit = card // 13
        print(ranks[rank], 'of', suits[suit])
        hand += [card]
    print()

    # Call reshuffle function to let user change their cards
    # and gets new hand if needed if program is expanded later
    hand = reshuffle(ranks, suits, cardDeck, hand)

    # End of program


# Lets user change cards in their hand
def reshuffle(ranks, suits, cardDeck, hand):

    # Lets user choose whether to change their cards or not
    choice = input('Would you like to reshuffle? (y/n) ')
    if choice == 'n':
        print('No cards changed.')
        return hand

    # Get cards that user would like to reshuffle
    redoCards = input("Which cards do you want to reshuffle? (Ex: 1, 3, 5) ")
    redoCards = redoCards.split(",")
    print()

    # Reshuffle specified cards
    for i in range(len(redoCards)):
        card = cardDeck.deal()
        hand[int(redoCards[i]) - 1] = card

    # Print reshuffled hand
    print('New hand:')
    print()
    for i in range (5):
        card = hand[i]
        rank = card % 13
        suit = card // 13
        print(ranks[rank], 'of', suits[suit])

    # Return altered hand to main
    return hand

# Call main for program to run
main()