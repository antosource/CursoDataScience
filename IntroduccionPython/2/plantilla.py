nombre = input("Ingrese su Nombre: > ")
edad = input("Ingrese Edad: > ")
ocupacion = input("Ingrese Ocupación: > ")
lugar = input("En dónde?: > ")
caracteristica_1 = input("Ingrese 3 características:\n1. > ")
caracteristica_2 = input("2. > ")
caracteristica_3 = input("3. > ")
pasatiempo = input("Cuál es tu pasatiempo: > ")
hacer = input("¿Que quieres hacer? > ")

#al usar f''' el texto sale tal como se escribe sin necesidad de \n
print(f''' 
Mi nombre es {nombre}, tengo {edad} años y me desempeño como {ocupacion} en {lugar}.

Soy una persona {caracteristica_1}, {caracteristica_2} y {caracteristica_3}.
Mi pasatiempo es {pasatiempo} y me gustaría poder {hacer}.''')
