aluno = dict()
aluno['nome'] = str(input('Qual o nome do aluno: '))
nota1 = float(input('Qual a primeira nota do aluno: '))
nota2 = float(input('Qual a segunda nota do aluno: '))
aluno['media'] = (nota1 + nota2) / 2
if ((nota1 + nota2) / 2) > 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média do {aluno["nome"]} é {aluno["media"]}')
print(f'Situação igual {aluno["situação"]}')
