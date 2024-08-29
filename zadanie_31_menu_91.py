from tkinter import *
class Restaurant(Frame):
    def __init__(self,master):
        super(Restaurant,self).__init__(master)
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
              text = "Menu of restaurant",
              ).grid(row = 0 , column = 0, sticky = W)
        row = 1
        for disk,price in self.menu.items():
            var = IntVar()
            self.order[disk] = var
            Checkbutton(self,
                        text = f"{disk} - {price} $",
                        variable = var).grid(row = row , column = 0, sticky = W)
            row += 1
        Button(self,
                   text = "Calculer la facture",
                   command  = self.calcul
                   ).grid(row = row, column = 0 , sticky = W)
        self.result_label = Label(self, text="")
        self.result_label.grid(row= 4, column=0, sticky=W)
    def calcul(self):
        total = 0
        for disk in self.order:
            if self.order[disk].get():
                total += self.menu[disk]
        self.result_label.config(text = f"Total de la facture : {total} $")


root = Tk()
root.title("Restaurant bill")
app = Restaurant(root)
root.mainloop()