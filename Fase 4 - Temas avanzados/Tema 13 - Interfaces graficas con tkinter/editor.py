from tkinter import *
from tkinter import filedialog as FileDilalog
from io import open

ruta = ""

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    # Se le indica que borre desde el caracter 1 hasta el final de todo, el primer caracter es un \n en un Text
    texto.delete(1.0, "end")
    root.title(ruta + "Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDilalog.askopenfilename(
        initialdir="/Users/juan/Documents/CursoPython/CursoPython/Fase 4 - Temas avanzados/Tema 13 - Interfaces graficas con tkinter", filetypes=(("Ficheros de texto", "*.txt"),), title="Abrir un archivo de texto")  # la coma siempre va porque sino lanza error. El punto indica el directorio actual

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")


def guardar():
    mensaje.set("Guardar fichero")
    if ruta is not "":
        contenido = texto.get(1.0, "end-1c") # Sirve para no guardar los saltos de linea una y otra vez
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se guardó correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Guardar como")
    fichero = FileDilalog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension="*.txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c") # Sirve para no guardar los saltos de linea una y otra vez
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se guardó correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


root = Tk()
root.title("Mi editor")

# Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill=BOTH, expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 13))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify=LEFT)
monitor.pack(side=LEFT)
root.config(menu=menubar)

root.mainloop()
root.destroy()
