import random
from IPython.display import clear_output

#Define variables 
deck= list(range(1,11))
player_deck = []
dealer_deck = []
end_game = (False)


# Define the game
# Tell the player the game is about to begin 
print('Welcome to blackjack, the rules are simple.\nThe dealer, and yourself get 2 cards each. You choose if you want another card or not.')
print('The closest to 21 (given that you are not over 21) ......Wins ')
        
# Shuffle the cards - give 2 to the dealer (only displaying 1), give 2 to player (displaying both)
while len(dealer_deck) != 2:
    next_card = random.choice(deck)
    dealer_deck.append(next_card)
print('The dealer has 2 cards, one of which is {}'.format(dealer_deck[0]))

# After shuffle give the user the total of his cards
while len(player_deck) != 2:
    next_card = random.choice(deck)
    player_deck.append(next_card)
print('Your cards are the following {}.  \nTotal of which is {}'.format(player_deck,sum(player_deck)))

# Give the user the opportunity to hit or stay

while sum(player_deck) < 22:        
    k = int(input('Do you want to:\n 1.Hit  \n 2.Stay   '))
    if k == 1 and sum(player_deck) < 22 :
        next_card = random.choice(deck)
        player_deck.append(next_card)
        print('Your cards are the following {}.  \nTotal of which is {}'.format(player_deck,sum(player_deck)))
        continue
    if k == 2:
        pass
    if sum(player_deck) >= 22:
        print('Thats a bust. Dealer wins - Dealer total is {}' .format(dealer_deck))
        quit()
    # Dealer must decide if he is to take another card or stay
    # Define the winner 