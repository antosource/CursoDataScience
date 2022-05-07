import requests
import json

def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ == "__main__":
    url = 'https://aves.ninjas.cl/api/birds'
    response = request_get(url)
    print(len(response))