relation = {}

while True:
    print("\nМеню:")
    print("1. Добавить пару 'СЫН - отец'")
    print("2.Узнать отца ")
    print("3. Заменить отца")
    print("4. Удалить пару 'СЫН - отец'")
    print("5. Показать все пары")
    print("6. Выйти")
    choice = input("Выберите действие:")
    if choice == "1":
        son = input("имя сын:")
        father = input(" имя папа:")
        relation[son] = father
    elif choice == "2":
        son = input("имя сын:")
        print("отца:",relation.get(son,"не найдено"))
    elif choice == "3" :
        son = input("имя сын:")
        if son in relation:
            father = input("новое имя отца")
            relation[son]=father
        else:
            print("отношение не найдено")
    elif choice == "4":
        son = input("имя сын:")
        if son in relation:
            del relation[son]
        else:
            print("отношение не найдено")
    elif choice == "5":
        for son,father in relation.items():
            print(f"{son}- {father}")
    elif choice == "6":
        break
    else:
        print("не правильно выбор")
