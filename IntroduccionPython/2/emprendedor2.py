try:
    p = int(input('Ingrese el precio de suscripción: '))
    un = int(input('Ingrese el numero de usuarios normales: '))
    up = int(input('Ingrese el numero de usuarios premium: '))
    gt = int(input('Ingrese gasto total: '))
    u = p*(un+up*1.5) -gt
    print(f'La utilidad es : {u:.2f}')
except Exception:
    print('Ingrese un numero entero')