listagem = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
n = 0
n1 = 1
print('\033[31;1m=\033[m'*29)
print('\033[30;1m     LISTAGEM DE PREÇOS      ')
print('\033[31;1m=\033[m'*29)
for c in range(0, 9):
    print(f'\033[30;1m{listagem[n]:.<20}R$ {listagem[n1]:>6}')
    n += 2
    n1 += 2

