totalgasto = 0
mais1000 = 0
maisbarato = 0
print('\033[34m--------Produtos--------\033[m')
while True:
    produto = input('Digite o nome: ')
    preco = float(input('Digite o preço: '))
    totalgasto += preco
    if maisbarato == 0:
        maisbarato = preco
    if preco < maisbarato:
        maisbarato = preco
    if preco > 1000:
        mais1000 += 1
    resp = input('Quer continuar (s) (n): ')
    if resp == 'n':
        break
print(f'O total gasto na compra é de \033[31m{totalgasto:.2f}\033[m R$')
print(f'{mais1000} produto(s) custa(m) mais de 1000 R$')
print(f'O produto mais barato custa {maisbarato} R$')
