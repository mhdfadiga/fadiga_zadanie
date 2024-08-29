"""import tkinter as tk
from tkinter import messagebox
import random


class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Игра: Отгадай число")

        self.target_number = random.randint(1, 100)
        self.attempts = 0

        tk.Label(master, text="Я загадал число от 1 до 100. Попробуйте угадать!").pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        tk.Button(master, text="Угадать", command=self.check_guess).pack(pady=10)
        tk.Button(master, text="Сбросить", command=self.reset_game).pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                messagebox.showwarning("Предупреждение", "Введите число от 1 до 100.")
            elif guess < self.target_number:
                messagebox.showinfo("Результат", "Слишком низко! Попробуйте снова.")
            elif guess > self.target_number:
                messagebox.showinfo("Результат", "Слишком высоко! Попробуйте снова.")
            else:
                messagebox.showinfo("Поздравляем!",
                                    f"Вы угадали число {self.target_number} за {self.attempts} попыток!")
                self.reset_game()
        except ValueError:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите целое число.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
"""
from tkinter import *


class Restaurant(Frame):
    def __init__(self, master):
        super(Restaurant, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.menu = {
            "Pasta": 200,
            "Pizza": 300,
            "Salade": 150,
            "Soupe": 100,
            "Dessert": 150
        }
        self.order = {}

        Label(self,
              text="Menu of restaurant",
              ).grid(row=0, column=0, sticky=W)

        row_number = 1
        for dish, price in self.menu.items():
            var = IntVar()
            self.order[dish] = var
            Checkbutton(self,
                        text=f"{dish} - {price} $",
                        variable=var).grid(row=row_number, column=0, sticky=W)
            row_number += 1

        Button(self,
               text="Calculer la facture",
               command=self.calcul
               ).grid(row=row_number, column=0, sticky=W)

        # Label for displaying the result
        self.result_label = Label(self, text="")
        self.result_label.grid(row=row_number + 1, column=0, sticky=W)

    def calcul(self):
        total = 0
        for dish in self.order:
            if self.order[dish].get():
                total += self.menu[dish]
        self.result_label.config(text=f"Total de la facture : {total} $")


root = Tk()
root.title("Restaurant bill")
app = Restaurant(root)
root.mainloop()