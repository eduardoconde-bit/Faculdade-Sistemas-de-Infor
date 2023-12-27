def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome}, fez {gols} gols no campeonato.')


nomejogador = input('nome do jogador: ')
qgols = input('Números de Gols: ')


if nomejogador == '' and qgols != '':
    qgols = int(qgols)
    ficha(gols=qgols)
elif nomejogador != '' and qgols == '':
    ficha(nome=nomejogador)
elif nomejogador != '' and qgols != '':
    qgols = int(qgols)
    ficha(nomejogador, qgols)
else:
    ficha()
