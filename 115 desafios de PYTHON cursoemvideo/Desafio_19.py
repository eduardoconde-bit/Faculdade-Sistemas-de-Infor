from random import choice
print('Sorteador de aluno')
a1 = input('Digite o nome do aluno 1 ')
a2 = input('Digite o nome do aluno 2 ')
a3 = input('Digite o nome do aluno 3 ')
a4 = input('Digite o nome do aluno 4 ')
sorteado = choice([a1, a2, a3, a4])  # A funcionalidade choice escolhe um elemento aleatoriamente
print('Quem irá apagar o quadro é \033[33m{}'.format(sorteado))  # de uma lista (blioteca random).

# Vesão Melhorada! 2022-04-18 - 15:33
print('Sorteador de aluno')
student = []
for i in range(0, 4):
    al = input(('Digite o nome do aluno: '))
    student.append(al)
sorted = choice(student)  # A funcionalidade choice escolhe um elemento aleatoriamente
print('Quem irá apagar o quadro é \033[33m{}'.format(sorted))  # de uma lista (blioteca random).
