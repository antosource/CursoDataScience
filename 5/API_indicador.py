import json
import requests

excluir = ['version','autor','fecha']

url = 'https://mindicador.cl/api/'
res = requests.get(url)
data = json.loads(res.text.encode("utf-8"))

#print(data)
#pretty_json = json.dumps(data, indent=2)
#print(f"Largo Diccionario: {len(data)}")

variables = [k for k in data.keys() if k not in excluir]

for v in variables:
  print (f"{v} = {data[v]['valor']}")