import preguntas as p

def print_pregunta(enunciado, alternativas):
       
    alter = ['A', 'B', 'C','D'] # Listado de alternativas
       
    print(f"{'[, '.join(enunciado)}") 
   
    for k,v in zip(alter,alternativas):
        print(f'{k}. {v[0]}')
    
    #Otra forma de imprimir enunciado y alternativas
    #print(enunciado,
    #f'\nA. {alternativas[0]}\nB. {alternativas[1]}\nC. {alternativas[2]}\nD. {alternativas[3]}')

# Test       
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4