from random import randint
jogo = []
jogos = int(input('Quantos jogos quer sortear?: '))
listadejogos = []
for n in range(0, jogos):
    for i in range(1, 7):
        jogo.append(randint(1, 60))
    listadejogos.append(jogo[:])
    jogo.clear()
i = 1
for play in listadejogos:
    print(f'jogo {i}: {sorted(play)}')
    i += 1
