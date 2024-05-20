pupa = 30
sipa = 0
zdarovie = 0
mudrost = 0
lovkost = 0
while pupa > 0:
    print(" у вас осталось ",pupa,"пунктов.")
    print("1.Сила:",sipa)
    print("2.Здоровье:",zdarovie)
    print("3.Мудрость:",mudrost)
    print("4.ловкость:",lovkost)
    print("выберите характеристику для изменения")

    choice =(input("вас выбор:"))

    if choice == "1":
        print("Введите колтичество пунктов для силы:")
        points = int(input("пунк:"))
        if points <= pupa + sipa:
            sipa = sipa + points
            pupa = pupa - points
        else:
            print("у вас недостаточно пуктов!")
    elif choice == "2":
        print("Введите количество пунктов для здоровья")
        points = int(input("пунк:"))
        if points <= pupa + zdarovie:
            zdarovie = zdarovie + points
            pupa = pupa - points
        else:
            print("У вас недостаточно пунктов!")
    elif choice == "3":
        print("Введите количество пунктов для Мудрости:")
        points = int(input("пунк:"))
        if points <= pupa + mudrost:
            mudrost = mudrost + points
            pupa = pupa - points
        else:
            print("У вас недостаточно пунктов!")
    elif choice == "4":
        print("Введите количество пунктов для Ловкости:")
        points = int(input("пунк:"))
        if points <= pupa + lovkost:
            lovkost = lovkost + points
            pupa = pupa - points
        else:
            print("У вас недостаточно пунктов!")
    else:
        print("Неверный выбор.")
print("Вы распределили все пункты!")
print("Сила:", sipa)
print("Здоровье:", zdarovie)
print("Мудрость:", mudrost)
print("Ловкость:", lovkost)