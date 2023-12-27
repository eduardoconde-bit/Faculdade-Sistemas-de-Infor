def parouimpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


resp = parouimpar(int(input('Digite um valor: ')))
print(f'O número é par?: {resp}')