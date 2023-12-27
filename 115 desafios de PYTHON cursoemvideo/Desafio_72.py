contagem = ('Zero','Um','Dois','Três','Quatro','Cinco','seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
c = 0
print('-----NÚMERO POR EXTENSO-----')
while True:
    if c == 0:
        n = int(input('Digite um número entre 0 e 20: '))
        if n >= 0 and n <= 20:
            break
    c += 1
    n = int(input('Tente novamente. Digite um número entre [0] e [2]: '))
    if n >= 0 and n <= 20:
        break
print(f'\033[30mVoçê digitou o número\033[31m {contagem[n]}')

