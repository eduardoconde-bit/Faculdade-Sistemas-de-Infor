valida = 0
while valida == 0:
    resp = input('Digite o sexo: ').upper()
    if resp == 'M' or resp == 'F':
        valida = 1
    print('Digite novamente')
print('FIM')
