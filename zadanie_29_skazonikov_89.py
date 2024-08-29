from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self,
              text="Введите данные для создания нового рассказа",
              ).grid(row=0, column=0, sticky=W)
        Label(self,
              text="Введите имя",
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=2, column=0, sticky=W)

        Label(self,
              text = "фамилия",
              ).grid(row = 1, column = 2 , sticky = W)
        self.family_ent = Entry(self)
        self.family_ent.grid(row=2, column=2, sticky=W)

        Label(self,
              text = "Глагол в инфинитиве:",
              ).grid(row = 1 , column = 3 , sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 2, column = 3 , sticky = W)

        Label(self,
              text= "Прилагательное (-ые):",
              ).grid(row = 4 , column = 0 , sticky = W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text ="нетерпеливый",
                    variable = self.is_itchy
                    ).grid(row = 4 , column = 1, sticky = W)
        self.is_joyeux = BooleanVar()
        Checkbutton(self,
                    text = "радостный",
                    variable = self.is_joyeux
                    ).grid(row = 4, column = 2 , sticky = W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "пронизывающий",
                    variable = self.is_electric
                    ).grid(row = 4, column = 3 , sticky = W)

        Label(self,
              text = "Часть тела:",
              ).grid(row = 5, column = 0 , sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)

        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5 , column = column, sticky = W)
            column += 1

        Button(self,
               text = "Получить рассказ",
               command = self.tell_story
               ).grid(row = 6, column = 0 , columnspan = 4)

        self.story_txt = Text(self,
                              width = 75,
                              height = 10,
                              wrap = WORD)
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)

    def tell_story(self):
        person = self.person_ent.get()
        family = self.family_ent.get()
        verbe = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливое, "
        if self.is_joyeux.get():
            adjectives += "радостное, "
        if self.is_electric.get():
            adjectives += "пронизывающее, "
        body_part = self.body_part.get()
        # Construire l'histoire
        story = "Знаменитый путешественник "
        story += person
        story += " уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города, в котором, по легенде, обитали "
        story += family.title()
        story += ". Но однажды "
        story += family
        story += " и "
        story += person + " столкнулись лицом к лицу. "
        story += "Мощное, "
        story += adjectives
        story += "ни с чем не сравнимое чувство охватило душу путешественника. "
        story += "После стольких лет поисков цель была наконец достигнута. "
        story += person
        story += " ощутил, как на его " + body_part + " скатилась слезинка. "
        story += "И тут внезапно "
        story += family
        story += " перешли в атаку, и "
        story += person + " был ими мгновенно сожран. "
        story += "Мораль? Если задумали "
        story += family
        story += ", надо делать это с осторожностью."
        # вывод рассказа на экран
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)







root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()






