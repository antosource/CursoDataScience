import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
   alter = ['A', 'B', 'C','D']
   index = list({k for k,v in alternativas})
    
   print(f"{'[, '.join(enunciado)}")
   
   for i in alter:
    print(f"{i}. {index[alter.index(i)]}")
            
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4