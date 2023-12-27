numeros = []
maior = 0
menor = 0
for c in range(0, 5):
    num = int(input('Digite valores: '))
    numeros.append(num)
for c in range(0, 5):
    if numeros[c] > maior:
        maior  = numeros[c]
    if c == 0:
        menor = numeros[c]
    if numeros[c]  < menor:
        menor = numeros[c]
sorted(numeros)
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
