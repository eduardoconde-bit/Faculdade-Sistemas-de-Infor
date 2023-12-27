dv = int(input('\033[30;1mQual a distância da viagem(Km): '))
if dv <= 200:
    print('O preço da passagem custa : {:.2f}'.format(dv * 0.50))
else:
    print('O preço da passagem custa : {:.2f}'.format(dv * 0.45))
print('\033[44;30;1m-------Fim do programa-------\033[m')
