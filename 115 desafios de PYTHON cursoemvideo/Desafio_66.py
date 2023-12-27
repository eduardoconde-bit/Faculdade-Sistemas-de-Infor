n = s = c = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma entre os números é {s} ,{c} números foram digitados')
