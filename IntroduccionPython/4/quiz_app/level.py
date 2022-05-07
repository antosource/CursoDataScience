def choose_level(n_pregunta, p_level):
    
# Construir lógica para escoger el nivel
   
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta <= p_level *2:
        level = 'intermedias'
    else:
        level = 'avanzadas'
    return level

# Test
if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias
    
    print(choose_level(3, 1)) 
    print(choose_level(2, 1))
    print(choose_level(1, 1))