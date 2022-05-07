try:
    p = int(input('Ingrese el precio de suscripción: '))
    u = int(input('Ingrese el numero de usuarios: '))
    gt = int(input('Ingrese gasto total: '))
    uante = float(input('Ingrese utilidad año anterior: '))
    u = p*u -gt
    last = ((u/uante)*100)-100
    
    print(f'La utilidad actual es: {u}')
    print(f'La razón con respecto al año anterior:{last:.2f}%')
except Exception:
    print('Ingrese un número válido')