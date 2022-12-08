#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

numeros = {
    'primero':1.0,
    'segundo':3.0,
    'tercero':5.0,
    'cuarto':7.0,
    'quinto':9.0
}

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
    
    </head>
    <body>
        <table>
''')    


for x in reversed(numeros):
    print('''
        <tr>
            <th>'''+str(numeros[x])+'''
            </th>
         </tr>
        ''')

print('''
        </table>
    </body>
</html>
''')
