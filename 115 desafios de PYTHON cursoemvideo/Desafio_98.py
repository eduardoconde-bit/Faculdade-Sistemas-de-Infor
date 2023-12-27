from time import sleep


def contador(inicio, fim, passo=1):
    # Contagem automática
    print('Contagem: ', end='')
    for c in range(inicio, fim+1, passo):
        print(c, end=' ')
        sleep(0.4)
    print()
    passo = 2
    print('Contagem: ', end='')
    for c in range(fim, inicio-2, -passo):
        print(c, end=' ')
        sleep(0.4)
    print()
    # Contagem Personalizada
    i = int(input('Digite o ínicio da contagem: '))
    f = int(input('Digite o fim da contagem: '))
    p = int(input('Digite o passo da contagem: '))
    if i < f:
        print('Contagem: ', end='')
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.4)
    else:
        print('Contagem: ', end='')
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.4)


contador(1, 10)
