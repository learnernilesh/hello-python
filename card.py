class Card():
    suit = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    def __init__(self, suit, value):
        if suit not in Card.suit or value not in Card.value:
            raise ValueError(f"{Card.value} of {Card.suit} is not a valid card!")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return (f"{self.value} of {self.suit}")

if __name__ == '__main__':
    mycard = Card('Spades', 'A')
    print(mycard)
    