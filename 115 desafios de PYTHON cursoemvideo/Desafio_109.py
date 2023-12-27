from utilidadesCeV.Moeda import moeda
p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.formatar(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.dobro(p)}')
print(f'Aumentando 50%, temos {moeda.aumentar(p, 50)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(p, 15)}')
