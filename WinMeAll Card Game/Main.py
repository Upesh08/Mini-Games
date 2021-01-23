"""
This script is the main script for this project which defines a main method storing the entire game logic.
Developer: Upesh Maharana
Dated: 2020/12/08
"""


from Player import Player
from Deck import Deck


def main():
    """This method stores the entire game logic"""

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    # Creating players.
    player_one = Player("P_One")
    player_two = Player("P_Two")

    # Creating Deck of cards.
    new_deck = Deck(suits, ranks, values)
    new_deck.shuffle()  # Shuffling the cards.

    # Dividing 52 cards equally between the players.
    for x in range(26):
        player_one.add_card(new_deck.deal())
        player_two.add_card(new_deck.deal())

    # print("cards with Player one :", len(player_one.all_Cards_In_Hand))
    # print("cards with Player two :", len(player_two.all_Cards_In_Hand))
    # print("pop one card", player_one.remove())
    # print("pop one card", player_two.remove())

    game_run = True  # A general variable which depicts if the game is finished or not.
    round_counter = 0  # counter to keep counting number of rounds.
    while game_run:
        round_counter += 1
        print("Round: ", round_counter)

        if len(player_one.all_Cards_In_Hand) == 0:
            print(player_one.name, " has no cards left. Hence, ", player_two.name, "is the winner !")
            game_run = False
            break

        if len(player_two.all_Cards_In_Hand) == 0:
            print(player_two.name, " has no cards left. Hence, ", player_one.name, "is the winner !")
            game_run = False
            break

        player_one_cards = [player_one.remove()]
        # print("on the table", player_one.remove())
        player_two_cards = [player_two.remove()]
        # print("on the table", player_two.remove())

        at_war = True

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                # then player one gets all the cards that were played in that round
                player_one.add_card(player_one_cards)  # gets own cards
                player_one.add_card(player_two_cards)  # gets opponent's cards as well
                print(player_one.name, " has won the round !!")
                at_war = False

            elif player_two_cards[-1].value > player_one_cards[-1].value:
                # then player two gets all the cards that were played in that round
                player_two.add_card(player_two_cards)  # gets own cards
                player_two.add_card(player_one_cards)  # gets opponent's cards as well
                print(player_two.name, " has won the round !!")
                at_war = False

            else:
                print("--------------")
                print("Its a War !!")
                print("--------------")
                if len(player_one.all_Cards_In_Hand) < 3:
                    print(player_one.name, "has shortage of cards")
                    print("Therefore, ",player_two.name," has WON !!")
                    game_run = False
                    break

                elif len(player_two.all_Cards_In_Hand) < 3:
                    print(player_two.name, "has shortage of cards")
                    print("Therefore, ", player_one.name, " has WON !!")
                    game_run = False
                    break

                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove())
                        player_two_cards.append(player_two.remove())


# Main getting called.
main()
