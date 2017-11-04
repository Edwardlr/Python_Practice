import random


# Deal the Card(dealer)
def play_game():
    total_hands = 0

    dealer_score = 0

    player_score = 0

    while total_hands < 5:
        # Dealer cards
        dealer_cards = []

        # Player cards
        player_cards = []

        while len(dealer_cards) != 1:
            dealer_cards.append(random.randint(1, 11))
            if  len(dealer_cards) == 1:
                print("Dealer has card", dealer_cards[0])

        # Deal the Card(player)

        while len(player_cards) != 1:
            player_cards.append(random.randint(1, 11))
            if len(player_cards) == 1:
                print("Player has card", player_cards[0])

        print("\nDealer begin:\n")
        while sum(dealer_cards) < 21:
            dealer_choice = input("Type hit to continue or anything else to stop")
            if dealer_choice == 'hit':
                dealer_cards.append(random.randint(1,11))
                print("Dealer now have a total of " + str(sum(dealer_cards)) + " from these cards ", dealer_cards)

                if sum(dealer_cards) == 21:
                    print('Dealer wins!!')
                    dealer_score += 1
                    break
                elif sum(dealer_cards) > 21:
                    print('Dealer busted!! Player wins!!')
                    player_score += 1
                    break

            else:
                print("Dealer now have a total of " + str(sum(dealer_cards)) + " from these cards ", dealer_cards)
                break


        print("\nPlayer begin:\n")

        while sum(player_cards) < 21 and sum(dealer_cards) < 21 :
            player_choice = input("Type hit to continue or anything else to stop")
            if player_choice == 'hit':
                player_cards.append(random.randint(1,11))
                print("Player now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)

                if sum(player_cards) == 21:
                    print('Player wins!!')
                    player_score += 1
                    break
                elif sum(player_cards) > 21:
                    print('Player busted!! Dealer wins!!')
                    dealer_score += 1
                    break
            else:
                if sum(player_cards) > sum(dealer_cards):
                    print("Player win!!!")
                    player_score += 1
                    break
                elif sum(player_cards) < sum(dealer_cards):
                    print("Dealer wins!!!")
                    dealer_score += 1
                    break
                else:
                    print("Dealer wins!!!")
                    dealer_score += 1
                break

        print("Current Best of 5 Hands:")
        print("Dealer: " + str(dealer_score) + " hands " +  " - to - Player " + str(player_score) + " hands ")
        print("-------------BEST----------OF------------FIVE-----------HANDS    ")
        total_hands += 1

play_game()
