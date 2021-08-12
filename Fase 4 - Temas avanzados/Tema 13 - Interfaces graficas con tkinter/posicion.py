from tkinter import *

root = Tk()

# Variables dinamicas

texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="Hola Mundo de Python").pack(anchor="nw")
etiqueta = Label(root, text="Otra etiqueta")#esta fdorma no es muy acertada
etiqueta.pack(anchor="center")
etiqueta.config(bg='green')
etiqueta.config(font=("Verdana", 20))
Label(root, text="Hola Mundo de Python").pack(anchor="sw")

etiqueta.config(textvariable=texto)

root.mainloop()
root.destroy()