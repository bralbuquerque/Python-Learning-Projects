import definitions

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
    player = definitions.Player(player_name, player_bank)
    dealer = definitions.Player('Dealer', 0)

    # Create deck
    game_deck = definitions.Deck()

    # Shuffle Deck
    game_deck.shuffle()

    # Ask for players bet
    bet = definitions.game_bet()

    # Deal two cards for each player (player and dealer)
    player.add_cards(game_deck.deal_one())
    player.add_cards(game_deck.deal_one())
    dealer.add_cards(game_deck.deal_one())
    dealer.add_cards(game_deck.deal_one())


    # Show cards (two of player, one of dealer)
    definitions.show_some(player, dealer)

    # While loop for keep playing the round
    while game_on:

        # Hit or Stand
        game_on = definitions.stand_hit(game_deck, player)

        # Show Cards
        definitions.show_some(player, dealer)

        # Check if player Bust and if yes Break inner loop
        if player.value > 21:
            definitions.player_bust(player, dealer, bet)
            break

        # If not bust keep dealing cards to dealer until 17
    if player.value <= 21:
        while dealer.value < 17:
            definitions.hit(game_deck, dealer)

         # Show Cards
        definitions.show_all(player, dealer)

        # Run scenarios
        if dealer.value > 21:
            definitions.dealer_bust(player, dealer, bet)
        elif dealer.value > player.value:
            definitions.dealer_win(player, dealer, bet)
        elif dealer.value < player.value:
            definitions.player_wins(player, dealer, bet)
        else:
            definitions.push(player, dealer, bet)

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





