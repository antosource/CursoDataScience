import requests
import json

#verificar token

#autentificar

#publicar



def reqPost(url, json={}):
   response=requests.request (url=url, data=data)
   return json.loads(response.text)



url = 'https://conexiones.sma.gob.cl/api/v1/'
auth_data = {"usuario":"96989120-4","password":"QI}|3)g_0)"}

resp = requests.post(url+'auth', json=auth_data)
print (resp.json())
