#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ejercicio6",
    password="ejercicio6",
    database="ejercicio6"
)

print("Content-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Listado de libros prestados</h1>""")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM socios ORDER BY id")

listaSocios = mycursor.fetchall()

for socios in listaSocios:
    print("<hr><h4>",socios[1],"ha recibido en prestamo:</h4>")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM libros WHERE id_socio="+str(socios[0]))
    listaLibros = mycursor.fetchall()
    for libros in listaLibros:
        print("<p>",libros[1],"de: "+str(libros[2])+"</p>")

print("""
</body>
</html>""")
