class Player(object):
    def __init__(self,name,score = 0):
        self.name = name
        self.score  = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
        reponse = None
        while reponse not in ("y","n"):
            reponse = input(question).lower()
            return reponse
def ask_number(question,low,high):
        reponse = None
        while reponse not in range(low,high):
            reponse = int(input(question))
        return reponse
if __name__ == "__main__":
    print("Bы запустили этот модуль напрямую. а не импортировали его.")
    input("\n\nHaжмитe Enter. чтобы выйти.")

