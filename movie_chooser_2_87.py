from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Укажите ваш любимый жанр кино").grid(row=0, column=0, sticky=W)
        Label(self, text="Выберите ровно один:").grid(row=1, column=0, sticky=W)

        self.favorite = StringVar()
        self.favorite.set(None)

        Radiobutton(self, text="Комедия", variable=self.favorite, value="Комедия", command=self.update_text).grid(row=2, column=0, sticky=W)
        Radiobutton(self, text="Драма", variable=self.favorite, value="Драма", command=self.update_text).grid(row=3, column=0, sticky=W)
        Radiobutton(self, text="Кино о любви", variable=self.favorite, value="Кино о любви", command=self.update_text).grid(row=4, column=0, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        message = "Ваш любимый киножанр: "
        message += self.favorite.get()
        self.results_txt.delete(1.0, END)  # Utilisation de 1.0 au lieu de 0.0
        self.results_txt.insert(1.0, message)  # Utilisation de 1.0 au lieu de 0.0

# Création de la fenêtre principale
root = Tk()
root.title("Киноман")
root.geometry("300x200")
app = Application(root)
root.mainloop()
