#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

'''

Crear un html con:
20 * div -> img

//¡'div id="contenedor1"
    img src="coche1.png" img="imagen de coche 1"

'''

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
    
    </head>
    <body>
''')

for x in range(1,21):
    print('''
            <div id="contenedor'''+str(x)+'''">
                <img src="img/coche'''+str(x)+'''.png" alt="imagen de coche''',x,'''">
             </div>
         ''')


print('''
    </body>
</html>
''')

