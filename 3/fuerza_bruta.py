from string import ascii_lowercase
import getpass

run = True
while run:
    clave = getpass.getpass('\nIngrese clave a probar: ')
    letras =list(ascii_lowercase)
    clave = list(clave.lower())
    chk = [i for i in clave if i not in letras]
    total=0
    if not chk:
        for i in clave:
            for j in letras:
                if i==j:
                    total=total+letras.index(j)
        print(f"La contraseña fue forzada en {total+len(clave)} intentos\n")
        run = False
    else : print(f'\nERROR: la clave solo puede contener {ascii_lowercase}\n')