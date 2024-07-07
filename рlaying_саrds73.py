class card(object):
    RANKS = ["А","2","З","4","5","6","7","В","9","10","J","Q","К"]
    SUITS = ["с","d","h","s"]
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class нand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = " пустой"
        return rep

    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)



card1 = card(rank= "А" ,suit = "С")
print("Bывoжy на экран объект-карту:")
print(card1)

card2 = card(rank= "2" , suit= "c")
card3 = card(rank= "3" , suit= "c")
card4 = card(rank= "4" , suit= "c")
card5 = card(rank= "5" , suit= "c")
print("\nBывoжy еще четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = нand()
print("\nПeчaтaю карты. которые у меня на руках до раздачи:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПeчaтaю пять карт. которые появились у меня на руках:")
print(my_hand)


your_hand = нand()
my_hand.give(card1,your_hand)
my_hand.give(card2,your_hand)
print("\nПepвыe две из моих карт я передал вам.")
print("Теперь у вас на руках:")
print(your_hand)
print("A у меня на руках:")
print(my_hand)

my_hand.clear()
print("\nY меня на руках после того. как я сбросил все карты:")
print(my_hand)
input("\n\nHaжмитe Enter. чтобы выйти.")


