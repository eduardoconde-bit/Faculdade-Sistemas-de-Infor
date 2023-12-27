# Declaração de dados
jogador = dict()
jogadores = []
gol_part = []  # Gols por partida
somadegols = []
v = 0
# Inicio do programa
while True:
    jogador['Nome'] = input('\033[33mNome do jogador: ')
    jogador['partidas'] = int(input('Quantas partidas disputadas: \033[m'))
    for c in range(1, (jogador['partidas'] + 1)):
        gol_part.append(int(input(f'\033[34mQuantos gols na partida {c}: \033[m')))
    for g in gol_part:
        v += g
    somadegols.append(v)
    v = 0
    jogador['gol'] = gol_part[:]
    gol_part.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    resp = input('Quer continuar: (s) (n)?: ').upper()
    if resp == 'N':
        break
print('-='*15)
print('\033[30mCod nome        gols        total\033[m')
print('-'*30)
v = 0
for objeto in jogadores:
    print(f'\033[30m{v+1} {objeto["Nome"]:<8}     {objeto["gol"]:}        {somadegols[v]}\033[m')
    v += 1
v = 1
while True:
    print('\033[30m-=\033[m'*15)
    resp = int(input('\033[31mMostrar dados de qual jogador (999 encerra): \033[m'))
    if resp <= len(jogadores):
        resp -= 1
        print(f'\033[30mDados do jogador {jogadores[resp]["Nome"]}\033[m')
        for c in jogadores[resp]["gol"]:
            print(f'\033[32mNa partida {v} fez {c} gol(s)\033[m')
            v += 1
    elif resp == 999:
        break
    elif resp != 999 and resp > len(jogadores):
        print('ERRO! jogador não existe.')
print("\033[34mPROGRAMA ECERRADO!\033[m")
