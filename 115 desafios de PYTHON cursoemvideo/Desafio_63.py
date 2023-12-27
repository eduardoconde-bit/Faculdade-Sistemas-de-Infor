a = 0
p = 0
while p < 50:
    print(p)
    p = p + a
    a = p - a
    if p == 0:
        p = p + 1
