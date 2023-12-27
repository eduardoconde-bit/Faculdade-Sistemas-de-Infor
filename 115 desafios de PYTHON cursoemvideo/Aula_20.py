def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f = f * c
        print(f)
    print(' ')
    return f


print('_________________________________________')
print(f'O fatorial é {fatorial(n=int(input("Digite um numero: ")))}')
