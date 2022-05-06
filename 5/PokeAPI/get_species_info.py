from get_module import get_info
import random

def get_species(name):
  
    url = f'https://pokeapi.co/api/v2/pokemon-species/{name}'
    data = get_info(url)
    lema =[i['flavor_text'] for i in data['flavor_text_entries'] if i['language']['name'] == 'es']
    previo = data['evolves_from_species']['name'] if data['evolves_from_species']!=None else "No Tiene"
    if data['is_baby']: tipo_esp = 'bebé'
    elif data['is_legendary']: tipo_esp = 'Legendario'
    elif data['is_mythical']: tipo_esp = 'Mitico'
    else : tipo_esp =''
    
    base_species={
        'descr': random.choice(lema),
        'previo': previo,
        'tipo_esp':tipo_esp}
            
    return base_species

if __name__ == '__main__':
    name = 'mewtwo'
    print(get_species(name))