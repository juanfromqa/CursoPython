from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()


def test():
    MessageBox.showinfo("Esto es un popup","Hola mundo - INFO")

def test2():
    MessageBox.showwarning("Esto es un popup","ALERTA!")

def test3():
    MessageBox.showerror("Esto es un popup","ERROR!")

def test4():
    resultado = MessageBox.askquestion("Si / No", "¿Estas seguro de que deseas salir?")
    if resultado == "yes":
        root.destroy()

def test5():
    resultado = MessageBox.askokcancel("Aceptar / Cancelar", "¿Sobreescribir el fichero actual?")
    if resultado:
        root.destroy()

def test6():
    resultado = MessageBox.askyesno("Yes/No - Boolean", "¿Estas seguro de que deseas salir?")
    if resultado:
        root.destroy()

def test7():
    resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
    if resultado:
        root.destroy()

Button(root, text="Da click", command=test).pack()
Button(root, text="Da click", command=test2).pack()
Button(root, text="Da click", command=test3).pack()
Button(root, text="Da click", command=test4).pack()
Button(root, text="Da click", command=test5).pack()
Button(root, text="Da click", command=test6).pack()
Button(root, text="Da click", command=test7).pack()

root.mainloop()
root.destroy()