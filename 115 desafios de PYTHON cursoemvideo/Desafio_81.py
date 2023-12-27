lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Voçê quer continuar (s) ou (n): ')
    if resp == 'n':
        break
print(f'Foram digitados {len(lista)} elementos!')
lista.sort(reverse=True)
print(f'A lista de forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado, faz parte da lista!')
else:
    print('O valor 5 não está na lista!')
