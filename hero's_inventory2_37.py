inventory = ("меч","кольцуга"," щит","целебное снадобье")
print("\nи так в вашем арсенале:")
for item in inventory:
    print(item)

input("\n Нажмите Enter чтобы продолжить")
print("Сеичас в вашем распоряжении ",len(inventory)," предме/ов.")

input("\n Нажмите Enter чтобы продолжить")
if "целебное снадобье" in inventory:
    print("   вы еще поживете и повоюете")
index = int(input("\n Введите индекс одного из предметов арсенала:"))
print("Под индексом",index,"в арсенале находится",inventory[index])
start = int(input("\n Введите начальный индекса среза"))
finish = int(input("\n Введите конечный индекса среза"))
print("Срез inventory[",start,":",finish,"]- это ",end = "")
print(inventory[start:finish])

input("\n Нажмите Enter чтобы продолжить")

chest = ("золото","драгоценные камни")
print("Вы нашли ларец вот что в нем есть")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу")
inventory += chest
print("теперь в вашем распоряжении")
print(inventory)
input("\n Нажмите Enter выйти")