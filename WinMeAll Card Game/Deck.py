"""
This script contains a Deck class which creates the entire Deck of fifty two cards.
Developer: Upesh Maharana
Dated: 2020/12/07
"""
from Card import Card
import random


class Deck:
    """A class that creates an entire deck of cards."""

    def __init__(self, suits, ranks, values):
        # --creating totalCards as a list object which depicts as deck of cards.
        self.totalCards = []
        for suit in suits:
            for rank in ranks:
                self.totalCards.append(Card(suit, rank, values))

    def shuffle(self):
        """ This method helps in shuffling the deck of cards.It doesn't return anything"""
        random.shuffle(self.totalCards)

    def deal(self):
        """This method returns a card from the deck of cards"""
        return self.totalCards.pop()
