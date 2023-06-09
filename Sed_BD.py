import requests
import json
from urllib.request import urlopen

# Obtener
url = 'https://api.ipify.org?format=json'
response = urlopen(url)
data = json.load(response)
extract = data['ip']

# Actualizar la base de datos en Firebase
firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
response = requests.get(firebase_url)
existing_data = json.loads(response.content)

if existing_data and 'ips' in existing_data:
    if extract not in existing_data['ips']:
            existing_data['ips'].append(extract)
            response = requests.put(firebase_url, json=existing_data)

    else:
         exit
        #  exit("")
        # existing_data['ips'] = [extract]
else:
    new_data = {'ips': [extract]}
    response = requests.put(firebase_url, json=new_data)
    # print('La dirección IP se almacenó correctamente.')
   
# if response.status_code == 200:
#     print("se agregó correctamente en la base de datos Firebase.")
# else:
#     print("Ocurrió un error en la base de datos Firebase.")