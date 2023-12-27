maior_idade = 0
menoridade = 0
for c in range(1, 4):
    print('{}ª pessoa'.format(c))
    ano_nasc = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano  atual: '))
    if ano_atual - ano_nasc >= 21:
        maior_idade = maior_idade + 1
    else:
        menoridade = menoridade + 1
print('{} maior(es) de idade'.format(maior_idade))
print('{} menor(es) de idade'.format(menoridade))
