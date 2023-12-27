from random import randint
numeros = []


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('Números: ', end='')
    for c in numeros:
        print(c, end=' ')
    print()


def somapar():
    soma = 0
    for e in numeros:
        if e % 2 == 0:
            soma += e
    print(f'A soma entre todos os números pares é {soma}')


sorteia()
somapar()
