def leiaint(string):
    while True:
        try:
            num = int(input(string))
        except (ValueError, TypeError):
            print('\033[31mERRO, Digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('Interrupção de usuário!')
            return 0
        else:
            return num


def leiafloat(string):
    while True:
        try:
            num = float(input(string))
        except (ValueError, TypeError):
            print('\033[31mDigite um número real válido\033[m')
        except KeyboardInterrupt:
            print('Interrupção de usuário!')
            return 0
        else:
            return num


n1 = leiafloat('Digite um número real: ')
n2 = leiaint('Digite um número inteiro: ')
print('\033[36m-'*20)
print(f'\033[32mVoçê acabou de digitar o número {n1:.2f}')
print(f'\033[32mVoçê acabou de digitar o número {n2}')
