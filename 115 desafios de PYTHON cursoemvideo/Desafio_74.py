from random import randint
n1 = randint(0, 20)
n2 = randint(0, 20)
n3 = randint(0, 20)
n4 = randint(0, 20)
n5 = randint(0, 20)
numeros = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram: \033[31m{} {} {} {} {}\033[m'.format(n1, n2, n3, n4, n5))
numeros = sorted(numeros)
print(f'O maior valor foi {numeros[4]}')
print(f'O menor valor foi {numeros[0]}')