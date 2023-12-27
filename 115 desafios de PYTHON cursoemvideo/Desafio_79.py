valores = []
while True:
    numero = (int(input('Digite valores: ')))
    if numero not in valores:
        valores.append(numero)
    else:
        print('Valor já cadastrado!')
    resp = input('Voçê  quer interromper: (s) ou (n): ')
    if resp == 's':
        break
print(f'Ordem: {sorted(valores)}')
