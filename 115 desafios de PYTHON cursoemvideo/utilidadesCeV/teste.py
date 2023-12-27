from utilidadesCeV.Moeda import moeda
from utilidadesCeV.dado import validadados


p = validadados.leiadinheiro('Digite um preço: ')
moeda.resumo(p, 40, 20)
