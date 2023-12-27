num = 0
for n in range(1, 7):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        num += valor
print('Soma dos numeros pares {}'.format(num))
