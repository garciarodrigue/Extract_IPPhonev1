import requests
import json
from urllib.request import urlopen

# Obtener la IP pública
url = 'https://api.ipify.org?format=json'
response = urlopen(url)
data = json.load(response)
ip_publica = data['ip']

# Actualizar la base de datos en Firebase
firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
response = requests.get(firebase_url)
existing_data = json.loads(response.content)

if existing_data:
    if 'ips' in existing_data:
        if ip_publica not in existing_data['ips']:
            existing_data['ips'].append(ip_publica)
    else:
        existing_data['ips'] = [ip_publica]
else:
    existing_data = {'ips': [ip_publica]}

response = requests.put(firebase_url, json=existing_data)

if response.status_code == 200:
    print("La IP se agregó correctamente en la base de datos Firebase.")
else:
    print("Ocurrió un error al agregar la IP en la base de datos Firebase.")