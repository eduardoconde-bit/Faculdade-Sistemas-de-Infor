print('\033[43;30;1m   ALISTAMENTO DO EXÉRCITO   \033[m')
nasc = int(input('digite o ano de nascimento: '))
ano_atual = int(input('digite o ano atual: '))
idade = ano_atual - nasc
if idade < 18:
    print('\033[31mAlistamento futuro\033[m')
    print('\033[30mAinda faltam {} ano(s)\033[m'.format(18 - idade))
elif idade == 18:
    print('\033[31mAlistamento liberado\033[m')
else:
    print('\033[31mO período de alistamento já passou\033[m')
    print('\033[30mPassou-se {} ano(s) do prazo\033[m'.format(idade - 18))
print('\033[41;30m       FIM DO PROGRAMA       \033[m')
