n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rs = n1 % n2
print('A soma vale {}, A multiplicação vale {}, A divisão vale {:.5f}'.format(s, m, d), end=', ')
print('A divisão inteira é {}, A exponenciação vale {}'.format(di, e))
print('O resto da divisão é {}'.format(rs))

