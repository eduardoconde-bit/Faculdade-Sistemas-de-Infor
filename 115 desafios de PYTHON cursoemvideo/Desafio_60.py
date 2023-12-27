n = int(input('Digite um número: '))
c = 1
fatorial = 0
while c < n:
    if fatorial == 0:
        fatorial = n * c
    fatorial = fatorial * c
    c += 1
print('O fatorial de {} é {}'.format(n, fatorial))
