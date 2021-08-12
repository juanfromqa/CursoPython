from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()

n1 = StringVar()
n2 = StringVar()
r = StringVar()
Label(root, text="Numero 1").pack()
Entry(root, justify=CENTER, textvariable=n1).pack()
Label(root, text="Numero 2").pack()
Entry(root, justify=CENTER, textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify=CENTER, textvariable=r, state="disabled").pack()

Button(root, text="+", command=sumar).pack(side=LEFT)
Button(root, text="-", command=restar).pack(side=LEFT)
Button(root, text="*", command=producto).pack(side=LEFT)





root.mainloop()
root.destroy()