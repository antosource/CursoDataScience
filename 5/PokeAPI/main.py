from poke_validation import validate
from show import show_pics

from get_base_info import get_base_pokemon
from build_pokemon_html import build_html
import data as d

import time

while True:
    opcion = input(d.mensaje_opcion)
    opcion = int(validate(opcion,['0','1','2'], mensaje = d.validacion_opcion))
    
    if opcion == 1:
        pokemon = input(d.mensaje_pokedex).lower()
        pokemon = validate(pokemon)  
        
        base_info = get_base_pokemon(pokemon)
        
        html = build_html(base_info)
        
        show_pics(html,'pokedex')
    else :
        break    
        
