"""
Доработайте функцию ask_numЬer() так, чтобы ее можно было вызывать еще с одним параметром -
кратностью (величиной шага). Сделайте шаг по умолчанию равным 1.
Доработайте игру «Опадай число» из главы З так, чтобы в ней нашла применение функция ask_number().
Доработайте новую версию игры «Опадай число» (которую вы создали, решая предыдущую задачу) так, чтобы
основная часть программы стала функцией main(). Для того чтобы игра началась, не забудьте вызвать эту
функцию глобально.
Напишите такую функцию computer_move(), которая сделала бы стратегию компьютера безупречной.
Проверьте, можно ли создать непобедимого противника.
"""
import random
X = "X"
O = "O"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9

def display_instruct():
    print(
        """
        Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен 
        твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики 
        Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям 
доски - так. как показано ниже: 
    0 | 1 | 2 
    3 | 4 | 5 
    6 | 7 | 8 
Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сражение. \n 
        """
    )
def ask_yes_no(question):
    """Задает вопрос с ответом 'Да' или 'Нет'."""
    reponse = None
    while reponse not in ("y","n"):
        reponse = input(question).lower()
        return reponse
def ask_number(question,low,high,step = 1):
    reponse = None
    while reponse not in range(low,high,step):
        reponse =int(input(question))
    return reponse
def computer_move(low,high):
    return (low + high)//2
def main():
    print("\t Доброе пожаловать в игру 'угадай число'!")
    print("\nя загадал некорое число в диапазоне от 1 до 100")
    print("постарайтесь угадать его за минимальное количество попыток\n")
    the_number = random.randint(1,100)
    guess = ask_number("ваша попытка:",1,101)
    tries = 1
    while guess != the_number:
        if guess > the_number:
            print("Меньше")
        else:
            print("Болше")
        guess = ask_number("ваша попытка:",1,101)
        tries += 1

    print("Поздравляю! вы угадали число! это действителтно",the_number)
    print("вы затратили на это",tries,"попыток\n")


if __name__ == '__main__':
    main()

def pieces():
    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")
    if go_first == "y":
        print("nHy что ж. даю тебе фору: играй крестиками.")
        human = X
        computer = O
    else:
        print("\nTвoя удаль тебя погубит. Буду начинать я.")
        computer = X
        human = O
        return computer,human
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
def display_board(board):
    print("\n\t",board[O],"|",board[1],"|",board[2])
    print("\t","---------")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t","---------")
    print("\t",board[6],"|",board[7],"|",board[8],"\n")

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
        return moves
def winner(board):
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None
def human_move(board,human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move =ask_number("Tвoй ход. Выбери одно из полей (О - 8):",O,NUM_SQUARES)
        if move not in legal:
             print("\nCмeшнoй человек! Это поле уже занято. Выбери дpyroe.\n")
    print("Ладно ... ")
    return move
def computer_move(board,computer,human):
    board = board[:]
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
print("Я выберу поле номер", end=" ")
def next_turn(turn):
        if turn == X:
            return O
        else:
            return X

def congrat_winner(the_winner,computer,human):

    if the_winner != TIE:
        print("Tpи",the_winner,"в ряд!\n")
    else:
        print("Hичья!\n")
    if the_winner == computer:
        print("Kaк я и предсказывал. победа в очередной раз осталась за м~ой. \n"  \
              "Вот еще один довод в пользу того. что компьютеры превосходят людей решительново всем.")
    elif the_winner == human:
        print("O нет. этого не может быть! Неужели ты как-то сумел перехитрить меня.белковый? \n " \
              " Клянусь: я.компьютер.недопущу этого больше никогда!")
    elif the_winner == TIE:
        print("Teбe несказанно повезло. дружок: ты сумел свести игру вничью. \n" \
              "Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить. ")
def main():
    display_instruct()
    computer = pieces()
    human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner,computer,human)

main()
input("\n\пНажмите Enter. чтобы выйти.")















