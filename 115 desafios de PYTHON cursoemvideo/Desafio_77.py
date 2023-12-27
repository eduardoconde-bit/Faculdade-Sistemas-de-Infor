nomes = ('aprender', 'programar','linguagem','phyton','curso','gratis','estudar','praticar','trabalhar','mercado')
n = 0
for c in range(0, len(nomes)):
    a = e = i = o = u = ''
    if 'a' in nomes[n]:
        a = 'a'
    if 'e' in nomes[n]:
        e = 'e'
    if 'i' in nomes[n]:
        e = 'i'
    if 'o' in nomes[n]:
        o = 'o'
    if 'u' in nomes[n]:
        u = 'u'
    print(f'Na palavra {nomes[n]} temos {a}{e}{i}{o}{u}')
    n += 1
print(f'{sorted(nomes[0])}')
palavra = nomes[0]
print(palavra)
