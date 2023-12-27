maior18 =   0
homem = 0
menor20 = 0
sexo = ''
while True:
    idade = int(input('Digite a idade:  '))
    valida = False
    while valida == False:
        sexo = input('Digite o sexo (m) ou (f): ')
        if sexo == 'm' or sexo == 'f':
            valida = True
    if idade > 18:
        maior18 += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f':
        if idade < 20:
           menor20 += 1
    resp = input('Voçê quer continuar (s) ou (n): ')
    if resp == 'n':
        break
print(f'{maior18} pessoa(s) tem mais de 18 anos')
print(f'{homem} homem(s) cadastrado(s)')
print(f'{menor20} mulher(es) tem menos de 20 anos!')
