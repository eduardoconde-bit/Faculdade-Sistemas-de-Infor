par_impar = []
par = []
impar = []
for n in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par_impar.append(par)
par_impar.append(impar)
print(f'Os valores pares digitados: {sorted(par_impar[0])}')
print(f'Os valores ímpares digitados: {sorted(par_impar[1])} ')
