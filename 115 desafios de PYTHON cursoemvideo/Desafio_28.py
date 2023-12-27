from random import randint
n1 = randint(0, 5)
resp = int(input('Tente adivinhar um número entre 0 e 5 que estou pesando: '))
if n1 == resp and n1 < 6:
    print('Voçe acertou o valor é {}'.format(n1))
else:
    print('Voce errou o valor que pensei é {}'.format(n1))

