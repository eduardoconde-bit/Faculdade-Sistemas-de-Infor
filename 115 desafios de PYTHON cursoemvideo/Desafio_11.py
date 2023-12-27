print('\033[30mPrograma que cálcula quantos litros de---')
print('tinta é necessário para pintar uma parede\033[m')
print('\033[35m/////////////////////////////////////////\033[m')
print('\033[31m---utilize metros para medição---\033[m')
print('\033[36m/////////////////////////////////////////\033[m')
L = float(input('\033[30mQual a largura da parede? '))
A = float(input('Qual a altura da parede? \033[m'))
Area = L * A
print('A area da Parede corresponde a {} m²'.format(Area))
Qtinta = Area / 2
print('É necessario {:.2f} Litros de tinta para pintar {:.2f} m²'.format(Qtinta, Area))

