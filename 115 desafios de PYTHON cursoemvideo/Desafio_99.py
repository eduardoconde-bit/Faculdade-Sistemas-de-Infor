def linha():
    print('-'*40)


def maior(*num):
    maior = 0
    for i in num:
        if i > maior:
            maior = i
    linha()
    print(f'Foram passados {len(num)} valores no total')
    print(f' O maior valor é {maior}')


maior(1, 3, 6, -1)
maior(10, 1000, 10, 10, 10)
maior(3, 30, 2)
linha()
