lista = []
pares = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Voçê quer continuar (s) ou (n): ')
    if resp == 'n':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impar.append(lista[c])
print(f'A lista gerada é {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impar}')
