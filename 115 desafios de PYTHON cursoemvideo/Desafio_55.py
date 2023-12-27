peso = 0
maior = 0
menor = 0
for c in range(1, 6):
    print('{}ª pessoa'.format(c))
    peso = float(input('Digite seu peso: '))
    if peso > maior:
        maior = peso
    if c == 1:
        menor = peso
    if peso < menor:
        menor = peso
print('o maior peso foi {} e o menor peso foi {}'.format(maior, menor))
