import random
WORDS = ("питон","анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
print("word:",word)
corect = word
jump = ""
while word :
    position = random.randrange(len(word))
    jump += word[position]
    word = word[:position] + word[(position+ 1):]
print("""
Добро пожаловать в игру 'Анаграммы'! 
Надо переставить буквы так. чтобы получилось осмысленное слово. 
(Для выхода нажмите Enter. не вводя своей версии.) 
""")

print("вот анаграмма:",jump)
guess = input("\nПопробуйте отгадать исходное слово:")
while guess != corect and guess != "":
    print("K сожалению. вы неправы.")
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == corect:
    print("Дa. именно так! Вы отгадали!\n")
print("Cnacибo за игру.")
input("\n\nHaжмитe Enter. чтобы выйти.")