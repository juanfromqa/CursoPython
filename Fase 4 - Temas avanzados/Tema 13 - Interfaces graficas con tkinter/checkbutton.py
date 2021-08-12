from tkinter import *

def seleccionar():
    cadena = ""
    if(leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    if(azucar.get()):
        cadena += " Con azucar"
    else:
        cadena += " Sin azucar"
    
    monitor.config(text=cadena)

root = Tk()

root.title("Cafetería")
root.config(bd=15)

# para almacenrar las dos variables
leche = IntVar() # 1 = si, 0 = no
azucar = IntVar() # 1 = si, 0 = no

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

frame = Frame(root)
frame.pack(side=LEFT)

Label(frame, text="¿Como quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azucar", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

# para mostrar el texto
monitor = Label(frame)
monitor.pack()

root.mainloop()
root.destroy()