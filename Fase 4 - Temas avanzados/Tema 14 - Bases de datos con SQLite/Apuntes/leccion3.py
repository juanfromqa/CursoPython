import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios WHERE edad = 27")

usuarios = cursor.fetchall()
print(usuarios)

#cursor.execute("UPDATE usuarios SET nombre = 'Hector Gomez', edad = 30 WHERE dni = '111111B'")
cursor.execute("DELETE FROM usuarios WHERE dni = '111111B'") # NO OLVIDAR EL WHERE en los DELETE y UPDATES


conexion.commit()
conexion.close()