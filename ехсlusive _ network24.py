print("\t\tЭксклюзивная компьютерная сеть")
print("\t\tТoлькo для зарегистрированных пользователей!\n")
securite = 0
username = ''
while  not username :
    username = input("login:")
password = ''
while not password:
    password = input("password:")
if username == "M .Dawson" and password == "secret":
    print("Привет. Майк ")
    securite = 5
elif username == "S.Meier" and password == "civilization":
    print("Здравствуй. Сид.")
    securite = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Дoбporo времени суток. Сигеру.")
    securite = 3
elif username == "W.Wright" and password == "thesims":
    print("Kaк дела. Уилл?")
    securite = 3
elif username == "guest" and password == "guest":
    print("Дoбpo пожаловать к нам в гости.")
    securite = 1
else:
    print("Войти в систему не удалось. Должно быть. вы не очень-то эксклюзивный гражданин. \n")
input("\n\nHaжмитe Enter. чтобы выйти.")