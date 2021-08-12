from tkinter import *
# Con este archivo se puede ejecutar un lienzo con grids para capturar datos desde una UI
root = Tk()


label = Label(root, text="Nombre de la persona")
label.grid(row=0, column=0, padx=5,pady=5) # En lugar de usar pack se usa grid para tener una cuadricula disponible 

entry = Entry(root)
entry.grid(row=0, column=1, padx=5,pady=5)
entry.config(justify=RIGHT)


label2 = Label(root, text="Apellido")
label2.grid(row=1, column=0,sticky="w", padx=5,pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5,pady=5)
entry2.config(justify=LEFT)

label3 = Label(root, text="Deshabilitado")
label3.grid(row=2, column=0,sticky="w", padx=5,pady=5)

entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=5,pady=5)
entry3.config(justify=CENTER, state="disabled")


label4 = Label(root, text="Password")
label4.grid(row=3, column=0,sticky="w", padx=5,pady=5)

entry4 = Entry(root)
entry4.grid(row=3, column=1, padx=5,pady=5)
entry4.config(justify=RIGHT, show="*")


root.mainloop()
root.destroy()