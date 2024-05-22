relation = {}

while True:
    print("1. Добавить пару 'СЫН - отец'")
    print("2.Узнать отца")
    print("3.Узнать дедушка")
    print("4.заменить связь сын-отец")
    print("5.Удалить связь сын-отец ")
    print("6.Показать все связи")
    print("7.Выйтий")
    choice = input("вас выбор:")

    if choice == "1":
        son = input("имя сын:")
        father = input("имя отец")
        relation[son]= father
    elif choice == "2":
        son = input("имя сын:")
        print("отец:",relation.get(son,"не найден"))
    elif choice == "3":
        grand_son = input(" имя внука:")
        father =relation.get(grand_son)
        if father:
            grand_father = relation.get(father)
            if grand_father:
                print("дедушка:",grand_father)
            else:
                print("дедушка не найден")
        else:
            print(" отец не найден")
    elif choice == "4":
        son = input("имя сын")
        if son in relation:
            father = input("Введите новое имя отца:")
            relation[son] = father
        else:
            print("Свяьз не найдена")
    elif choice == "5":
        son = input("имя сын")
        if son in relation:
            del relation [son]
        else:
            print("Свяьз не найдена")
    elif choice == "6":
        for son,father in relation.items():
            print(f"{son}- {father}")
    elif choice == 7:
        break
    else:
        print("Неправильно выбор")