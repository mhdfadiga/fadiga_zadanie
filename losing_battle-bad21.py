print("Baшeгo героя окружила огромная армия троллей.")
print("Одинокий герой достает меч из ножен . готовясь к последней битве в своей жизни.\n")
health = 10
trolls = 0
damage = 3
while health != 0 :
    trolls += 1
    health -= damage
    print("Взмахнув мечом. ваш герой истребляет злобного тролля." 
      "но сам получает повреждений на",damage, "очков .\n")
print("Ваш герой доблестно сражался и убил" ,trolls,"троллей.")
print("Ho увы! Он пал на поле боя ")
input("\n\nHaжмитe Enter. чтобы выйти ")