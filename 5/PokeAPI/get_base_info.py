from get_module import get_info

'''
#Pruebas Previas
name = 'bulbasaur'
url = f'https://pokeapi.co/api/v2/pokemon/{name}'
data = get_info(url)

keys= data.keys()

name = data['name']
id = data['id']
img = data['sprites']['other']['official-artwork']['front_default']
stats = [[elemento['stat']['name'],elemento['base_stat']] for elemento in data['stats']]
tipo = [elemento['type'] for elemento in data['types']]
'''

def get_base_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    data = get_info(url)
    base_info ={
        'name' : data['name'],
        'id' : data['id'],
        'img': data['sprites']['other']['official-artwork']['front_default'],
        'stats': [[elemento['stat']['name'],elemento['base_stat']] for elemento in data['stats']],
        'tipo': [elemento['type'] for elemento in data['types']]
        }
    return base_info

if __name__ == '__main__':
    name = 'pikachu'
    print(get_base_pokemon(name))
    