import sqlite3

conexion = sqlite3.connect("ejemplo.db")

# Cursos que se ocupa para trabajar con bd 
cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
# cursor.execute("INSERT INTO usuarios VALUES('Juan Hernandez Sanchez',30,'juanito@gmail.com')")
# cursor.execute("SELECT * FROM usuarios")
# Para usarlo como objeto
# usuario = cursor.fetchone()
# print(usuario[0])
# Si se vuelve a ejecutar el fetchone, comienza desde el siguiente elemento
# usuario = cursor.fetchone()

# usuarios = [ 
#     ('Mario Perez Gonzalez', 26, 'mario@gmail.com'),
#     ('Mercedes Perez Gonzalez', 19, 'mercedes@gmail.com'),
#     ('Javier Perez Gonzalez', 26, 'javier@gmail.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for u in usuarios:
    print(u[0])

conexion.commit()
conexion.close()
