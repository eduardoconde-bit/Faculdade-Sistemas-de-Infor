def aumentar(valoraumentar, porcentagem1, valorformatar=True):
    """

    -----Função (aumentar()) aumenta em x porcento um valor e retorna-o----

    :param valoraumentar: Valor que vai ser aumentado (x) porcentagem
    :param porcentagem1: valor que vai ser aumentado em porcento
    :param valorformatar: Valor lógico para formatação ou não é opcional, True sem parâmetro, mostra o valor formatado
     False parâmetro explicitado não exibe o valor formatado
    :return: sim/yes
    """
    if valorformatar:
        a = ((porcentagem1/100) * valoraumentar) + valoraumentar
        return formatar(a)
    else:
        a = ((porcentagem1/100) * valoraumentar) + valoraumentar
        return a


def diminuir(valordiminuir, porcentagem2=0, valorformatar=True):
    """
    -----Função (diminuir()) diminui em x porcento um valor e retorna-o----

    :param valordiminuir: Valor que vai ser diminuido (x) porcentagem
    :param porcentagem2: valor em por cento que vai ser diminuído do valordiminuir
    :param valorformatar: Valor lógico para formatação ou não, é opcional, True sem parâmetro, mostra o valor formatado
     False parâmetro explicitado não exibe o valor formatado
    :return: sim/yes
    """
    if valorformatar:
        b = valordiminuir - ((porcentagem2/100) * valordiminuir)
        return formatar(b)
    else:
        b = valordiminuir - ((porcentagem2/100) * valordiminuir)
        return b


def dobro(valordobro, valorformatar=True):
    if valorformatar:
        c = valordobro * 2
        return formatar(c)
    else:
        c = valordobro * 2
        return c


def metade(valormetade, valorformatar=True):
    if valorformatar:
        d = valormetade / 2
        return formatar(d)
    else:
        d = valormetade / 2
        return d


def formatar(valorformatar):
    return f'\033[32mR$ {valorformatar:.2f}\033[m'


def resumo(valor, por1, por2):
    print('-'*38)
    print('\033[30;46;1m           RESUMO DO VALOR            \033[m')
    print('-'*38)
    print(f'{"Dobro do preço":28} {dobro(valor):<11}')
    print(f'{"Metadade do preço":28} {metade(valor):<11}')
    print(f'{por1}{"% de Aumento":26} {aumentar(valor, por1):<11}')
    print(f'{por2}{"% de redução":26} {diminuir(valor, por2):<11}')
