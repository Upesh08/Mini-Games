"""
This python script defines a class called "Player".The object of this class will be the players who will be playing
the game.
Developer: Upesh Maharana
Dated: 2020/12/07
"""


class Player:
    """
    This class will be used to hold a player's list of cards.
    A player should be able to add or remove the cards from their hand (which is nothing but the list of cards)
    """

    def __init__(self, name):
        self.name = name
        self.all_Cards_In_Hand = []

    def remove(self):
        return self.all_Cards_In_Hand.pop(0)

    def add_card(self, new_cards):
        card_type = type(new_cards)
        if card_type == type([]):
            self.all_Cards_In_Hand.extend(new_cards)
        else:
            self.all_Cards_In_Hand.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_Cards_In_Hand)} cards.'
