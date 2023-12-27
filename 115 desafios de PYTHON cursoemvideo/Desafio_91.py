from random import randint
from time import sleep
jogador = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
print('----Jogo de dados----')
v = input('')
jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)
for k, v in jogador.items():
    print(f'{k} tirou {v}')
    sleep(0.5)
print('')
n = 1
print('Ranking dos jogadores: ****')
for item in sorted(jogador, key=jogador.get):
    print(f'{n}° lugar  jogador {n} com {jogador[item]}')
    n += 1
    sleep(0.7)
print()
