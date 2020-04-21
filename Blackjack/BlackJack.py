import random

print('This is blackjack')
print('The dealer will choose first, you will chose after')

card_deck = [1,2,3,4,5,6,7,8,9,10,11]
player_d = []
dealer_d = []

while len(dealer_d) < 2:
    next_card = random.choice(card_deck)
    dealer_d.append(next_card)
print ('\n You can only see one card: {}' .format(dealer_d[0]))

while len(player_d)<2:
    next_card = random.choice(card_deck)
    player_d.append(next_card)
print('\nYour cards are {} and the sum of these is: {}  '.format(player_d,sum(player_d)))


#dealer decision
while sum(dealer_d) < 17:
    next_card = random.choice(card_deck)
    dealer_d.append(next_card)
    if sum(dealer_d) > 21:
        print('Dealer bust, his total is {}, his cards were {}'.format(sum(dealer_d),dealer_d)
        exit()

#player move 

while sum(player_d) < 21:
    k = int(input('Do you want to hit or stay again?\n1.Hit\n2.Stay'))
    if k == 1:
        next_card = random.choice(card_deck)
        player_d.append(next_card)
        if sum(player_d) < 21:
            print('\nYour cards are {} and the sum of these is: {}  '.format(player_d,sum(player_d)))
            continue
        if sum(player_d) > 21:
            print('Thats a bust! Your cards were {}, with a total of {}'.format(player_d,sum(player_d)))
            exit()
    if k == 2:
        print('\nYour total is: {}' .format(sum(player_d)))
        break
    if sum(player_d) > 22:
        print('Thats a bust!')
        exit()


if sum(dealer_d) == sum(player_d):
    print('Thats a draw\n The dealer had the following: {} '.format(dealer_d))

if sum(dealer_d) > sum(player_d):
    print('dealer wins this time! A total of {}'.format(dealer_d))

if sum(dealer_d) < sum(player_d):
    print('You win! {}\n The dealer had {}'.format(player_d,dealer_d) )







