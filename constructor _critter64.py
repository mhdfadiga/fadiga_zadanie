class Criiter(object):
    def __init__(self,name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
    def __str__(self):
        print("\nПpивeт. Я зверюшка - экземпляр класса Critter.")
        rep = "Объект класса Critter\n"
        rep += "имя:" + self.name + "\n"
        return rep
    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")
crit1 = Criiter("Бoбик")
crit1.talk()
crit2 = Criiter("Мурзик")
crit2.talk()
print("Bывoд объекта critl на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту critl.name:")
print(crit1.name)
input("\n\nHaжмитe Enter. чтобы выйти.")