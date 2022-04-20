import random
import sys

jugada = sys.argv[1].lower()
compu = random.choice(['piedra','papel','tijeras'])

if jugada =='piedra' or jugada =='papel'or jugada =='tijeras':
    print(f'Tu jugaste {jugada} \nComputador jugó {compu}') 
    if (jugada=='piedra' and compu=='tijeras') or (jugada=='papel' and compu=='piedra') or (jugada=='tijera' and compu=='papel'):
        print('Ganaste!!!')
    elif jugada == compu:
        print('Empataste')
    else:
        print('Perdiste')
else:
    print('Argumento inválido: Debe ser piedra, papel o tijera.')