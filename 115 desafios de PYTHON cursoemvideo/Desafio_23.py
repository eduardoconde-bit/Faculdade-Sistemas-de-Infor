numeros = int(input('Digite um número entre 0 e 9999: '))
numeros = str(numeros)
numeros = numeros[::-1]
print('Unidades: {}'.format(numeros[0]))
print('Dezenas: {}'.format(numeros[1]))
print('Centenas: {}'.format(numeros[2]))
print('Milhar: {}'.format(numeros[3]))
