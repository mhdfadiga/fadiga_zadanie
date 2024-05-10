word = "пицца"
print("Введите начальный и конечный индексы для того среза 'пицца' , который хотите получить .")
print("для выхода нажмите Enter, не вводя начальную позицио ")
start = None
while start != '':
    start = int(input("\nначальная позиция:"))
    if start :
        finish = int(input("конечная позиция :"))
        print("Срез word[",start,":",finish,"] выглидит как ", end = " ")
        print(word[start:finish])
input("\n\nнажмите Enter. чтобы выйти.")
