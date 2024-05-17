scores = []
choice = None

while choice != "0":
    print(
    """
    рекорды 2.0
    0 -Выйтии 
    1 - показать рекорды
    2 - добавить рекорд
    """
    )
    choice = input("Baш выбор:")
    print()

    if choice == "0":
        print( "До свидания.")
    elif choice == "1":
        print("Рекорды\n")
        print("ИМЯ\tРезультат")
        for entry in scores:
            score, name = entry
            print(name,"\t",score)
    elif choice == "2":
        name = input("Впишите имя игрока:")
        score = int(input("Bnишитe его результат: "))
        entry = (score,name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:]
    else:
        print("Извините. в меню нет пункта",choice)
input("\n\nHaжмитe Enter. чтобы выйти.")