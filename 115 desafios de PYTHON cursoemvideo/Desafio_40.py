nt1 = float(input('Digite a nota 1: '))
nt2 = float(input('Digite a nota 2: '))
media = (nt1 + nt2)/2
if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
