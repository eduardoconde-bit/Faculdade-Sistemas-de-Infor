from random import randint
pc = randint(1, 3)
print('\033[41m             \033[30;1mJOKENPÔ               \033[m')
print('\033[33m1\033[m - PEDRA | \033[36m2\033[m - PAPEL | \033[31m3\033[m - TESOURA')
u = int(input('\033[31mESCOLHA SUA JOGADA: '))
if pc != u:
    if (u == 1 and pc == 3) or (u == 2 and pc == 1) or (u == 3 and pc == 2):
        print('\033[1;33m--VITÓRIA DO USUARIO---\033[m')
    elif (pc == 1 and u == 3) or (pc == 2 and u ==1) or (pc == 3 and u == 2):
        print('\033[1;33m-----VITÓRIA DO PC-----\033[m')
elif pc == u:
    print('\033[1;32m--------EMPATE--------  \033[m')
if u > 3:
    print('JOGADA INVÁLIDA')
print('\033[30mjogada do usuário:    \033[32m{}\033[m'.format(u))
print('\033[30;41m        FIM        \033[m')
print('\033[30mjogada do computador: \033[32m{}\033[m '.format(pc))
print('\033[41m             \033[1;30mJOKENPÔ\033[m\033[41m               \033[m')
