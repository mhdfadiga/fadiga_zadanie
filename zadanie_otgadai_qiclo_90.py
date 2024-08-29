from tkinter import *
import random


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.reset_game()

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label = Label(self,
                                  text="Я загадал число от 1 до 100. Попробуйте угадать!")
        self.result_label.grid(row=0, column=0, sticky=W)

        self.number_ent = Entry(self)
        self.number_ent.grid(row=1, column=0)

        Button(self,
               text="Угадать",
               command=self.check_guess
               ).grid(row=2, column=0)
        Button(self,
               text="Сбросить",
               command=self.reset_game
               ).grid(row=3, column=0)

    def check_guess(self):
        try:
            guess = int(self.number_ent.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="Введите число от 1 до 100.")
            elif guess < self.target_number:
                self.result_label.config(text="Слишком низко! Попробуйте снова.")
            elif guess > self.target_number:
                self.result_label.config(text="Слишком высоко! Попробуйте снова.")
            else:
                self.result_label.config(
                    text=f"Поздравляем! Вы угадали число {self.target_number} за {self.attempts} попыток!")
                self.number_ent.delete(0, END)  # Efface l'entrée après avoir gagné
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите целое число.")


root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()



