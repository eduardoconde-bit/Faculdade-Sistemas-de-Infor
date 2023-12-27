s = 0
for n in range(1, 500+1):
    if (n % 2) == 1:
        if n % 3 == 0:
            s += n
            print(n)
