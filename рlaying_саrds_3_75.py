class Card(object):
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "В", "9", "10", "J", "Q", "К"]
    SUITS = ["с", "d", "h", "s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    def __str__(self):
        return "<нельзя распечатать>"

class Positionable_Сard(Card):
    def __init__(self,rank,suit,face_up = True):
        super(Positionable_Сard,self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            return super(Positionable_Сard,self).__str__()
        else:
            return "XX"

    def flip(self):
        self.is_face_up = not self.is_face_up


Card1 = Card("A","C")
Card2 = Unprintable_Card("A","d")
Card3 = Positionable_Сard("A","h")

print("Печатаю объект Card:")
print(Card1)

print("\nneчaтaю объект UnprintaЫe_Card:")
print(Card2)

print( "\nПечатаю объект Positiоn e_Card: ")
print(Card3)

print("Переворачиваю объект PositionaЫe Card. ")
Card3.flip()

print("\nПeчaтaю объект PositionaЫe_Card:")
print(Card3)
input("\n\nHaжмитe Enter. чтобы выйти.")