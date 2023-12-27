aluno = []
dados = []
while True:
    dados.append(input('Digite o nome do aluno: '))
    dados.append(float(input('Digite a a primeira nota: ')))
    dados.append(float(input('Digite a a segunda  nota: ')))
    aluno.append(dados[:])
    dados.clear()
    resp = input('Voçê quer continuar (s/n): ').upper()
    if resp == 'N':
        break
print('  NOME      MÉDIA')
n = 1
for a in aluno:
    print(f'{n} {a[0].capitalize()}         {(a[1]+a[2])/2:.2f}')
    n += 1
print('-'*30)
escolha = 999
while escolha != 0:
    escolha = int(input('Mostrar nota de qual aluno [0 - encerra]: '))
    if escolha <= len(aluno):
        if escolha != 0:
            print(f'Notas de {aluno[escolha-1][0]} são {aluno[escolha-1][1]:.2f} , {aluno[escolha-1][2]:.2f}')
        print('-'*30)
    else:
        print('Notas inexistentes!')
print('Fim do Programa!')
