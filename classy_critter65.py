class Critter(object):
    total = 0
    @staticmethod
    def Status():
        print("\nBcero зверюшек сейчас" , Critter.total)
    def __init__(self,name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1

print("Haxoжy значение атрибута класса Critter.total :",end=" ")
print(Critter.total)
print("\nCoздaю зверюшек ")
crit1 = Critter("зверюшка 1")
crit2 = Critter("зверюшка 2")
critЗ = Critter("зверюшка 3")
Critter.Status()
print("\nOбpaщaюcь к атрибуту класса через объект:", end=" ")
print(crit1.total)
input("\n\nHaжмитe Enter. чтобы выйти.")