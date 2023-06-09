import requests
import json

# Obtener los datos de las IPs desde la API de Firebase
firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
response = requests.get(firebase_url)
data = json.loads(response.content)

# Verificar si existen IPs en la respuesta
if data and 'ips' in data:
    ips = data['ips']

    # Generar el contenido HTML con las IPs
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bases de Datos Ip</title>
    </head>
    <body style="background-color: black;">
        <h1 style="color: red;">IPs almacenadas en la base de datos</h1>
        <ul>
    '''

    for ip in ips:
        html_content += f'<li style="color: green;">{ip}</li>'

    html_content += '''
        </ul>
    </body>
    </html>
    '''

    # Guardar el contenido HTML en un archivo
    with open('ips.html', 'w') as file:
        file.write(html_content)

    print("El archivo HTML 'ips.html' se generó correctamente.")

else:
    print("No se encontraron IPs en la base de datos.")

