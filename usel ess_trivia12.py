name = input("Привет. Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
weigher = int(input("Xopoшo. и последний вопрос. Сколько в тебе килограммов?"))
print("\nEcли бы поэт Каммингс адресовал тебе письмо. он бы обратился к тебе так: " ,name.lower())
print("A если бы это был рехнувшийся Каммингс. то так: ",name.upper())
called = name * 5
print("\nEcли бы маленький ребенок решил привлечь твое внимание")
print("\noн произнес бы твое имя так:")
print(called)
second = age * 365 * 24 * 60 * 60
print("\nTвoй нынешний возраст - свыше", second,"секунд.")
moon_weight = weigher / 6
print("\nЗнaeтe ли вы. что на Луне вы весили бы всего", moon_weight, "кг?")
sun_weight = weigher * 27.1
print("А вот находясь на Солнце. вы бы весили", sun_weight,"кг. (Но. вы. это продолжалось бы недолго)")
input("\n\nНажмите Enter. чтобы выйти.")