def voto(nasc):
    idade = 2021 - nasc
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos. \033[31mVoto Obrigatório\033[m'
    if idade < 18:
        return f'Com {idade} anos. \033[32mVoto Negado\033[m'
    if idade >= 65:
        return f'Com {idade} anos. \033[34mVoto Opcional\033[m'


nascimento = int(input('Digite o ano de nascimento: '))
print(voto(nascimento))
