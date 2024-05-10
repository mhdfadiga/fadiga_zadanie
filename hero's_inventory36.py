inventory = ()
if  not inventory:
    print("вы безоружны")
input("\n Нажмите Enter чтобы продолжить")
inventory = ("меч","кольцуга"," щит"," целебное снадобье")
print("\nСодержание кортежа:")
print(inventory)
print("\n и так, в вашем арсенале:")
for item in inventory:
    print(item)
input("\n Нажмите Enter чтобы выйтии")
