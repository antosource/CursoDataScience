import sys

peso = float(sys.argv[1])
talla = float(sys.argv[2])

talla = talla / 100
imc = peso/talla**2 

if imc >= 40:
    clasif = 'Obesidad Grado 3'
elif imc >=35:
    clasif = 'Obesidad Grado 2'
elif imc >=30:
    clasif = 'Obesidad Grado 1'
elif imc >=25:
    clasif = 'Sobrepeso'
elif imc >=18.5:
    clasif = 'Adecuado'
else:
    clasif = 'Bajo Peso'
    
print (f'Su IMC es {imc:.2f}\nLa clasificación OMS es {clasif}')