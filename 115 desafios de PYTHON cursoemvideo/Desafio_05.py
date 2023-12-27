def sucesantec(valor):
    """
    Função para mostrar o sucessor e antecesor um número
    :param valor: parâmetro  que recebe o argumento de uma variável com valor inteiro
    :return: nenhum
    """
    print('\033[31mSucessor e antecessor\033[m')
    s = valor + 1
    a = valor - 1
    print('O sucessor de \033[34m{}\033[m é \033[34m{}\033[m'.format(valor, s))
    print('O antecessor de \033[34m{}\033[m é \033[34m{}\033[m'.format(valor, a))


n1 = int(input('Digite um numero: '))
sucesantec(n1)
help(sucesantec)
