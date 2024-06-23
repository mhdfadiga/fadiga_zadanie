class Critter(object):
    def __init__(self,name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name
    @property
    def name(self):
            return self.__name

    @name.setter

    def name(self,new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")
    def talk(self):
        print("\nПpивeт. меня зовут", self.name)
Crit = Critter("бобки")
Crit.talk()
print("\пМою зверюшку зовут", end=" ")
print(Crit.name)
print("\пПробую изменить имя зверюшки на Мурзик")
Crit.name = "Мурзик"
print("Moю зверюшку зовут", end =" ")
print(Crit.name)
print("\пПробую изменить имя зверюшки на пустую строку")
Crit.name = ""
print("Мою зверюшку зовут", end= " ")
print(Crit.name)
input("\n\nНажмите Eпter. чтобы выйти.")




