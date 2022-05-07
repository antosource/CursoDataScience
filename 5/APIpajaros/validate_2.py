def validate(valor):
    try:
        return int(valor)
    except:
        valor = input("Ingrese valor valido: ")
        return(validate(valor))