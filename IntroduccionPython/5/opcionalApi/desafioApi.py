import os
import sys
import requests
import json

url ='https://reqres.in/api/users'

def req(tipo, url, data={}):
   response=requests.request (tipo, url=url, data=data)
   return json.loads(response.text)

def del_req(url, id):  # Se ingresa url e indica si lo elimino o no
    url = url + f'/{id}'
    print(url)
    return requests.request('DELETE', url=url)

op_sys = 'cls' if sys.platform == 'win32' else 'clear'
os.system(op_sys)

#Obtenga GET
print('*** Uso de GET ***')
users_data = req('GET', url) 
print (users_data)

#Cree POST
print(f"\n*** Uso de POST ***")
post_data = {"first_name": "Ignacio",
             "job" : "Profesor"}
created_user = req('POST', url, data=post_data)
print (created_user)

#Actualice PUT
print(f"\n*** Uso de PUT ***")
put_data = {
    "name" : "Morpheus",
    "job" : "Zion resident"
}
update_user = req('PUT', url+'/2', data=put_data)
print(update_user)

#Elimine DELETE
print(f"\n*** Uso de DELETE ***")
d = users_data['data']
id = [elemento['id'] for elemento in d if elemento['first_name']=='Tracey'] # con list comprehesion

print(f"Respuesta del servidor: {del_req(url, id[0])}\n")