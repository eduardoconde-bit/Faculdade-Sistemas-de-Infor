def escreva(texto):
    tam = len(texto)
    print('\033[31m~' * (tam))
    print(f'\033[32m{texto}\033[m')
    print('\033[31m~\033[m' * (tam))

for c in range(1, 4):
    escreva(texto=input('Digite um texto: '))
