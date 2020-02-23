from Card import Card


class Numcard(Card):
    # subclass of Card, defines number cards

    def __init__(self, color, suit, number):
        # a number card should have a color, a suit, and a number
        Card.__init__(self, color, suit)
        self.num = number


four = Numcard("Black", "Clubs", 4)
