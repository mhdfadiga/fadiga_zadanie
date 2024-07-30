"""from tkinter import *
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self,
              text= "Укажите ваш~ любимые жанры кино"
              ).grid(row = 0,column = 0 , sticky = W)
        Label(self,
              text= "Выберите все. что вам по вкусу:"
              ).grid(row = 1 , column = 0 , sticky = W)
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                     text = "Комедия",
                     varible = self.likes_comedy,
                     command = self.update_text
                     ).grid(row = 2,colomn = 0 , sticky = W)
        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text= "Драма",
                    variable = self.likes_drama
                    ,command= self.update_text
                    ).grid(row = 3,colomn = 0, sticky = W)
        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text="Фильм о любви",
                    variable = self.likes_romance,
                    command= self.update_text,
                    ).grid(row = 4, colomn = 0, sticky = W)
        self.results_txt = Text(self,width = 40,height = 5 , wrap = WORD)
        self.results_txt.grid(row=5, column = 0,columnspan = 3)

    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self.likes_drama.get():
            likes += "Вас привлекает жанр драмы.\n"
        if self.likes_romance.get():
            likes += "Вам по вкусу кино о любви."
        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,likes)





root = Tk()
root.title("Kинoмaн")
root.geometry("300x150")
app = Application(root)
root.mainloop()
"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self, text="Укажите ваши любимые жанры кино").grid(row=0, column=0, sticky=W)
        Label(self, text="Выберите все, что вам по вкусу:").grid(row=1, column=0, sticky=W)

        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text="Комедия",
                    variable=self.likes_comedy,
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text="Драма",
                    variable=self.likes_drama,
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text="Фильм о любви",
                    variable=self.likes_romance,
                    command=self.update_text,
                    ).grid(row=4, column=0, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self.likes_drama.get():
            likes += "Вас привлекает жанр драмы.\n"
        if self.likes_romance.get():
            likes += "Вам по вкусу кино о любви.\n"

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)


root = Tk()
root.title("Киноман")
root.geometry("300x200")  # Adjusted height for better layout
app = Application(root)
root.mainloop()