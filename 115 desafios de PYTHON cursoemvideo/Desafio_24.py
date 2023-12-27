print('verifica se o nome de uma cidade começa com santo')
cidade = str(input('digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
