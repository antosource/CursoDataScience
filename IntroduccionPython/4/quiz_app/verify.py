import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas
    #correcto =True if "alt_2" in alternativas[eleccion] else False
    
    if 'alt_2' in alternativas[eleccion]:
        correcto = True
        print (f'Respuesta Correcta {alternativas[eleccion]}')
    else:
        correcto = False
        print(f'Respuesta Incorrecta {alternativas[eleccion]}')
   
    return correcto

# Test
if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
    






