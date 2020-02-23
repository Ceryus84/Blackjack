from Card import Card


class Facecard(Card):
    # this class will be a subclass of Card that will have a suit, color, and face instead of number

    def __init__(self, color, suit, face):
        Card.__init__(self, color, suit)
        self.fc = face


queen = Facecard("Black", "Clubs", "Queen")
print(queen)
