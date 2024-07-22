"""This program is intended to create a Deck class that simulates the shuffling and dealing of a standard set of
52 cards. The program will have an optional draw phase after the initial deal of 5 cards. This draw phase allows
for up to 3 selected cards out of your hand to be exchanged for new ones out of the deck.
"""

# Import random
import random

# Define class Deck
class Deck():

    # Initialize variable 'size'
    def __init__(self, size):

        # Assign 'self.card_list' equal to i in the range of a specified size (defines the size of the deck)
        self.card_list = [i for i in range(size)]

        # Shuffle 'self.card_list' when initiated
        random.shuffle(self.card_list)

        # Assign 'self.current_card' equal to 0
        self.current_card = 0

        # Assign 'self.size' equal to 'size'
        self.size = size

    # Define deal
    def deal(self):

        # If the size of the deck is zero reshuffle the entire deck
        if self.size - self.current_card < 1:

            # Random.shuffle(self.card_list) all 52 cards will be randomly rearranged
            random.shuffle(self.card_list)

            # Set the current_card back to 0
            self.current_card = 0

            # Print statement to let the user know the deck is being reshuffled
            print('Reshuffling...!!!')

        # Set the current_card equal to 1 greater than it currently is
        self.current_card += 1

        # return the value of the 'card_list' passing in the index the value of current_card - 1
        return self.card_list[self.current_card - 1]

# Set variable 'ranks' equal to a list holding the face values of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Set variable 'suits' equal to a list holding the suit of the cards
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# Set variable 'my_deck' equal to class 'Deck' passing in '52' to specify the size of the deck
my_deck = Deck(52)


# Define poker_hand to deal one poker hand
def poker_hand():

    # Set variable 'cards' to a global variable
    global cards

    # Set variable 'current_card' equal to 1
    current_card = 1

    # Set variable 'cards' equal to an empty dictionary
    cards = {}

    # Print statement to inform the user what their hand looks like
    print('Here is your hand: ')

    # For loop - for i in range(1)
    for i in range(1):

        # For loop - for i in range(5)
        for i in range(5):

            # Set variable 'd' equal to the last 'card' in the simulated deck
            d = my_deck.deal()

            # Set variable 'r' equal to variable 'd' equal to modulo 13
            r = d % 13

            # Set variable 's' equal to variable 'd' equal to floor div
            s = d // 13

            # Set variable 'hand' equal to a tuple or the face value (ranks[r]) and suit (suits[s]) of the card
            # that has been 'dealt'
            hand = (ranks[r], suits[s])

            # Add the tuple generated and assigned to variable 'hand' (this is a card) to the current index of
            # the dictionary 'cards' (to add the card to your hand)
            cards[current_card] = hand

            # Print statement for testing
            #print(cards[current_card])

            # Print statement for testing
            #print(type(hand))

            # Set the value of current_card equal to 1 higher to prepare for next card
            current_card += 1

            # Print statement for testing
            #print(current_card)

            # Delete
            #cards[current_card] = ''

            # Print statement to format the cards in the user's hand
            print(ranks[r], 'of', suits[s])

        # Delete Print statement
        #print()

# Call poker_hand
poker_hand()


# Define main
def main():

    # Print statement to inform user that they can draw up to three cards
    print('You may choose up to three cards to replace.')

    # Set variable 'draw' equal to the input of the user to confirm if they want to draw or not
    draw = input('Would you like to draw any cards? (y/n) ')

    # If statement - if variable 'draw' is equal to 'y'
    if draw == 'y':

        # Set variable 'new_cards' equal to an empty list
        new_cards = []

        # Set variable 'draw_amount' equal to the input from the user specifying how many cards they want to draw,
        # convert the string to an integer
        draw_amount = int(input('Please tell me how many cards you would like to draw: '))

        # While statement - while variable 'draw_amount' is greater than 3 or less than or equal to 0
        while draw_amount > 3 or draw_amount <= 0:

            # Print statement to inform the user they can only draw up to three cards
            print('You can only draw up to three cards.')

            # Set variable 'draw_amount' equal to the input from the user specifying how many cards they want to draw,
            # convert the string to an integer
            draw_amount = int(input('Please tell me how many cards you would like to draw: '))

        # For loop - for i in range(draw_amount)
        for i in range(draw_amount):

            # Set variable 'd' equal to the value 0-51 from the 'deal' attribute
            d = my_deck.deal()

            # Set variable 'r' equal to the value of variable 'd' modulo 13
            r = d % 13

            # Set variable 's' equal to the value of variable 'd' floordiv 13
            s = d //13
            new_cards.append((ranks[r], suits[s]))
        replace_input = (input('Please enter the number(s) corresponding with your hand like to replace (1-5, format example: 1,2,3) '))
        replace_indices = []

        for num in replace_input.split(','):
            replace_indices.append(int(num))

        for index in range(draw_amount):
            replace_index = replace_indices[index]
            cards[replace_index] = new_cards[index]
        print(f'{cards[1][0]} of {cards[1][1]}')
        print(f'{cards[2][0]} of {cards[2][1]}')
        print(f'{cards[3][0]} of {cards[3][1]}')
        print(f'{cards[4][0]} of {cards[4][1]}')
        print(f'{cards[5][0]} of {cards[5][1]}')

    else:
        pass

main()
