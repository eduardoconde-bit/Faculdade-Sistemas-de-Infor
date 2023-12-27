print('\033[31mCLASSIFICADOR DE CATEGORIA\033[m')
nasc = int(input('digite o ano de nascimento: '))
idade = 2020 - nasc
if idade <= 9:
    print('Categoria \033[36mMirim\033[m')
elif idade > 9 and idade <= 14:
    print('categoria \033[31minfantil\033[m')
elif idade > 14 and idade <= 19:
    print('Categoria \033[33mJunior\033[m')
elif idade == 20:
    print('Categoria \033[30mSênior\033[m')
else:
    print('categoria \033[32mMaster\033[m')
