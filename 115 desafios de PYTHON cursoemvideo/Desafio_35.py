l1 = int(input('Digite um lado do triângulo: '))
l2 = int(input('Digite um lado do triângulo: '))
l3 = int(input('Digite um lado do triângulo: '))
if l1 < (l2 + l3) and l1 > abs(l2 - l3):
    print('Os lados podem formar um triângulo')
else:
    print('Os lados não podem formar um triâgulo')
