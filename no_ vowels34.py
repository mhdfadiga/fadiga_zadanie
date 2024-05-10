message = input("Введите  текст:")
new_message = ""
vowels = "авраврвалвармва"
print()
for letter in message:
    if letter.lower() not in vowels:
        new_message += letter
        print("Создана новая строка:", new_message)
print("\nВот ваш текст с изьятыми гласными буквами :" , new_message)
input("\n\n Нажмите Enter, чтобы выйти.")
