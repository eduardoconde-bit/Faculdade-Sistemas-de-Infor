def dolareal():
    print('-- \033[34mConversor de Reais para Dólares\033[m --')
    reais = float(input('Digite quanto Dinheiro vc tem na carteira: '))
    dolar = reais / 5.56
    print(f'Voçê pode comprar {formatardolar(dolar)} Dólares')


def formatardolar(valordolar):
    return f'\033[31mU$ {valordolar:.2f}\033[m'


dolareal()
