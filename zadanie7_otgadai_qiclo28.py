""" Измените программу «Отгадай число» таким образом, чтобы у игрока было ограниченное количество попыток. Если игрок не укладывается в заданное чисnо (и проигрывает), то программа должна выводить сколь
возможно суровый текст.
 """
import random
print("\tДобро пожаловать в игру 'Отгадай число'!")
print("nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток.\n")
the_number = random.randint(1,100)
guess = int(input("Baшe предположение: "))
tries = 0
while guess != the_number:
    if guess > the_number:
        print("Меньше")
    else:
        print("больше")
    guess = int(input("Ваше предположение:"))
    tries += 1
    if tries >= 3:
        break
print("поиграль")
print("Bы затратили на отгадывание всего лишь ",tries, "попыток!\n")