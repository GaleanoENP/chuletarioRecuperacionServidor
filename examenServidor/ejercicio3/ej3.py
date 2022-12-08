#!C:\Users\aceru\AppData\Local\Programs\Python\Python310\python.exe

'''

Crear un diccionario de nombre preciosProductosID

Recorrer el diccionario con un foreach para crear una tabla HTML

'''

preciosProductosID = {
    'CA132':99.2,
    'CB231':55.7,
    'CA332':101.0,
    'CB563':65.2,
    'CB838':48.1
}

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
        
    </head>
    <body>
        <table>
            <tr>
                <th>identificador</th>
                <th>precio</th>
            </tr>
''')

total = 0
for elemento in preciosProductosID:
    print('''
            <tr>
                <td>'''+elemento+'''</td>
                <td>'''+str(preciosProductosID[elemento])+'''</td>
            </tr>
         ''')
    total += preciosProductosID[elemento]


print('''
            <tr>
                <td>total</td>
                <td>'''+str(total)+'''</td>
            </tr>
        </table>
    </body>
</html>
''')