import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

try:
    valor = int(sys.argv[1])
    print({k:v for k,v in ventas.items() if v>valor})
    
except ValueError:
    print ('\nFavor ingresar un número entero\n')