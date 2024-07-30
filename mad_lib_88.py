"""from tkinter import*
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text= "Введите данные для создания нового рассказа",
              ).grid(row = 0 , colomn = 0, sticky = W)
        Label(self,
              text= "Имя человека: ",
              ).grid(row = 1, colomn = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, colomn = 1 , sticky = W)

        Label(self,
              text= "Существительное во мн. ч. : ",
              ).grid(row = 2, colomn = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, colomn = 1, sticky = W)

        Label(self,
              text= "Глагол в инфинитиве:"
              ).grid(row = 3, colomn = 0 , sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, colomn = 1, sticky = W )

        Label(self,
              text= "Прилагательное (-ые):",
              ).grid(row = 4 , colomn = 0 , sticky = W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text= "нетерпеливый",
                    variable = self.is_itchy
                    ).grid(row = 4 , colomn = 1 , sticky = W)
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "радостный",
                    variable = self.is_joyous
                    ).grid(row = 4 , colomn = 2 , sticky = W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "пронизывающий",
                    variable = self.is_electric
                    ).grid(row = 4 , colomn = 3 , sticky = W)
        Label(self,
              text = "Body Ра rt:",
              ).grid(row = 5 , colomn = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)

        body_parts = ["пуnок","большой палец ноги","nродолговатый мозг"]
        colomn = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, colomn = colomn, sticky = W)
            colomn += 1

            Button(self,
                   text = "Получить рассказ",
                   command = self.tell_story
                   ).grid(row = 6 , colomn = 0 , colomnspan = 4)
            def tell_story(self):
                person = self.person_ent.get()
                noun = self.noun_ent.get()
                verb = self.verb_ent.get()
                adjectives = ""
                if self.is_itchy.get():
                    adjectives += "радостное. "
                if self.is_electric.get():
                    adjectives +=  "пронизывающее. "
                body_parts = self.body_part.get()

                story = "Знаменитый путешественник"
                story += person
                story += " уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города. в котором. по легенде. обитали "
                story += noun.title()
                story += ". Но однажды "
                story += ". Но однажды "
                story += noun
                story += " и "
                story += person + " столкнулись лицом к лицу. "
                story += "Мощное. "
                story += adjectives
                story += "ни с чем не сравнимое чувство охватило душу путешественника."
                story += "После стольких лет поисков цель была наконец достигнута. "
                story += person
                story += " ощутил. как на его " + body_parts + " скатилась слезинка. "
                story += "И тут внезапно "
                story += noun
                story += " перешли в атаку. и "
                story += person + " был ими мгновенно сожран."
                story += "Мораль? Если задумали "
                story += verb
                story += ". надо делать это с осторожностью."
                self.story_txt.delete(0.0,END)
                self.story_txt.insert(0.0,story)

root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()
"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Введите данные для создания нового рассказа",
              ).grid(row=0, column=0, sticky=W)

        Label(self,
              text="Имя человека: ",
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        Label(self,
              text="Существительное во мн. ч. : ",
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Глагол в инфинитиве:"
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        Label(self,
              text="Прилагательное (-ые):",
              ).grid(row=4, column=0, sticky=W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text="нетерпеливый",
                    variable=self.is_itchy
                    ).grid(row=4, column=1, sticky=W)
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="радостный",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="пронизывающий",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)

        Label(self,
              text="Часть тела:",
              ).grid(row=5, column=0, sticky=W)
        self.body_part = StringVar()
        self.body_part.set(None)

        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part
                        ).grid(row=5, column=column, sticky=W)
            column += 1

        Button(self,
               text="Получить рассказ",
               command=self.tell_story
               ).grid(row=6, column=0, columnspan=4)

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливое, "
        if self.is_joyous.get():
            adjectives += "радостное, "
        if self.is_electric.get():
            adjectives += "пронизывающее, "
        body_part = self.body_part.get()

        # Construire l'histoire
        story = "Знаменитый путешественник "
        story += person
        story += " уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города, в котором, по легенде, обитали "
        story += noun.title()
        story += ". Но однажды "
        story += noun
        story += " и "
        story += person + " столкнулись лицом к лицу. "
        story += "Мощное, "
        story += adjectives
        story += "ни с чем не сравнимое чувство охватило душу путешественника. "
        story += "После стольких лет поисков цель была наконец достигнута. "
        story += person
        story += " ощутил, как на его " + body_part + " скатилась слезинка. "
        story += "И тут внезапно "
        story += noun
        story += " перешли в атаку, и "
        story += person + " был ими мгновенно сожран. "
        story += "Мораль? Если задумали "
        story += verb
        story += ", надо делать это с осторожностью."
        # вывод рассказа на экран
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,story)

# Créer et lancer l'application
root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()