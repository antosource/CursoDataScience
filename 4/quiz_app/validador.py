def validate(opciones, eleccion):
   
    while eleccion not in opciones: # Se pueden colocar condiciones logícas 
        eleccion = input(f'"{eleccion}" No es una opción Válida, \nIngrese una de las opciones válidas: {opciones} ->').lower()   
    return eleccion

'''
En Opciones se puede ingresar una lista y eleccion es la opcion a validar 
'''
#Test
if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)