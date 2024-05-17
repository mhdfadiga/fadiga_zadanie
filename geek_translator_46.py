choice = None
while choice != "0" :
    print("""
    Переводчик с гикского на русский 
    О - Выйти 
    1 -Найти толкование термина 
    2 -Добавить термин 
    3 -Изменить толкование 
    4 -Удалить термин 
    """)
    choice = input("Ваш выбор:")
    print()

    if choice == "0":
        print("Дo свидания.")
    elif choice == "1":
        term = input("Kaкoй термин вы хотите перевести с гикского на русский? ")
        if term in geek:
            definition = geek[term]
            print("\n".term,"означает",definition)
        else:
            print("\nYвы. этот термин мне незнаком:", term)