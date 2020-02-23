class Card:
    # the card class wil define card based on color and suit

    def __init__(self, color, suit):
        # an object in the Card class must have two elements, the suit and the color
        self.col = color
        self.st = suit

    def __str__(self):
        # allows cards to be known, only says color and suit
        return str(self.col)+" "+str(self.st)


redheart = Card("Red", "Hearts")
print(redheart)
