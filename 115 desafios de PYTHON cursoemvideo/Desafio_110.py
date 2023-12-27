from utilidadesCeV.Moeda import moeda
from utilidadesCeV.dado.validadados import leiadinheiro
p = leiadinheiro('Digite o preço R$: ')
moeda.resumo(p, 40, 20)
