print('\033[7;32m|||||||||||\033[35m CALCÚLO DO IMC \033[m\033[7;32m|||||||||||\033[m')
peso = float(input('\033[41m  \033[mDigite o peso: '))
altura = float(input('\033[41m  \033[mDigite a altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('\033[41m  \033[m\033[34mIMC\033[m igual a \033[32m{:.2f}\033[m, abaixo do peso'.format(imc))
elif imc >= 18 and imc <=25:
    print('\033[41m  \033[m\033[34mIMC\033[m igual a \033[32m{:.2f}\033[m, Peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('\033[41m  \033[m\033[34mIMC\033[m igual a \033[32m{:.2f}\033[m, Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('\033[41m  \033[m\033[34mIMC\033[m igual a \033[32m{:.2f}\033[m, Obesidade'.format(imc))
else:
    print('\033[41m  \033[m\033[34mIMC\033[m igual a \033[32m{:.2f}\033[m, Obesidade mórbida'.format(imc))
print('\033[7;32m|||||||||||\033[35m      FIM       \033[m\033[7;32m|||||||||||\033[m')
