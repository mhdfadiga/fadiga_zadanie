scores = []
choice = None
while choice != "0":
    print(
    """
    Рекорды
    О - Выйти
    1 - Показать рекорды
    2 - Добавить рекорд
    3 - Удалить рекорд
    4 - Сортировать список
    """
    )
    choice =input("Baш выбор:")
    print()

    if choice == "0":
        print("До свидания")
    elif choice == "1":
        print("Peкopды")
        for score in scores:
            print(score)
    elif choice == "2" :
        score = int(input("Bnишитe свой рекорд:"))
        scores.append(score)
    elif choice == 3:
        score = int(input( "Какой из рекордов удалить?: "))
        if score in scores :
            scores.remove(score)
        else:
            print("Результат", score,"не содержится в списке рекордов.")
    elif choice == 4 :
        scores.sort()

    else:
        print("Извините. в меню нет пункта",choice)
input("\n\nHaжмитe Enter. чтобы выйти.")