from os import name
from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()


def test():
    color = ColorChooser.askcolor(title="Elige un color")
    print(color)


def test2():
    ruta = FileDialog.askopenfile(title="Abrir un fichero", initialdir="/Users/juan/Documents/CursoPython/CursoPython/Fase 4 - Temas avanzados/Tema 13 - Interfaces graficas con tkinter",
                                     filetypes=(("Fichero de texto", ".txt"), ("Fichero avanzado", ".txt2"), ("Todos los ficheros", "*")))
    print(ruta.__getattribute__("name"))

def test3():
    # This is to actually save/overwrite an existing document is equivalent to open("ruta", "w") - es decir que elimintará el archivo anterior 
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode = "w", defaultextension="txt")
    if fichero is not None:
        fichero.write("HOLA MUNDO!!!! python es increíble y sencillo de aprender :D")
        fichero.close()

Button(root, text="Da click", command=test).pack()
Button(root, text="Da click", command=test2).pack()
Button(root, text="Da click", command=test3).pack()


root.mainloop()
root.destroy()
