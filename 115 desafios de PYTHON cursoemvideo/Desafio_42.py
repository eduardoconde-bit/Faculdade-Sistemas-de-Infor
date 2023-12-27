l1 = int(input('Digite um lado do triângulo: '))
l2 = int(input('Digite um lado do triângulo: '))
l3 = int(input('Digite um lado do triângulo: '))
print()
if l1 < (l2 + l3) and l1 > abs(l2 - l3):
    print('Os lados podem formar um triângulo')
    if l1 == l2 == l3:
        print('È um triângulo \033[30mEquilátero\033[m')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('É um triângulo \033[31mIsósceles\033[m')
    else:
        print('É triângulo \033[32mEscaleno\033[m')
else:
    print('Os lados não podem formar um triâgulo')
