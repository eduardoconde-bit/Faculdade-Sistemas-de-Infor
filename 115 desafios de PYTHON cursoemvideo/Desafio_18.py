from math import sin, cos, tan, radians
angulo = int(input('\033[31mDigite o ângulo: \033[m'))
seno = sin(radians(angulo))
print('{:.2f}'.format(seno))
cosseno = cos(radians(angulo))
print('{:.2f}'.format(cosseno))
tangente = tan(radians(angulo))
print('{:.2f}'.format(tangente))
