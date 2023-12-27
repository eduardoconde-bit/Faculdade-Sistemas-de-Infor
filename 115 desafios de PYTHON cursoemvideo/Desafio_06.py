print('\033[1;41m||||||||||||||||||\033[m')


def dobrotriplo():
    n1 = int(input('\033[33mDigite um numero:\033[m '))
    print('O dobro de ',n1,' é {}'.format(n1 * 2))
    print('O triplo de ',n1,' é {}'.format(n1 * 3))
    print('A raiz quadrada de ',n1,' é {:.2f}'.format(n1**(1/2)))


dobrotriplo()
