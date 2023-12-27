n50 = 0
n20 = 0
n10 = 0
n01 = 0
valor2 = 0
print('\033[30m=\033[m'*22)
print('\033[30m       BANCO L      \033[m')
print('\033[30m=\033[m'*22)
valor = int(input('Digite o valor de saque: '))
while True:
    while valor2 < valor:
        valor2 += 50
        n50 += 1
    if valor2 == valor:
        print(f'\033[31mTotal de {n50} cédula(s) de 50 R$')
        break
    if valor2 > valor:
        valor2 = valor2 - 50
    while valor2 < valor:
        valor2 += 20
        n20 += 1
    if valor2 == valor:
        print(f'\033[31mTotal de {n50-1} cédula(s) de 50 R$')
        print(f'Total de {n20} cédula(s) de 20 R$')
        break
    if valor2 > valor:
        valor2 = valor2 - 20
    while valor2 < valor:
        valor2 += 10
        n10 += 1
    if valor2 == valor:
        print(f'\033[31mTotal de {n50-1} cédula(s) de 50 R$')
        print(f'Total de {n20-1} cédula(s) de 20 R$')
        print(f'Total de {n10} cédula(s) de 10 R$')
        break
    if valor2 > valor:
        valor2 = valor2 - 10
    while valor2 < valor:
        valor2 += 1
        n01 += 1
    if valor2 == valor:
        print(f'\033[31mTotal de {n50-1} cédula(s) de 50 R$')
        print(f'Total de {n20-1} cédula(s) de 20 R$')
        print(f'Total de {n10-1} cédula(s) de 10 R$')
        print(f'Total de {n01} Moeda(s) de 1 R$')
        break
    if valor2 > valor:
        valor2 -= 1
