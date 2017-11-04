import random
import os

# Dealer cards
dealer_cards = []

# Player cards
player_cards = []

# Deal the Card(dealer)
while len(dealer_cards) != 1:
    dealer_cards.append(random.randint(1, 11))
    if  len(dealer_cards) == 1:
        print("Dealer has card", dealer_cards[0])

# Deal the Card(player)

while len(player_cards) != 1:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 1:
        print("Player has card", player_cards[0])

if sum(dealer_cards) == 21:
    print("dealer has 21 and wins!!")
elif sum(player_cards) > 21:
    print("dealer has busted! Player wins!")

print("\nDealer begin:\n")
while sum(dealer_cards) < 21:
    dealer_choice = input("Do you want to stay or hit")
    if dealer_choice == 'hit':
        dealer_cards.append(random.randint(1,11))
        print("Dealer now have a total of " + str(sum(dealer_cards)) + " from these cards ", dealer_cards)

        if sum(dealer_cards) == 21:
            print('Dealer wins!!')
            os._exit(0)
        elif sum(dealer_cards) > 21:
            print('Dealer busted!! Player wins!!')
            os._exit(0)

    else:
        print("Dealer now have a total of " + str(sum(dealer_cards)) + " from these cards ", dealer_cards)
        break


print("\nPlayer begin:\n")
while sum(player_cards) < 21:
    player_choice = input("Do you want to stay or hit")
    if player_choice == 'hit':
        player_cards.append(random.randint(1,11))
        print("Player now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)

        if sum(player_cards) == 21:
            print('Player wins!!')
            os._exit(0)
        elif sum(player_cards) > 21:
            print('Player busted!! Dealer wins!!')
            os._exit(0)



    else:
        print("Player now have a total of " + str(sum(dealer_cards)) + " from these cards ", player_cards)
        break


if sum(dealer_cards) > sum(player_cards):
    print("Dealer wins!!! Dealer's sum is {} and number is {} ".format(sum(dealer_cards), dealer_cards))
    print("Player's sum is {} and number is {}".format(sum(player_cards), player_cards))
elif sum(dealer_cards) < sum(player_cards):
    print("Player wins!!!Player's sum is {} and number is {}".format(sum(player_cards), player_cards))
    print("Dealer's sum is {} and number is {} ".format(sum(dealer_cards), dealer_cards))
else:
    print("Tie")
