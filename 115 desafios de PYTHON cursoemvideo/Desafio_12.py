def fim():
    print('\033[3;1;7;30m         FIM DO PROGRAMA         \033[m')


def desproduto():
    print('\033[1;3;30m-----Desconto de produtos-----\033[m')
    P_produto = float(input('\033[30mDigite o preço do produto: '))
    desc_0 = float(input('Digite quanto quer descontar em %: '))
    desc = (desc_0 * P_produto)/100
    P_produto = P_produto - desc
    print("O novo preço do produto é {:.2f} R$\033[m".format(P_produto))


desproduto()
fim()
