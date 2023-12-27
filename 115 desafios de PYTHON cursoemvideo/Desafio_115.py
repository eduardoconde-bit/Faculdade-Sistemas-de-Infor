from TEXTO import texto
while True:
    texto.menu()
    resp = texto.escolha('\033[7;1mDIGITE A OPÇÃO:\033[m ')
    if resp == 1:
        texto.lertexto()
    elif resp == 2:
        texto.cadrastro()
    elif resp == 3:
        break
    else:
        print('-'*30)
        print('\033[35mDIGITE UMA OPÇÃO VÁLIDA\033[m')
        print('-' * 30)
print()
print('\033[35mObrigado por utilizar este programinha!')