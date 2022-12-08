#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

'''

Crear una funcion de nombre concatenaVocales.

Recibe un parametro con el nombre letras, es una lista.

Comprobar que tiene una longitud de 5 o menos

Devolver las letras concatenadas como un string.

'''

def concatenaVocales(letras):
    salida=""
    if len(letras) > 5:
        return 'error'

    for i in letras:
        if(i!= 'A') and (i!= 'E') and (i!= 'I') and (i!= 'O') and (i!= 'U'):
            return 'error'
        salida += i

    return salida

print("Content-Type: text/plain\n")

print(concatenaVocales(['A','U']))
print(concatenaVocales(['E','U','A','I','O']))
print(concatenaVocales(['b','A','I','O']))
print(concatenaVocales(['E','U','A','I','O','I','O']))
