def validate(valor):
    while type(valor)!=int:
        try:
            return int(valor)
        except:
            valor = input("Ingrese valor valido: ")