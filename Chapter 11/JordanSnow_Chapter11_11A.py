
import random


class Deck():

    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]


ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

suits = ['clubs', 'diamonds', 'hearts', 'spades']

my_deck = Deck(52)

current_card = 1

cards = {0:''}

# Deal one poker hand
print('Here is your hand: ')
for i in range(1):
    for i in range(5):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        hand = (ranks[r], suits[s])
        cards[current_card] = hand
        #print(cards[current_card])
        #print(type(hand))
        current_card += 1
        #print(current_card)
        cards[current_card] = ''
        print(ranks[r], 'of', suits[s])
    print()

def main():

    print('You may choose up to three cards to replace.')
    draw = input('Would you like to draw any cards? (y/n) ')
    if draw == 'y':
        new_cards = []
        draw_amount = int(input('Please tell me how many cards you would like to draw: '))
        while draw_amount > 3 or draw_amount <= 0:
            print('You can only draw up to three cards.')
            draw_amount = int(input('Please tell me how many cards you would like to draw: '))
        for i in range(draw_amount):
            d = my_deck.deal()
            r = d % 13
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
