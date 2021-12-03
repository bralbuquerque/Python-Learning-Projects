import Definitions

# Initializations
black_jack = True

print('*******************************************************************************')
print('*                                                                             *')
print('*                           Welcome to Blackjack                              *')
print('*                                                                             *')
print('*******************************************************************************\n')

player_name = input('Player: What is your name? ')
player_bank = int(input('Player: Amount to play? '))



#GAME LOGIC
# While loop for keep playing Black Jack
while black_jack:
    game_on = True

    # Create Players
    player = Definitions.Player(player_name, player_bank)
    dealer = Definitions.Player('Dealer', 0)

    # Create deck
    game_deck = Definitions.Deck()

    # Shuffle Deck
    game_deck.shuffle()

    # Ask for players bet
    bet = Definitions.game_bet()

    # Deal two cards for each player (player and dealer)
    player.add_cards(game_deck.deal_one())
    player.add_cards(game_deck.deal_one())
    dealer.add_cards(game_deck.deal_one())
    dealer.add_cards(game_deck.deal_one())


    # Show cards (two of player, one of dealer)
    Definitions.show_some(player, dealer)

    # While loop for keep playing the round
    while game_on:

        # Hit or Stand
        game_on = Definitions.stand_hit(game_deck, player)

        # Show Cards
        Definitions.show_some(player, dealer)

        # Check if player Bust and if yes Break inner loop
        if player.value > 21:
            Definitions.player_bust(player, dealer, bet)
            break

        # If not bust keep dealing cards to dealer until 17
    if player.value <= 21:
        while dealer.value < 17:
            Definitions.hit(game_deck, dealer)

         # Show Cards
        Definitions.show_all(player, dealer)

        # Run scenarios
        if dealer.value > 21:
            Definitions.dealer_bust(player, dealer, bet)
        elif dealer.value > player.value:
            Definitions.dealer_win(player, dealer, bet)
        elif dealer.value < player.value:
            Definitions.player_wins(player, dealer, bet)
        else:
            Definitions.push(player, dealer, bet)

    # Show Players Bank
    player_bank = player.bank
    print(f'{player.name} winnings stand at: {player.bank}')


    # Ask if Player want to play again
    while True:
        ans = input('Do you want to play again? (y/n)')
        if ans == 'y':
            break
        elif ans == 'n':
            black_jack = False
            print('Thank you for playing!!!')
            break
        else:
            pass





