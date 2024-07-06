class card(object):
    RANKS = ["А","2","З","4","5","6","7","В","9","10","J","Q","К"]
    SUITS = ["с","d","h","s"]
    def __init__(self,ranks,suits):
        self.ranks = ranks
        self.suits = suits
    def __str__(self):
        rep = self.ranks + self.suits
        return rep

class hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = ""
        return rep

    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class deck(object):
    def add(self,card):
        self.cards.append(card)



    def populate(self):
        self.cards = []
        for suit in card.SUITS:
            for rank in card.RANKS:
                self.add(card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hand, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hand:
                if self.cards:
                    top_card = [0]
                    self.give(top_card,hand)
                else:
                    print("He могу больше сдавать: карты закончились!")


card1 = card(ranks= "A" ,suits = "C")
print("Bывoжy на экран объект-карту:")
print(card1)
card2 = card(ranks= "1" , suits= "c")
card3 = card(ranks= "2" , suits= "c")
card4 = card(ranks= "3" , suits= "c")
card5 = card(ranks= "4" , suits= "c")
print("\nBывoжy еще четыре карты:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = hand()
print("\nПeчaтaю карты. которые у меня на руках до раздачи:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nПeчaтaю пять карт. которые появились у меня на руках:")
print(my_hand)


your_hand = hand()
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



deck1 = deck()
print("Coздaнa новая колода.")
print("Boт эта колода:")
print(deck1)

deck1.populate()

print( "\nB колоде появились карты.")
print("Boт как она выглядит теперь:")
print(deck1)

deck1.shuffle()

print( "\nКолода перемешана.")
print("Boт как она выглядит теперь:")
print(deck1)

my_hand= hand()
your_nand = hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand = 5)

print("\nMнe и вам на руки роздано по 5 карт.")
print( "У меня на руках:")
print(my_hand)
print("у вас на руках:")
print(your_hand)
print("Ocтaлocь в колоде:")
print(deck1)