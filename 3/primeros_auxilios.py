import itertools

titulo = 'Guía Primeros Auxilios'
respTrue = ['si','s','yes','ok'] #Lista respuestas Verdaderas
respFalse = ['no','n','not','nop'] #Lista respuestas falsas
salir = True
def error01():
    print(f"Opciones Válidas: {list(itertools.chain(*zip(respTrue,respFalse)))}")
    return

print(f"\n{titulo}")
print ('*'*len(titulo))
while salir:
    preg = (input('Responde a estímulos (si/no):  ').lower())
    if preg in respTrue or preg in respFalse:
        if preg in respTrue:
            print('\n*** Valora la necesidad de llevarlo al hospital más cercano ***\n')
            salir = False
        else:
            while salir:
                preg=(input('\n*** Abrir vía Aérea ***\n\n¿Respira? (si/no): ').lower())
                if preg in respTrue or preg in respFalse: 
                    if preg in respTrue:
                        print('*** Permitirle posición de suficiente ventilación ***\n')
                        salir = False
                    else: print('\n*** Administrar 5 Ventilaciones y llamar a Ambulancia ***\n')
                    while salir:
                        preg = (input('Signos de Vida (si/no): ').lower())                     
                        if preg in respTrue or preg in respFalse:
                            if preg in respTrue: print('\n*** Reevaluar a la espera de la Ambulancia ***\n')
                            else: print('\n*** Administrar Compresiones Torácicas hasta que llegue ambulancia ***\n')
                            preg = (input('¿Llegó la Ambulancia? (si/no): ').lower())                    
                            if preg in respTrue: salir = False                        
                        else: error01()
                else: error01()
    else: error01()