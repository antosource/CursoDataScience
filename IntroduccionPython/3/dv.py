import itertools

titulo = "\nCálculo Digito Verificador"
valido = list('0123456789')
serie = itertools.cycle((2,3,4,5,6,7))
print (titulo)
print ('*'*len(titulo))
run = True

while run:
    var = input('Ingrese rut sin puntos -> ')
    chk = [i for i in var if i not in valido]
    
    if not chk:
        inver = var[::-1]
        sum =0
        for num, ser in zip(inver,serie):
            sum += int(num)*ser
        dv = 11-sum%11
        if dv==10 : dv=0
        if dv==11 : dv="K"
        print (f"El dígito verificador es: {dv}\n")
        run = False
    else : print ('*** Ingrese solo numeros ***')
