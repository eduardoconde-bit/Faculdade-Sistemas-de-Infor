print('\033[34;1m-------NÚMEROS PRIMOS-------\033[m')
for b in range(1, 11):
    contador = 0
    n = int(input('Digite um numero: '))
    c = 0
    for c in range(2, n):
        if n % c != 0:
            contador += 1
    if contador == n-2:
        print('\033[31mÉ um número primo\033[m')
    else:
        print('\033[30mNão é um número primo!\033[m')
