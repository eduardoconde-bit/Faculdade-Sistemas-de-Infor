dados = {}
dados['Nome'] = input('Nome: ')
dados['Idade'] = int(input('Ano de Nascimento: '))
dados['Idade'] = 2020 - dados['Idade']
dados['CTPS'] = int(input('Carteira de trabalho: '))
if dados['CTPS'] == 0:
    print('-='*15)
    print(f'Nome tem o  valor {dados["Nome"]}')
    print(f'Idade tem o valor {dados["Idade"]}')
    print(f'CTPS tem o valor {dados["CTPS"]}')
else:
    ano_contrato = int(input('Ano de contratação: '))
    sal = float(input('Salário R$: '))
    dados['contratação'] = ano_contrato
    dados['Salário'] = sal
    aposentadoria =  dados['Idade'] + (35 - (2020 - ano_contrato))
    dados['Aposentadoria'] = aposentadoria
    print('-='*15)
    for chave, valor in dados.items():
        print(f'\033[m{chave}\033[m tem valor \033[31m{valor}\033[m')
