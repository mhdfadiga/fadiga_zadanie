def  read_global():
    print("В области видимости функции read_global () значение value1 равно",value)
def shadow_global():
    value = - 10
    print("В области видимости функции read_global () значение value2 равно",value)
def change_global():
    global value
    value = - 10
    print("B области видимости функции change_global() значение value3 равно", value)

value = 10
print("B глобальной области видимости значение переменной value сейчас стало равным",value,"\n")
read_global()
print("Вернемся в глобальную область видимости. Здесь va 1 ue по-прежнему равно",value, "\n")
change_global()
print("Bepнeмcя в глобальную область видимости. Значение value изменилось на",value)
input("\n\nHaжмитe Enter. чтобы выйти.")