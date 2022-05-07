import preguntas as p
import random

def shuffle_alt(pregunta):
    #mezclar alternativas
    random.shuffle(pregunta['alternativas']) #Random busca cualquier pregunta y alguna alternativa (llave)
    
    return pregunta['alternativas']

#Test
if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]