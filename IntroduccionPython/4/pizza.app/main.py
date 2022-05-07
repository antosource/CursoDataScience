from masa import tipo_masa
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from show import mostrar_ingredientes
from tiempo import estimar_tiempo

import sys
import os

clear ='cls' if sys.platform == 'win32' else 'clear'


ingredientes_orden = {'masa': 'Masa Tradicional',
'salsa': 'Salsa de Tomate',
'ingredientes': ['Queso']
}

while True:
    opcion = input('''¿Qué desea realizar?
    1. Cambiar tipo de Masa
    2. Cambiar tipo de Salsa
    3. Agregar Ingredientes
    4. Eliminar Ingredientes
    5. Ordenar con los Ingredientes Actuales
    0. Consultar ingredientes de la pizza
    Otro Número cancelará el pedido.
    > ''')

    if opcion == '1':
        eleccion = input("""Escoja el tipo de Masa:
        T). Masa Tradicional
        D). Masa Delgada
        B). Masa con Bordes de Queso
        > """).upper()
        ingredientes_orden = tipo_masa(ingredientes_orden, eleccion)

    elif opcion == '2':
        eleccion = input('''Seleccione su tipo de Salsa:
        T). Salsa de Tomate
        A). Salsa Alfredo
        B). Salsa Barbecue
        P). Salsa Pesto
        > ''').upper()
        ingredientes_orden = tipo_salsa(ingredientes_orden, eleccion)
        
    elif opcion == '3':
        eleccion = int(input('''Seleccione su Ingrediente:
        1). Tomate
        2). Champiñones
        3). Aceituna
        4). Cebolla
        5). Pollo
        6). Jamón
        7). Carne
        8). Tocino
        9). Queso
        > '''))
        ingredientes_orden = agregar_ingrediente(ingredientes_orden,eleccion)
        
    elif opcion == '4':
        eleccion = int(input('''Seleccione qué ingrediente quitar:
        1). Tomate
        2). Champiñones
        3). Aceituna
        4). Cebolla
        5). Pollo
        6). Jamón
        7). Carne
        8). Tocino
        9). Queso
        > '''))
        ingredientes_orden = quitar_ingrediente(ingredientes_orden, eleccion)
        
    elif opcion == '5':
        tiempo = estimar_tiempo(ingredientes_orden)
        print(f'Su Pizza estará lista en {tiempo} minutos')
        ordenar = input('Desea ordenar ahora S/N: ').upper()
        
        if ordenar == 'S':
            print('Gracias por ordenar en Pizza JAT')
            print('Disfrute su Pizza')
            exit()
            
    elif opcion == '0':
        mostrar_ingredientes(ingredientes_orden)  
        
    else:
        print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
        exit() 