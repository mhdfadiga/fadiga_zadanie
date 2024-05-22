def display (message):
    print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question):
    """ Задает вопрос с ответом 'да' или 'нет' . """
    reponse = None
    while reponse not  in ('y','n'):
        reponse = input(question).lower()
        return reponse


display("hello fode")
number = give_me_five()
print("Boт что возвратила функция give_me_five() :", number)
answer = ask_yes_no("\nПожалуйста. введите 'у' или 'n': ")
print( "Спасибо. что ввели", answer)
input("\n\nHaжмитe Enter. чтобы выйти.")
