print('\033[31m-------Maior número-------\033[m')
n1 = int(input('Digite um número: '))
n2 = int(input('digite um número: '))
n3 = int(input('Digite um número: '))
maior = n1
if (n2 > maior):
    maior = n2
if(n3 > maior):
    maior = n3
menor = n1
if (n2 < menor):
    menor = n2
if(n3 < menor):
    menor = n3
print('O maior número é \033[33m{}\033[m e o menor é \033[36m{}\033[m'.format(maior, menor))
