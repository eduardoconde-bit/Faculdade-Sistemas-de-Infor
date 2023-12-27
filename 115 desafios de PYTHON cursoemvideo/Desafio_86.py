lc = []
valor = []
c = 0
i = 0
print('\033[31m-----------MATRIZ-----------\033[m')
for n in range(0, 9):
    if i == 3:
        i = 0
    if n == 3:
        c = 1
    if n == 6:
        c = 2
    valor.append(int(input(f'digite o valor para {c, i}: ')))
    lc.append(valor[:])
    valor.clear()
    i += 1
print(lc[0], lc[1], lc[2])
print(lc[3], lc[4], lc[5])
print(lc[6], lc[7], lc[8])
