import math

r = float(input('Ingrese el radio en Kilómetros: '))
g = float(input('Ingrese la constante g: '))
ve = math.sqrt(2*g*r*1000)

print(f'La velocidad de Escape es {ve:.2f} [m/s]')