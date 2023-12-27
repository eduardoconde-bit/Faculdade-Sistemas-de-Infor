n = 17
Tabela = ('Vasco','Flamengo','Corinthians','Fluminense','Palmeiras','Internacional','Bahia','Atlético Mineiro','São Paulo','Grêmio','Cruzeiro','Sport','Goiás','América','Ponte Preta','Avaí','Santos','Criciúma','Fortaleza','Paysandu')
print(f'\033[30;44;1m{Tabela}\033[m')
print(f'Os 5 primeiros \033[31m{Tabela[0:5]}\033[m')
print(f'Os quatro últimos \033[31m{Tabela[-4:]}\033[m')
print(f'Ordem alfabética \033[31m{sorted(Tabela)}\033[m')
print(f'\033[31m{Tabela[7]}\033[m está na 8º colocação')
