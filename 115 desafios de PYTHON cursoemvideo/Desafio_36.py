print('\033[1;31;40mFINANCIAMENTO DE UMA CASA\033[m')
casa = float(input('Qual o valor da casa: '))
sal  = float(input('Qual o valor do salário: '))
anos = int(input('Em quantos anos voçê vai pagar: '))
por30 = (sal * 30)/100
if casa /(anos * 12) <= por30:
    prestacao =  casa/(anos * 12)
    print('Voçê vai pagar por mês \033[31m{:.2f}\033[m'.format(prestacao))
else:
    print('Empréstimo negado')













