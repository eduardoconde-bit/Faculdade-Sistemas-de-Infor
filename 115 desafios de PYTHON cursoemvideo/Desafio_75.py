n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
n3 = int(input('digite um número: '))
n4 = int(input('digite um número: '))
c = 0
numero = (n1, n2, n3, n4)
print(f'O número 9 apareceu {numero.count(9)} vez(es)')
if numero.count(3) == True:
    print(f'O primeiro valor 3 apareceu na posição {numero.index(3)+1}')
else:
    print(f'O valor 3 nao aparece em nenhuma posição!')
for n in range(0,4):
    if numero[n] % 2 == 0:
        c += 1
print(f'Os valores pares apareceram {c} vez(es)')
