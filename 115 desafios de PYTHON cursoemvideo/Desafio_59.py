resp = 0
while resp == 0:
    print('------OPÇÕES------')
    n1 = int(input('digite um valor: '))
    n2 = int(input('digite um valor: '))
    print('[1] - somar - [2] - multiplicar - [3] maior - [4] - novos números [5] - sair do programa')
    escolha = int(input('Digite a opção escolhida: '))
    if escolha == 1:
        print('A soma entre {} e {} é igual {}'.format(n1, n2, n1 + n2))
    if escolha == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    if escolha == 3:
        if n1 > n2:
            print('{} é o maior número'.format(n1))
        elif n2 > n1:
            print('{} é o maior número'.format(n2))
        else:
            print('Os número são iguais!')
    if escolha == 4:
        print('Um instante')
    if escolha == 5:
        resp = 1
print('\033[31mFIM DO PROGRAMA!\033[m')

