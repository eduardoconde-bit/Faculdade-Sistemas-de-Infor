nome = ''
idade = 0
sexo = ''
somatorio = 0
maior = 0
maisvelho = ''
menor20 = 0
for c in range(1, 5):
    print('{}ª pessoa'.format(c))
    nome = input('Digite  o nome: ')
    idade = int(input('Digite a idade: '))
    somatorio += idade
    sexo = input('Digite o sexo (m) (f): ')
    if sexo == 'm':
        if idade > maior:
            maior = idade
            maisvelho = nome
    if sexo == 'f':
        if idade < 20:
            menor20 += 1
media = somatorio/4
print('\033[30;41m|||||||||||||||||||||||||||||||\033[m')
print('A média de idade é \033[31m{}\033[m anos'.format(media))
print('O nome do homem mais velho é \033[31m{}\033[m'.format(maisvelho))
print('\033[31m{}\033[m mulher(es) tem menos de 20 anos'.format(menor20))
