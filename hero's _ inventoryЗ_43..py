inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("\nИтaк. в вашем арсенале:")
for item in inventory:
    print(item)
input("\nНажмите Enter. чтобы продолжить.")

print("Сейчас в вашем распоряжении", len( inventory), "предмета/-ов. ")
input("\nНажмите Enter. чтобы продолжить.")

if "целебное снадобье" in inventory:
    print("Bы еще поживете и повоюете.")

index =int(input("\nBвeдитe индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится",inventory[index])

start = int(input("\nBвeдитe начальный индекс среза: "))
finish = int(input("Bвeдитe конечный индекс среза: "))
print("срез inventory[",start,":",finish,"]-это ", end="")
print(inventory[start:finish])
input("\nНажмите Enter. чтобы продолжить.")

chest = ["золото","драгоценные камн"]
print("Bы нашли ларец. Вот что в нем есть:")
print(chest)
print("Bы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)
input("\n\nHaжмитe Enter. чтобы продолжить.")

print("Bы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Teпepь ваш арсенал содержит следующие предметы:")
print(inventory)
input("\nНажмите Enter. чтобы продолжить.")

print("Зa золото и драгоценные камнV: вы купили магический кристалл. способный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print("Teпepь в вашем распоряжении:")
print(inventory)
input("\nНажмите Enter. чтобы продолжить.")

print("Bopы лишили вас арбалета и кольчуги.")
del inventory[:2]
print("B арсенале теперь только:")
print(inventory)
input("\п\пНажмите Enter. чтобы выйти.")
