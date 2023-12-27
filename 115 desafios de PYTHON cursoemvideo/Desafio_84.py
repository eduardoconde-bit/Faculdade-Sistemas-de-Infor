pessoas = []
dados = []
pesada = 0
nome_pesado = []
nome_leve = []
leve = 0
n = 1
while True:
    dados.clear()
    dados.append(input('Digite o nome: '))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    resp = input('Quer continuar (s) (n): ')
    if resp == 'n':
        break

for p in pessoas:
    if p[1] >= pesada:
        pesada = p[1]
        nome_pesado.append(p[0])

leve = pessoas[0][1]#peso da primeira pessoa da lista
nome_leve.append(pessoas[0][0])#nome da primeira da lista
for p in pessoas:
    n += 1
    if n > 1:
        if p[1] <= leve:#peso for mais leve que o mais leve
            leve = p[1]
            nome_leve.append(p[0])
if pessoas[0][1] < pesada:
    nome_pesado.pop(0)
if pessoas[0][1] != leve:
    del(nome_leve[0])
if n > 1:
    nome_leve.pop(0)
print(f'Foram cadastradas {len(pessoas)} pessoa(s)')
print(f'O maior peso foi {pesada}. Peso de {nome_pesado}')
print(f'O menor peso foi {leve}. Peso de {nome_leve}')
