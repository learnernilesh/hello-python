import card
from random import shuffle

class Deck():
    cards = []
    @classmethod
    def initialize(Deck):
        for s in card.Card.suit:
            for v in card.Card.value:
                newCard = card.Card(s, v)
                Deck.cards.append(newCard)
        return Deck.cards

    def __init__(self, name):
        self.name = name
        self.cards = Deck.initialize()

    def __repr__(self):
        return (f"This is card deck {self.name} has {len(self.cards)} cards in it")
    
    def shuffleDeck(self):
        shuffle(self.cards)

if __name__ == "__main__":
    myDeck = Deck("DeckX")
    print(myDeck)
    # for card in myDeck.cards:
    #     print (card)
    # myDeck.shuffleDeck()
    # for card in myDeck.cards:
    #     print (card)
    