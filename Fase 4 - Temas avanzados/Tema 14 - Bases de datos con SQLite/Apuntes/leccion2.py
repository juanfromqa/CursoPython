import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE usuarios (
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# usuarios = [
#     ('111111A','Juan Hernandez Sanchez', 30, 'mario@gmail.com'), 
#     ('111111B','Mario Perez Gonzalez', 26, 'mario@gmail.com'),
#     ('111111C','Mercedes Perez Gonzalez', 19, 'mercedes@gmail.com'),
#     ('111111D','Javier Perez Gonzalez', 26, 'javier@gmail.com')
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
# ''')

# productos = [
#     ('Teclado', 'Logitech', 19.95), 
#     ('Pantalla 19"', 'LG', 89.25)    
# ]

# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos) # DE esa manera se llena el dato incremental, asignando null

# cursor.execute("SELECT * FROM productos")
# productos = cursor.fetchall()
# for p in productos:
#     print(p[1])

# utilizar unique para que no sea posible duplicar registros iguales

# cursor.execute('''
#     CREATE TABLE usuarios (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE, 
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

usuarios = [
    ('111111A','Juan Hernandez Sanchez', 30, 'mario@gmail.com'), 
    ('111111B','Mario Perez Gonzalez', 26, 'mario@gmail.com'),
    ('111111C','Mercedes Perez Gonzalez', 19, 'mercedes@gmail.com'),
    ('111111D','Javier Perez Gonzalez', 26, 'javier@gmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)



conexion.commit()
conexion.close()