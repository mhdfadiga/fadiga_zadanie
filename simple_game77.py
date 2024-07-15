import game_76,random
print("Дoбpo пожаловать в самую-самую простую игру!\n")
again = None
while again != "n":
    players = []
    num = game_76.ask_number(question = "Сколько игроков участвует?(2-5):",low = 2, high = 5)
    for i in range(num):
        name = input("имя игрока")
        score = random.randrange(100) + 1
        player = game_76.Player(name,score)
        players.append(player)
        print("\nBoт результаты игры:")
        for player in players:
            print(player)

        again = game_76.ask_yes_no("\nХотите сыграть еще раз? (y/n): ")
input("\n\nHaжмитe Еntеr.-чтобы выйти.") 