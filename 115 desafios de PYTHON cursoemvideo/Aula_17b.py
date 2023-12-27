pessoa = []
dados = []
totmaior = totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite a idade: ')))
    pessoa.append(dados[:])
    dados.clear()
for p in pessoa:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmenor += 1
print(f'O total de maiores de idade é {totmaior}')
print(f'O total de menores de idade é {totmenor}')
