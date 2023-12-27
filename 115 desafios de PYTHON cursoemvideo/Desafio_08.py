print('\033[1;41;30m<<<<<Programa conversor de medidas>>>>>\033[m')
v = float(input('Quantos Metros voçê quer converter?: '))
print('O valor em centimetros é \033[31m{:.2f}\033[m'.format(v * 10 * 10))
print('o valor em milimetros é \033[31m{:.2f}\033[m'.format(v * 10 * 10 * 10))
