import math
proteina = float(input("Ingrese los gramos de proteinas: \n"))
carbo = float(input("Ingrese los gramos de carbohidratos: \n"))
grasa = float(input("Ingrese los gramos de grasa: \n"))

calorias = 4*(proteina+carbo)+grasa*9

print (f'El total de calorias es: {math.ceil(calorias)}')
