"""
This program creates a Card class that will depict a Card in the deck of cards. The object of this class will be a card
and the object will be passed in a total of two string arguments which are nothing but the properties of a card
as discussed below:
 a) Suit of the card.
 b) rank of the card.

Developer: Upesh Maharana
Dated: 2020-12-06
"""


class Card:
    """ Card class depicting a each card. """

    def __init__(self, card_suit, card_rank, values):
        self.suit = card_suit
        self.rank = card_rank
        self.value = values[card_rank]

    def __str__(self):
        result = self.suit + "-" + self.rank
        return result
