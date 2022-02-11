import collections
from random import choice


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def rank_cards(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    # Example card
    Card = collections.namedtuple('Card', ['rank', 'suit'])

    # Initializing a deck
    deck = FrenchDeck()

    # Had the __getitem__ method not been implemented, this would throw
    # an 'object not subscriptable' error
    print(deck[0])

    # Had the __len__ method not been implemented, this would throw
    # an 'object has no len()' error
    print(len(deck))

    # Pick a random card
    print(choice(deck))

    # Get all Aces
    print(deck[12::13])

    # As _cards is iterable, the 'in' operator works,
    # even tough the __contains__ method is not implemented
    print(Card('Q', 'hearts') in deck)

    # Ranking cards using a custom function
    suit_values = {
        'clubs': 3,
        'hearts': 2,
        'spades': 1,
        'diamonds': 0
    }
    sorted(deck, key=rank_cards)
