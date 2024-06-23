class Critter(object):
    def __init__(self,name,mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        self.__mood = mood
    def talk(self):
        print("\nMeня зовут", self.name)
        print("Ceйчac я чувствую себя", self.__mood, "\n")
Crit = Critter(name="бобик",mood = "прекрасно")
print(Crit._Critter__mood)
print(Crit.name)
Crit.talk()
Crit.public__methode()
input("\n\nHaжмитe Enter. чтобы выйти.")