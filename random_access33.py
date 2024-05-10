import random
word = "яндекс"
print("В переменной word хранить слово :" , word,"\n")
high = len(word)
low =  -len(word)
for i in range(10):
    position = random.randrange(low,high)
    print("word[",position , "]\t", word[position])
input("\n\n Нажмите Enter, чтобы выйти.")