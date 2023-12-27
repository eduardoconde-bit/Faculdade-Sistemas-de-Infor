sal = float(input('Digite o valor do salário: '))
if sal <= 1250:
    sal_1 = (15 / 100) * sal
    sal = sal + sal_1
    print('O novo valor do salário é {}'.format(sal))
else:
    sal_1 = (10 / 100) * sal
    sal = sal + sal_1
    print('O valor do novo salário é {}'.format(sal))
print('Fim do programa')
