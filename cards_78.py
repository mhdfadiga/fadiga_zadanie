class Cards(object):
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "В", "9", "10", "J", "Q", "К"]
    SUITS = ["с", "d", "h", "s"]

    def __init__(self,rank,suit,face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    def __init__(self):
        self.cards = []


    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "пустой"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        for suit in Cards.SUITS:
            for rank in Cards.RANKS:
                self.add(Cards(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand):
        for hand in hands:
            if self.cards:
                top_card = self.cards[0]
                self.give(top_card,hand)
            else:
                print("He могу больше сдавать: карты закончились!")
if __name__ == "__main__":
    print
    print("  это модуль.содержащий классы для карточных игр.")
    input("\n\nHaжмитe Enter. чтобы выйти.")






