from tkinter import *


def hola():
    print("Hola Mundo")

def crear_label():
    Label(root, text="Label Creada dinámicamente").pack()



root = Tk()

Button(root, text="Da click", command=crear_label).pack()


root.mainloop()
root.destroy()