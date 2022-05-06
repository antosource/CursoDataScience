from get_module import get_info

def get_types_info(lista):
    damage_relations={'double_damage_to':[],'double_damage_from':[],
    'half_damage_to':[],'half_damage_from':[],'no_damage_to':[],'no_damage_from':[] }

    for tipo in lista:
        url = f'https://pokeapi.co/api/v2/type/{tipo}'
        data = get_info(url)
        #super_ef+=([i['name'] for i in data['damage_relations']['double_damage_to'] ])
        for relations in damage_relations:
            damage_relations [f'{relations}']= list(set(damage_relations[f'{relations}'] + ([i['name'] for i in data['damage_relations'][f'{relations}'] ])))
      
    return (damage_relations)

if __name__ == '__main__':
    name = ('fire','flying')
    rel = get_types_info(name)
    print (f"Super efectivo contra: {rel['double_damage_to']}")