
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
payload = {}
headers = {}

response = requests.request('GET', url, headers=headers, data=payload)
print (response)
print (payload)
print (headers)