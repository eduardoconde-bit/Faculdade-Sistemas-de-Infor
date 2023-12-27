print('\033[33m----------Ajuste de Salário-----------\033[m')
print('\033[31m////////////////////////////////////\033[m')
S = float(input('Digite o valor do salário: '))
aumento = (S * 15) / 100  # calculo do valor do aumento
NewS = aumento + S
print('O novo salario é \033[33m{:.2f}\033[m'.format(NewS))
print('\033[31m////////////////////////////////////\033[m')
