from tkinter import *

root = Tk()

root.title("Hola mundo")
# root.resizable(0,0) # Para que no se redimensione
root.iconbitmap('hola.ico')


frame = Frame(root)
#frame.pack(side=BOTTOM, anchor="w") # Alinea los widgets al centro y arriba east, west, south, north
frame.pack(fill='both', expand=1) # para que ocupe todo el tamaño de su contenedor padre
frame.config(width=480, height=420)
frame.config(cursor="pirate") # Cambia el cursor a una calavera en la zona del frame
frame.config(bg="lightblue")
frame.config(bd=15)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

#Abajo del todo
root.mainloop()
root.destroy()  




