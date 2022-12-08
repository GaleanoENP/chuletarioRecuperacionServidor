#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

from http import cookies
import os

#esto se copia y se pega
todasCokis={} #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>""")
print("<p>Palabras que empiezan por ABC:",todasCokis["empiezaABC"],"</p>")
print("<p>Palabras que no empiezan por ABC:",todasCokis["otras"],"</p>")

print("""
</body>

</html>""")