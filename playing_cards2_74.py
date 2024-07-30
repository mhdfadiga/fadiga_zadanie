class Cards(object):
    RANKS = ["А", "2", "З", "4", "5", "6", "7", "В", "9", "10", "J", "Q", "К"]
    SUITS = ["с", "d", "h", "s"]
    def __init__(self,rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
            return rep
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

class deck(Hand):
    def populate(self):
        self.cards = []
        for suit in Cards.SUITS:
            for rank in Cards.RANKS:
                self.add(Cards(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand = 1):
        for hand in hands:
            for _ in range(per_hand):
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("He могу больше сдавать: карты закончились!")
deck1 = deck()
print("Coздaнa новая колода.")
print("Boт эта колода:")
print(deck1)


deck1.populate()
print( "\nB колоде появились карты.")
print("Boт как она выглядит теперь:")
print(deck1)

my_hand = Hand()
your_hand =  Hand()
hands = [my_hand,your_hand]
deck1.deal(hands,per_hand = 5)

print("\nMнe и вам на руки роздано по 5 карт.")
print( "У меня на руках:")
print(my_hand)
print("·у вас на руках:")
print(your_hand)
print("Ocтaлocь в колоде:")
print(deck1)

deck1.clear()
print( "\nКолода очищена.")
print("Boт как она выглядит теперь:",deck1)
input("\n\nHaжмитe Enter. чтобы выйти.")