class Critter(object):
    def __init__(self,name,hunger = 0,boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
            m = "прекрасно"
        elif 5<= unhapiness <=10:
            m = "неплохо"
        elif 11<= unhapiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m
    def talk(self):
        print("Meня зовут",self.name,".и сейчас я чувствую себя",self.mood,"naw.\n")
        self.__pass_time()
    def eat(self,food = 4):
        print("Мррр.Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.__pass_time()
    def play(self,fun = 4):
        print("Yиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
def main():
    crit_name = input("Kaк вы назовете свою зверюшку? ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
        ("""
        Моя зверюшка
        О - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
        choice = input("Baш выбор:")
        print()
        if choice == "0":
            print("Дo свидания.")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Извините. в меню нет пункта",choice)
main()
input("\n\nHaжмитe Enter. чтобы выйти.")










