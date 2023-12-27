jogador = dict()
gol_part = []
jogador['Nome'] = input('Nome do jogador: ')
jogador['partidas'] = int(input('Quantas partidas disputadas: '))
for c in range(1, (jogador['partidas'] + 1)):
    gol_part.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gol'] = gol_part[:]
print('-='*15)
for chave, valor in jogador.items():
    print(f'O campo \033[31m{chave}\033[m tem valor \033[31m{valor}\033[m')
print('-='*15)
print(f'O jogador {jogador["Nome"]} jogou {jogador["partidas"]} partida(s).')
for n in range(0, jogador['partidas']):
    print(f'Na partida \033[31m{n+1}\033[m, fez \033[31m{gol_part[n]}\033[m gol(s)')
