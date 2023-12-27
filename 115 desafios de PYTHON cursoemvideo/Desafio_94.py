pessoa = {}
lista = []
mulheres = []
acimamedia = []
resp = 's'
n_pessoas = 0
media = 0
while resp == 's':
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['sexo'] = input('Digite o sexo: ').upper()
    pessoa['idade'] = int(input('Digite a idade: '))
    media += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    n_pessoas += 1
    resp = input('Quer continuar? \033[31m[s]\033[m \033[33m[n]\033[m: ')
c = 0
for people in lista:
    if people['sexo'] == 'F':
        mulheres.append(people['nome'])
media = media/n_pessoas
acimamedia = []
for people in lista:
    if people['idade'] > media:
        acimamedia.append(people)
print('-='*15)
print(f'\033[31mO grupo tem \033[30m{n_pessoas}\033[31m pessoa(s)\033[m')
print(f'\033[30mA média de idade é de {media:.2f} anos')
print(f'As mulheres cadrastadas foram: {mulheres[:]}\033[m')
print('')
print('\033[32mLISTA DAS PESSOAS QUE ESTÃO ACIMA DA MÉDIA: \033[m')
print('')
for people in acimamedia:
    print(f'\033[34mnome = {people["nome"]}; sexo = {people["sexo"]}; idade = {people["idade"]}')
    print('')
print('\033[31m<<<<FIM DO PROGRAMA>>>>\033[m')
