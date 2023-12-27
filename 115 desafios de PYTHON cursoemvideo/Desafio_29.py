print('\033[31;40;1;3m      Programa de Multas     \033[m')
vc = int(input('\033[36;1;3mDigite a velocidade: \033[m'))
if vc > 80:
    multa  = 7 * (vc - 80)
    print('\033[31;1mVOÇÊ FOI MULTADO! \033[m')
    print('\033[30;1mO VALOR DA MULTA É\033[m \033[31m{:>7}\033[m \033[30mR$\033[m'.format(multa))
if vc <= 80:
    print('|||| Velocidade correta ||||')
print('\033[40;31;1m    ---FIM DO PROGRAMA---    \033[m')
