#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

import cgi 
from http import cookies
import datetime

args = cgi.parse()

palabrasABC=" "
otras=" "

texto = args["texto"][0]
    #palabras contiene el texto del input separado por espacios
palabras = texto.split(" ")

for palabra in palabras:
    if palabra[0]=="A" or palabra[0]=="a" or palabra[0]=="B" or palabra[0]=="b" or palabra[0]=="C" or palabra[0]=="c":
        palabrasABC += palabra+" "
    else:
        otras += palabra+" "


coki = cookies.SimpleCookie()
    # esta parte solo se ejecuta la primera vez que accede el usuario
coki["empiezaABC"] = palabrasABC
expires = datetime.datetime.utcnow() + datetime.timedelta(days=90)  # expires in 90 days
coki['empiezaABC']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
print(coki)

coki2 = cookies.SimpleCookie()
    # esta parte solo se ejecuta la primera vez que accede el usuario
coki2["otras"] = otras
expires = datetime.datetime.utcnow() + datetime.timedelta(days=90)  # expires in 90 days
coki2['otras']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
print(coki2)

#se pone siempre despues de las cookies 
print("Content-Type: text/plain\n")

