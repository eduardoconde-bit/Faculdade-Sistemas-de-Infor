from random import randint
c = 0
while True:
    jogada = int(input('Par (1), Ímpar (2): '))
    valor = int(input('digite o valor: '))
    pc = randint(1, 10)
    if jogada == 1:
        if (valor + pc) % 2 == 0:
            print('Vitória do usuário!')
            c += 1
        else:
            print('Vitória da máquina !')
            break
    if jogada == 2:
        if (valor + pc) % 2 == 1:
            print('Vitória do usuário!')
            c += 1
        else:
            print('Vitória da máquina')
            break
print(f'\033[31mO jogador teve {c} vitória(s) consecutiva(s)\033[m')
