try:
    p = int(input('Ingrese el precio de suscripción: '))
    u = int(input('Ingrese el numero de usuarios: '))
    gt = int(input('Ingrese gasto total: '))
    u = p*u -gt
    print(f'La utilidad es : {u}')
except Exception:
    print('Ingrese un numero entero')
    