def fatorial(n, show=False):
    f = 1
    for c in range(1, n+1):
        f = f * c
    if show:
        for c in range(n, 1, -1):
            print(f'{c} * ', end='')
            n -= 1
        print(1, end=' ')
        print(f'= {f}')
        return ''
    else:
        return f'{f}'


print(fatorial(3, show=True))
