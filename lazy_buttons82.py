from tkinter import*
root = Tk()
root.title("Бесполезные кнопки")
root.geometry("200x85")
app = Frame(root)
app.grid()

bttn1 = Button(app,text = "Я ничего не делаю")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text= "И я тоже")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И Я!"
root.mainloop()