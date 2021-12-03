# File containing class definitions, cards and functions
import random

# Definition of ranks, suits and equivalence between rank and card value
suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
rank_value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
              'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Card class with suit and rank as attribute
class Card():

    def __init__(self,suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Deck class that can be shuffled,printed and one card can be removed and given to player
class Deck():

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        given_card = self.deck.pop()
        return given_card

    def __str__(self):
        deck_cards= ''
        for card in self.deck:
            deck_cards += card.__str__() + '\n'

        return 'The deck has:\n' + deck_cards

# Player class that has as attribute, cards in hand, total value, bank, Ace value and as method add cards, win, lose bet
class Player():

    def __init__(self,  name, bank):
        self.name = name
        self.cards = []
        self.value = 0
        self.ace = 0
        self.bank = bank

    def adjust_aces(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1

    def add_cards(self, card):
        self.cards.append(card)
        self.value += rank_value[card.rank]

    def win_bet(self, bet):
        self.bank += bet

    def lose_bet(self, bet):
        self.bank -= bet

# Function to take game round bet
def game_bet():
    bet = int(input('What is your bet? '))
    return bet

# Function to show all cards
def show_all(player, dealer):
    print('\nDealer Cards:', *dealer.cards, sep = '\n')
    print('Dealer Value:', dealer.value)
    print(f'\n{player.name} Cards:', *player.cards, sep = '\n')
    print(f'{player.name} Value:', player.value)

# Function to show all player cards and hide one card of the Dealer
def show_some(player, dealer):
    print('\nDealer Cards:')
    print('<Hidden Card>')
    print(dealer.cards[1])
    print(f'\n{player.name} Cards:', *player.cards, sep='\n')
    print(f'{player.name} Value:', player.value)

# Function to add cards to player or Dealer hand and adjust aces values in case of hit
def hit(deck, player):
    player.add_cards(deck.deal_one())
    player.adjust_aces()

# Engine to keep adding cards to hand or stand and break loop
def stand_hit(deck, player):
    global game_on

    while True:
        ans = input('Hit or Stand? (h/s)')
        if ans == 'h':
            hit(deck, player)
            game_on = True
        elif ans == 's':
            print('Dealer Playing')
            game_on = False
        else:
            print('Please try again')
            continue
        break
    return game_on

# Definition of different game scenarios
def dealer_bust(player, dealer,  bet):
    print('Dealer bust!!!')
    player.win_bet(bet)

def dealer_win(player, dealer, bet):
    print('Dealer win!!!')
    player.lose_bet(bet)

def player_bust(player, dealer, bet):
    print(f'{player.name} bust!!!')
    player.lose_bet(bet)

def player_wins(player, dealer, bet):
    print(f'{player.name} wins!!!')
    player.win_bet(bet)

def push(player, dealer, bet):
    print(f'{player.name} and Dealer tie!!!')

