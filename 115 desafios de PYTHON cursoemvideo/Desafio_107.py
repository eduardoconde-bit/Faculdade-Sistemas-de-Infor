#Não Funciona, pois o código foi melhorado em outro desafio subsequente a esse (109)!
#A funcionalidade formatar foi incluída em nas outras funcionlidades como parâmetro
from utilidadesCeV.Moeda import moeda
p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.formatar(p)} é {moeda.formatar(moeda.metade(p))}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.formatar(moeda.dobro(p))}')
print(f'Aumentando 20%, temos {moeda.formatar(moeda.aumentar(p, 20))}')
print(f'Diminuindo 20%, temos {moeda.formatar(moeda.diminuir(p, 20))}')
