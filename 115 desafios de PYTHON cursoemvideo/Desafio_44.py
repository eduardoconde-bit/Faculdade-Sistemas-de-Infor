print('\033[34m||||||\033[33mEscolha um opção de pagamento\033[m\033[34m||||||\033[m')
print('\033[32m1\033[m - Pagamento a vista  \033[32m2\033[m - A vista no cartão')
print('\033[32m4\033[m - Em até 2x no cartão  \033[32m4\033[m - 3x ou mais no cartão')
produto = float(input('Digite o preço normal do produto: '))
forma =  int(input('Digite a forma de pagamento: '))
if forma == 1:
    desc = (produto * 10)/100
    print('Preço a ser pago {:.2f} R$'.format(produto - desc))
elif forma == 2:
    desc = (produto * 5)/100
    print('Preço a ser pago {:.2f} R$'.format(produto - desc))
elif forma == 3:
    print('Preço a ser pago {:.2f} R$'.format(produto))
elif forma == 4:
    desc = (produto * 20)/100
    print('Preço a ser pago {:.2f} R$'.format(produto + desc))
