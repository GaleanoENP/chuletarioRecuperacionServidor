#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

import cgi
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ejercicio6",
    password="ejercicio6",
    database="ejercicio6"
)

args = cgi.parse()

socio=""
titulo=""
autor=""

socio = args["socio"][0]
titulo = args["titulo"][0]
autor = args["autor"][0]

noVacio=False
usuario=False

print("Content-Type: text/plain\n")

if socio!=" " and titulo!=" " and autor!=" ":
    noVacio=True

if noVacio:
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM socios")

    lista = mycursor.fetchall()
    for socios in lista:
        if socios[1]==socio: #str(socios[1]).lower()==socio.lower() para que no importe mayusc o minusc
            usuario=True
            idSocio=socios[0]

if usuario:
    sql = "INSERT INTO libros (titulo, autor, id_socio) VALUES (%s, %s, %s)"
    valores=(titulo,autor,idSocio)
    mycursor.execute(sql, valores)
    mydb.commit()
    print("Libro prestado")
else:
    print("El usuario no existe")