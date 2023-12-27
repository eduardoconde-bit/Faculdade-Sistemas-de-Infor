valores = list()
for c in range(0, 5):
    valores.append(int(input('digite valores: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c+1} achei o valor {v}')
print('Final da lista')
